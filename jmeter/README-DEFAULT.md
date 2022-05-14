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

### Set default heap size
6. `vim [jmeter_path]/apache-jmeter-5.4.3/bin/jmeter`
7. at line _166_ set `: "${HEAP:="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m"}"`


## Run the test
7. `mkdir [project_path]/jmeter/results`
8. `[jmeter_path]/apache-jmeter-5.4.3/bin/jmeter -n -t [project_path]/jmeter/example.jmx -l [project_path]/jmeter/results/results.jtl`

## Outputs
- `[project_path]/jmeter/results/results.jtl`