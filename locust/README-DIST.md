# Locust stepping pattern

## Pre-requisites

### Install python 3.10
1. `sudo apt update && sudo apt upgrade -y`
2. `sudo apt install software-properties-common -y`
3. `sudo add-apt-repository ppa:deadsnakes/ppa`
4. press `enter` to continue
5. `sudo apt install python3.10`
6. `python3.10 --version`
7. `sudo apt install python3.10-venv`

### Setup virtual environment
1. `python -m venv [project_path]/venv`
2. `[project_path]/bin/activate`

### Install python dependencies
1. `pip install locust==2.8.6`

## Run the test
1. `mkdir [project_path]/locust/results`
2. Run one master process - `locust -f [project_path]/locust/locustfile.py  --headless --csv=[project_path]/locust/results/test --master`
3. Run 2 worker processes:
    1.`locust -f [project_path]/locust/locustfile.py  --headless --csv=[project_path]/locust/results/test --worker --master-host=localhost`
    2.`locust -f [project_path]/locust/locustfile.py  --headless --csv=[project_path]/locust/results/test --worker --master-host=localhost` 

## Outputs
1. `[project_path]/locust/results/test_exceptions.csv`
2. `[project_path]/locust/results/test_failures.csv`
3. `[project_path]/locust/results/test_stats.csv`
4. `[project_path]/locust/results/test_stats_history.csv`

NOTE! - locust has an active bug under investigation [here](https://github.com/locustio/locust/issues/2075)