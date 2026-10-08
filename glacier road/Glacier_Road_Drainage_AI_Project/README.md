# AI/ML-Driven Glacier Lakes, Road Networks & Urban Drainage Change Analysis

A reproducible Python 3.11 geospatial AI project built from the four supplied project documents. It implements the planned Modules A–D:

- **Module A:** glacial lake detection using MNDWI/NDWI baseline, Random Forest, and U-Net; inventory, trends and screening indicators.
- **Module B:** road extraction using segmentation, skeleton/graph processing and topology-aware comparison.
- **Module C:** urban drainage screening using DEM hydrology, open-channel mapping, built-up/impervious change and SAR waterlogging indicators.
- **Module D:** change analysis, trend statistics, uncertainty/accuracy hooks, Streamlit dashboard and experiment tracking.

## Important scope
This repository is the **implementation package** derived from the supplied documents. No satellite scenes, labels, municipal GIS or final reference measurements were supplied, so it does not fabricate model results. Put/download the required data into `data/` and run the pipeline.

The supplied specification explicitly limits the project to screening-level analysis: 10 m imagery cannot resolve narrow roads/small drains, underground drains are not visible from satellite data, and the project is not an operational early-warning or engineering design system.

## Quick start

```bash
conda env create -f environment.yml
conda activate geoai
python scripts/verify_env.py
python scripts/run_demo.py
```

For real data, edit `config/config.yaml`, place prepared rasters/labels in `data/`, then run:

```bash
python scripts/run_pipeline.py --module lakes
python scripts/run_pipeline.py --module roads
python scripts/run_pipeline.py --module drainage
python scripts/run_pipeline.py --module change
streamlit run app/dashboard.py
```

## Data expected
The project specification calls for Sentinel-2 L2A, Sentinel-1, Landsat, Copernicus GLO-30 DEM, OSM, glacier inventories, WorldCover/Dynamic World and optional reference/benchmark datasets. Acquisition can be done through public catalogues such as Planetary Computer, Copernicus Data Space and Google Earth Engine.

## Repository layout

```text
config/                  Project configuration
src/geoai/               Reusable implementation modules
scripts/                 CLI entry points and environment/demo checks
app/                     Streamlit dashboard
notebooks/               Suggested analysis notebook entry points
data/                    Raw/intermediate/processed/external data
models/                  Trained model weights
mlruns/                  MLflow runs
reports/                 Figures/tables/reports
 tests/                  Automated smoke/unit tests
```

## Recommended experiment sequence
1. Establish AOIs and time periods.
2. Acquire and preprocess data.
3. Freeze spatial train/validation/test splits and label version.
4. Run the MNDWI/NDWI baseline.
5. Run Random Forest.
6. Run U-Net and compare optical vs optical+SAR vs optical+SAR+terrain.
7. Build lake inventories and trends.
8. Train road segmentation, then graph/skeleton post-processing.
9. Build drainage hydrology and waterlogging indicators.
10. Compare post-classification and learned change detection where data allow.
11. Validate independently and record every experiment.

## Outputs
The intended outputs are GeoPackage inventories, GeoTIFF probability/mask/change layers, CSV/Parquet statistics, figures, an interactive dashboard and a reproducible experiment log.
