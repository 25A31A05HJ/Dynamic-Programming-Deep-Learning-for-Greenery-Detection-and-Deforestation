## Dataset

This repository includes a **synthetic dataset of 1,000 records** for studying greenery and deforestation detection using vegetation-related time-series and similarity measures.

### File

- `greenery_deforestation_synthetic_1000_records.csv` — Synthetic dataset containing 1,000 observations and 35 features.

### Dataset Description

The dataset contains information about different ecosystems, vegetation conditions, environmental factors, deforestation events, and model predictions. It can be used to experiment with **deforestation detection, vegetation-loss analysis, time-series similarity measures, and severity classification**.

### Main Features

| Feature | Description |
|---|---|
| `record_id` | Unique identifier for each observation |
| `ecosystem` | Ecosystem type, such as Moist forest or Mangrove |
| `latitude_deg` | Latitude of the observation |
| `longitude_deg` | Longitude of the observation |
| `phenology_shift_days` | Shift in seasonal vegetation patterns |
| `amplitude_factor` | Vegetation-seasonality amplitude factor |
| `baseline_offset` | Baseline vegetation offset |
| `cloud_fraction` | Fraction of observations affected by cloud cover |
| `observed_count` | Number of observations available |
| `clearing_event` | Indicates whether a clearing event occurred |
| `clearing_day` | Day on which the clearing event occurred |
| `clearing_ndvi_level` | NDVI level associated with the clearing event |
| `drought_event` | Indicates whether a drought event occurred |
| `drought_duration_days` | Duration of the drought event |
| `drought_magnitude` | Magnitude of the drought |
| `mean_ndvi_observed` | Mean observed NDVI |
| `std_ndvi_observed` | Standard deviation of observed NDVI |
| `ndvi_drop_from_reference` | NDVI reduction from the reference level |
| `mean_vegetation_fraction` | Mean vegetation fraction |
| `vegetation_loss_fraction` | Fraction of vegetation lost |
| `true_gli` | Reference/true greenery-loss indicator |
| `gli_uncorrected` | Uncorrected greenery-loss indicator |
| `gli_twdtw_corrected` | Time-weighted DTW corrected greenery-loss indicator |
| `euclidean_score` | Similarity/distance score using Euclidean distance |
| `standard_dtw_score` | Similarity score using standard Dynamic Time Warping |
| `twdtw_ndvi_score` | Time-weighted DTW score based on NDVI |
| `proposed_dpdl_score` | Score produced by the proposed DPDL approach |
| `true_deforestation_label` | Reference deforestation label |
| `euclidean_prediction` | Deforestation prediction using Euclidean distance |
| `standard_dtw_prediction` | Deforestation prediction using standard DTW |
| `twdtw_ndvi_prediction` | Deforestation prediction using time-weighted DTW |
| `proposed_dpdl_prediction` | Deforestation prediction using the proposed DPDL method |
| `true_severity` | Reference deforestation severity |
| `uncorrected_severity` | Severity estimated from the uncorrected indicator |
| `twdtw_severity` | Severity estimated using the time-weighted DTW approach |

### Dataset Statistics

- **Records:** 1,000
- **Features:** 35
- **Format:** CSV
- **Dataset type:** Synthetic
- **Primary application:** Vegetation and deforestation analysis

### Download

The complete dataset is available in this repository:

[Download `greenery_deforestation_synthetic_1000_records.csv`](./greenery_deforestation_synthetic_1000_records.csv)

### Example Usage

```python
import pandas as pd

df = pd.read_csv("greenery_deforestation_synthetic_1000_records.csv")

print(df.shape)
print(df.head())
print(df["ecosystem"].value_counts())
```

> **Note:** This is a synthetic dataset intended for research, experimentation, demonstrations, and algorithm evaluation. It should not be treated as real-world satellite or environmental monitoring data.
