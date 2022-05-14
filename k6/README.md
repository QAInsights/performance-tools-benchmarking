# K6 stepping pattern

## Pre-requisites

### Install k6
1. `sudo apt-get update`
2. `sudo apt-get install k6`

## Run the test
3. `mkdir [project_path]/k6/results`
4. `k6 run [project_path]/k6/scripts.js --out json=[project_path]/k6/results/results.json`

## Outputs
- `[project_path]/k6/results/results.json`