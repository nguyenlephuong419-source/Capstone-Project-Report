# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Applied Data Science Capstone project files. Submit the presentation PDF and the URL of this repository in the corresponding fields of the course assignment.

## Contents

- `spacex_sql_completed.ipynb`: executed SQL tasks on the 101-row course dataset.
- `spacex_eda_completed.ipynb`: executed EDA plots and 90 × 83 feature matrix.
- `spacex_ml_completed.ipynb`: executed logistic regression, SVM, decision tree and KNN; all scored 15/18 on the test split.
- `spacex_map_completed.ipynb`: executed Folium map code using the 56-row geography snapshot.
- `spacex_api_completed.ipynb`: reproducible IBM snapshot fallback and data wrangling.
- `spacex_scraping_completed.ipynb`: reproducible IBM table fallback.
- `spacex_scraping_parser.ipynb`: filled original 2021 Wikipedia HTML parser; archived page access was unavailable during this run.
- `spacex_dash_app.py`: interactive Dash dashboard with site filter and payload slider.
- `dataset_part_1.csv`, `dataset_part_2.csv`, `spacex_sql_source.csv`, and `spacex_launch_geo.csv`: fixed course snapshots.

## Run

```bash
pip install -r requirements.txt
jupyter lab
python spacex_dash_app.py
```

Start Jupyter Lab from the repository root, then open notebooks in order: API, scraping, SQL, EDA, map and machine learning. The files are in the repository root. The snapshot notebooks refer to the course datasets in this directory. The executed SQL, EDA, ML and map notebooks already contain their outputs.

## Source and limitations

The fixed datasets were downloaded from IBM DS0321EN course resources. The live SpaceX API returned HTTP 525 and the archived Wikipedia page timed out in this environment. The fallback notebooks state these limitations rather than presenting snapshot rows as live API or scraping results. The model comparison uses a small 18-row held-out test set, so the 83.3% tie does not establish a unique best model.
