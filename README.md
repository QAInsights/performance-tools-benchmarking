# performance-tools-benchmarking

## Experiments ot run

|   #	| mode          	| howto 	                            |
| :---  |    :----:         |    ---:                               |
| 1 	| JMeter        	| [link](./jmeter/README.md)  	        |
| 2 	| K6            	| [link](./k6/README.md)  	            |
| 3 	| Locust-single 	| [link](./locust/README-SINGLE.md)  	|
| 4 	| Locust-dist   	| [link](./locust/README-DIST.md)  	    |

## Test scenario
1. Each user sends a get request to [petclinic](https://petclinic.ycrash.io) api every 1 second.
2. Test follows a stepping pattern
    1. start from 0
    2. add 50 users evert 30 seconds
    3. all the way up to 1000 users
    4. hold for additional 60 seconds.

