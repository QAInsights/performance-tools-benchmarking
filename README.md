# performance-tools-benchmarking

## Table of Contents
1. [JMeter](./jmeter/README.md)
2. [K6](./k6/README.md)
3. [Locust](./locust/README.md)


## Test scenario
1. Each user sends a get request to [petclinic](https://petclinic.ycrash.io) api every 1 second.
2. Test follows a stepping pattern
    1. start from 0
    2. add 50 users evert 30 seconds
    3. all the way up to 1000 users
    4. hold for additional 60 seconds.

