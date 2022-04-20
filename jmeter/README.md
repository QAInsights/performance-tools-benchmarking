# JMeter stepping pattern

## Pre-requisites

### install Open-JDK with
1. `sudo apt update`
2. `sudo apt install default-jdk`
3. `java -version`:
```
openjdk version "11.0.14.1" 2022-02-08
OpenJDK Runtime Environment (build 11.0.14.1+1-Ubuntu-0ubuntu1.18.04)
OpenJDK 64-Bit Server VM (build 11.0.14.1+1-Ubuntu-0ubuntu1.18.04, mixed mode, sharing)
```

### Download jmeter
4. `curl -O https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.4.3.tgz`
5. `tar -xvzf apache-jmeter-5.4.3.tgz`

### install custumed thread group plugin
6. `cd apache-jmeter-5.3/lib`
7. `curl -O https://repo1.maven.org/maven2/kg/apc/cmdrunner/2.3/cmdrunner-2.3.jar`
8. `cd ext`
9. `curl -O https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/1.7/jmeter-plugins-manager-1.7.jar`
10. `cd ..` (back to lib)
11. `java -jar cmdrunner-2.3.jar --tool org.jmeterplugins.repository.PluginManagerCMD install jpgc-casutg`

## Run the test
1. `mkdir [project_path]/jmeter/results`
2. `[jmeter_path]/apache-jmeter-5.4.3/bin/jmeter -n -t [project_path]/jmeter/example.jmx -l [project_path]/jmeter/results/results.jtl`

## Outputs
1. `[project_path]/jmeter/results/results.jtl`