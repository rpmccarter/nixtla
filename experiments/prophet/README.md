# TimeGPT vs Prophet: Time Series Forecasting Benchmark

## Overview

This repository offers a detailed benchmarking framework for comparing the performance of TimeGPT against Prophet and StatsForecast in time series forecasting. We provide datasets with over 300,000 series across various frequencies, including daily, weekly, 10-minute, and hourly intervals. Users can also incorporate their own datasets for a more personalized analysis. **TimeGPT was not trained on this datasets.**


## Notes

- Results were generated using a VM with 96 cores and 196 GB of RAM.
- Prophet and StatsForecast was executed in paralell.
- TimeGPT uses the AzureML endpoint.
- Since the AzureML endpoint does not support GPU and scalable requests, the results can improve.

## Repository Structure

- `/data`: Parquet files with time series data.
- `/src`: Source code for running benchmarks and experiments.
- `/data/results`: Outputs and analysis from benchmark runs.

## Data Structure

Datasets should adhere to this structure:

- **unique_id**: Identifier for each series.
- **ds**: Timestamp of observation.
- **y**: Target variable for forecasting.
- **frequency**: Description of data frequency (e.g., 'Daily').
- **pandas_frequency**: Pandas frequency string (e.g., 'D').
- **h**: Forecasting horizon. (The last `h` periods of each series will be used as test.)
- **seasonality**: Seasonality of the series (e.g., 7 for daily).

## Running Experiments

### Makefile

The repository includes a Makefile to streamline the process of running experiments. The key commands are:

1. **evaluate**: Runs the evaluation for a specified method (`timegpt`, `prophet`, or `statsforecast`).
2. **summarize_results**: Summarizes the results from the evaluation.

### Evaluation Flow

1. **Run Evaluation**: Use `make evaluate method=<method_name>` where `<method_name>` is either `timegpt`, `prophet`, or `statsforecast`. The script filters out files containing specific strings (like 'catalogue') and runs the experiment for each `.parquet` file in the `/data` directory. The results will be written in `/data/results`. 

2. **Summarize Results**: After running evaluations for each method, execute `make summarize_results` to aggregate and summarize the results, which will be written in this `README.md` file.

## Getting Started

1. **Prepare Data**: Ensure your Parquet files are in `/data`. If you want access to the original datasets, please write to `ops@nixtla.io` with your use case.
2. **Create conda environment**: Run `conda env create -f environment.yml` and activate the environment using `conda activate timegpt-benchmark`.
3. **Run Benchmarks**: Use the Makefile commands to run evaluations and summarize results.


## Results
<This section is automatically generated by results_summary.py>

### Data Description

| file           | frequency   |   n_series |      mean |        std |   min_length |   max_length |       n_obs |
|:---------------|:------------|-----------:|----------:|-----------:|-------------:|-------------:|------------:|
| 10Minutely_10T | 10Minutely  |         17 |     2.919 |      6.095 |        3,000 |        3,000 |      51,000 |
| 30Minutely_30T | 30Minutely  |        556 |     0.233 |      0.329 |        3,000 |        3,000 |   1,668,000 |
| Daily_D        | Daily       |    103,529 |   178.763 |  5,825.784 |           14 |        3,000 | 251,217,667 |
| Hourly_H       | Hourly      |        227 |   635.332 |  4,425.693 |          748 |        3,000 |     590,653 |
| Minutely_T     | Minutely    |         34 |    44.612 |    106.121 |        3,000 |        3,000 |     102,000 |
| Monthly_MS     | Monthly     |     97,588 | 4,280.461 | 72,939.696 |           24 |        1,456 |   9,116,399 |
| Quarterly_QS   | Quarterly   |      2,539 | 4,722.366 |  9,521.907 |           18 |          745 |     253,160 |
| Weekly_W-MON   | Weekly      |     98,144 | 1,388.030 | 99,852.095 |            9 |          399 |  35,096,195 |

### Performance


| file           | metric   |   TimeGPT |   Prophet |   SeasonalNaive |
|:---------------|:---------|----------:|----------:|----------------:|
| 10Minutely_10T | mae      | **0.976** |     2.758 |             1.0 |
| 10Minutely_10T | rmse     | **0.764** |     2.005 |             1.0 |
| 10Minutely_10T | time     | **0.147** |     0.565 |             1.0 |
|----------------|----------|-----------|-----------|-----------------|
| 30Minutely_30T | mae      |   **0.6** |     0.661 |             1.0 |
| 30Minutely_30T | rmse     | **0.652** |     0.687 |             1.0 |
| 30Minutely_30T | time     | **0.318** |     7.498 |             1.0 |
|----------------|----------|-----------|-----------|-----------------|
| Daily_D        | mae      | **0.802** |     1.699 |             1.0 |
| Daily_D        | rmse     |  **0.78** |     1.479 |             1.0 |
| Daily_D        | time     | **0.544** |    48.019 |             1.0 |
|----------------|----------|-----------|-----------|-----------------|
| Hourly_H       | mae      | **0.855** |     1.124 |             1.0 |
| Hourly_H       | rmse     | **0.881** |     1.048 |             1.0 |
| Hourly_H       | time     | **0.134** |     3.426 |             1.0 |
|----------------|----------|-----------|-----------|-----------------|
| Minutely_T     | mae      | **0.732** |     1.349 |             1.0 |
| Minutely_T     | rmse     | **0.705** |     1.207 |             1.0 |
| Minutely_T     | time     | **0.088** |     0.786 |             1.0 |
|----------------|----------|-----------|-----------|-----------------|
| Monthly_MS     | mae      | **0.728** |      1.41 |             1.0 |
| Monthly_MS     | rmse     | **0.686** |     1.196 |             1.0 |
| Monthly_MS     | time     |      7.02 |   118.178 |         **1.0** |
|----------------|----------|-----------|-----------|-----------------|
| Quarterly_QS   | mae      | **0.966** |     1.384 |             1.0 |
| Quarterly_QS   | rmse     | **0.974** |     1.313 |             1.0 |
| Quarterly_QS   | time     |     1.218 |    18.685 |         **1.0** |
|----------------|----------|-----------|-----------|-----------------|
| Weekly_W-MON   | mae      | **0.878** |     2.748 |             1.0 |
| Weekly_W-MON   | rmse     | **0.878** |     2.748 |             1.0 |
| Weekly_W-MON   | time     |    12.489 |    85.611 |         **1.0** |
|----------------|----------|-----------|-----------|-----------------|
<end>