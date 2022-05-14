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
2. `locust -f [project_path]/locust/locustfile.py  --headless --users 1000 --run-time 15m --spawn-rate 16 --html=[project_path]/locust/results/test.html`

## Outputs
- `[project_path]/locust/results/test.html `