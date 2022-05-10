# Performance tools benchmarking

## Abstract

With more load testing tools coming up to the market, performance engineers are in a need to make a better informed decision as to the tool that best suites their needs.
One area of concern, is the tools computational resource consumption such as cpu, memory or I\O.
When the use of resources is excessive and the load testing tool is not performant, this can lead to unreliable results or high performance testing costs.

In our experiment, we've created a  load testing script of equal load model using 3 popular open-source load testing tools 1.JMeter; 2.K6; 3.Locust.
We've ran these scripts on a sterile environment and collected performance metrics from the load generator.


## Tools Overview


### JMeter

First introduced in 1998, JMeter is one of the longest standing load testing tools.
It's written in JAVA programming language and implements a thread based architecture, this means that every virtual user is a thread. running in our operating system.

Scripting is done with by using a GUI but can be extended with scripting code, mostly in Groovy language.

JMeter supports distributed execution using a manager-worker architecture, this way we can generate our load from multiple load agents.

JMeter supports various protocols like HTTP, MQTT, JMS, SMTP and many others, and it can be extended with plugins.

JMeter is supported by many Platform as a Service (PaaS) applications, enabling execution of performance tests in cloud environment easily.

### Locust
Locust is a python based open-source tool.
Unlike JMeter's thread based architecture, Locust is based on python asyncio module, which means that it runs on a single thread while I\O operations are performed concurrently.

Scripting is done in python and locust provide an easy interface to write performance test scripts, making the scripting supper easy and readable.

Locust supports distributed execution using a manager-worker architecture, but unlike JMeter, Locust also allows inter communication between the nodes which improves the ability to synchronize between the nodes and sharing data at run time.


Owing to pythons __Global Interpreter Lock__ (GIL), locust can only use a single CPU core at the time.
To take advantage of multiple cores, it is recommended to instantiate multiple workers on a single machine.

Locust supports various protocols like HTTP, MQTT, JMS, SMTP and many others, and it can be extended with plugins.

To the best of our knowledge there aren't many (or any) PaaS applications supporting locust for in cloud execution, which means that the implementation of cloud execution needs to be implemented by the developers.

### K6

K6 has recently been acquired by Grafana-labs and its being strongly maintained.
Written in Golang, it takes advantage of Golan's powerful concurrency abilities.

Scripting in K6 however is done with Javascript which is an interesting decision.
K6 creators believe that most programmers are more comfortable writing in Javascript, such that it would allow the tool to have the best of both worlds:
Golangs performance with Javascripts readability.

Unlike JMeter and Locust, K6 does not support distributed execution, for that purpose you need to use the commercial version that allows in cloud distributed execution.

A key advantage for K6 is the ease of integration with visualization tools, namely Grafana, DataDog or CloudWatch, as well as integration with IDE such as visual studio code or intelij.

K6 supports various protocols like HTTP, MQTT, JMS, SMTP and many others, and it can be extended with plugins.

|   #	                        | JMeter        | K6 	         |Locust|
| :---                          |    :----:     |    :---:       |---:       |
| __Runtime__ 	                | JAVA          | Golang         | Python    |
| __Scripting__ 	            | GUI + Groovy  | Javascript     | Python    |
| __Architecture__ 	            | Thread based  | Go routine     | Asyncio   |
| __Protocols supported__ 	    | Extensive     | Extensive      | Extensive |
| __Plugin extension__ 	        | difficult     | easy           | very easy |
| __distributed mode__ 	        | supported     | licensed       | supported |
>>>>>> table 1 - tools comparison


## Experimental material

### Setup

To evaluate performance of the 3 tools, we first set up a testing environment using a m4-large EC2 instance on AWS, it has 2 CPU cores and 8GB of memory.
We installed all required pre-requisites.
We used AWS cloud-watch to gather performance insights from the EC2 Instance

Our Software Under Test (SUT) is a demo 'pet-clinic' website developed by ycrash, we are using it's root path as our targeted API.
### Performance test scenario

Our performance test scenario is very simple, we spin up 1000 virtual users in a ramp-up period of 60 seconds, then each of the virtual users sends an http request every 1-5 seconds in a uniform distribution.
Load was kept for 1 hour

## Measurements:
1. CPU usage - collected from AWSs cloud-watch
2. Memory usage - collected from AWSs cloud-watch
3. Request rate - collected individually from the tools reporter
4. Network bytes sent - collected from AWSs cloud-watch

## Results

### 1. CPU Consumption

#### 1.1 JMeter:
![](images/JMETER-CPU.png)
>>>>>> image 1 - JMeter CPU consumption

#### 1.2 Locust single executor:
![](images/LocustSingle-CPU.png)
>>>>>> image 2 - Locust single CPU consumption

#### 1.3 Locust with 2 workers:
![](images/LocustDIST-CPU.png)
>>>>>> image 3 - Locust single CPU consumption

#### 1.4 K6:
![](images/K6_2-CPU.png)
>>>>>> image 4 - K6 CPU consumption

### 2. Memory Consumption

#### 2.1 JMeter:
![](images/JMETER-MEM.png)
>>>>>> image 5 - JMeter memory consumption

#### 2.2 Locust single executor:
![](images/LocustSingle-MEM.png)
>>>>>> image 6 - Locust single memory consumption

#### 2.3 Locust with 2 workers:
![](images/LocustDIST-MEM.png)
>>>>>> image 7 - Locust single memory consumption

#### 2.4 K6:
![](images/K6-MEM.png)
>>>>>> image 8 - K6 memory consumption

JMeter went up to 20% of memory usage, Locust single mode consumed 4.8% of memory while Locust with 2 executors consumed 5.7%.
K6 Memory usage progressed gradually from 13% to 18%

It seems like in all instances memory usage was not an issue, with JMeter performing worst, K6 performing slightly better, and Locust being most efficient in memory use.


### 3. Request rate

#### 3.1 JMeter:
![](images/JMETER-RequestRate.png)
>>>>>> image 9 - JMeter Request rate

#### 3.2 Locust single executor:
![](images/LocustSingle-RequestRate.png)
>>>>>> image 10 - Locust single Request rate

#### 3.3 Locust with 2 workers:
![](images/LocustDist-RequestRate.png)
>>>>>> image 11 - Locust distributed Request rate

#### 3.4 K6:
![](images/K6_2-Dashboard.png)
>>>>>> image 12 - K6 Request rate

When looking at request rates we see that all 4 executions performed ~315 requests per second.

However, locust performed with 0 errors, K6 performed with 59 errors in total which is negligible (0.006%), while JMeter performed with a constant rate of about 80 failures per second, around 21% of total requests failed.

So despite the fact that the CPU load was down by a half in JMeter, JMeter was out-performed by Locust and K6 when it comes to success rates.

When looking at the errors in JMeters dashboard we can see the error types:
![](images/JMeter-Dashboard.png)
>>>>>> image 13 - JMeter dashboard

```Non HTTP response code: org.apache.http.NoHttpResponseException/Non HTTP response message: petclinic.ycrash.io:443 failed to respond```

### 4. Network - bytes sent

#### 4.1 JMeter:
![](images/JMETER-nw-out.png)
>>>>>> image 14 - JMeter bytes out

#### 4.2 Locust single executor:
![](images/LocustSingle-nw-out.png)
>>>>>> image 15 - Locust single bytes out

#### 4.3 Locust with 2 workers:
![](images/LocustDist-nw-out.png)
>>>>>> image 16 - Locust distributed bytes out

#### 4.4 K6:
![](images/K6-nw-out.png)
>>>>>> image 17 - K6 bytes out

Locust did not show any difference in network traffic when executed in parallel mode vs single process, in both cases, traffic went up to 25M bytes per minute
Expectation was that adding additional worker will improve performance but it did not seem to be the case in this experiment.
One possible explanation for this could be that any improvement gained by using the 2 cores is lost to costly inter-process communication between the manager and the two workers.

K6 performed slightly better than Locust with 30M bytes per minute.

JMeter however lag far behind with 12M bytes per minute, demonstrating a sever performance bottleneck.

## Conclusions
... TBD
## External links
... TBD