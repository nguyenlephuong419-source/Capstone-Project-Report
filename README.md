# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Applied Data Science Capstone project files. The presentation PDF is submitted separately to the course's **Question 2**. For **Question 1**, upload this repository to GitHub and submit the repository URL.

## Contents

- `notebooks/spacex_sql_completed.ipynb`: executed SQL tasks on the 101-row course dataset.
- `notebooks/spacex_eda_completed.ipynb`: executed EDA plots and 90 × 83 feature matrix.
- `notebooks/spacex_ml_completed.ipynb`: executed logistic regression, SVM, decision tree and KNN; all scored 15/18 on the test split.
- `notebooks/spacex_map_completed.ipynb`: executed Folium map code using the 56-row geography snapshot.
- `notebooks/spacex_api_completed.ipynb`: reproducible IBM snapshot fallback and data wrangling.
- `notebooks/spacex_scraping_completed.ipynb`: reproducible IBM table fallback.
- `notebooks/spacex_scraping_parser.ipynb`: filled original 2021 Wikipedia HTML parser; archived page access was unavailable during this run.
- `scripts/spacex_dash_app.py`: interactive Dash dashboard with site filter and payload slider.
- `data/`: fixed IBM course snapshots used by the notebooks and dashboard.

## Run

```bash
pip install -r requirements.txt
jupyter lab
python scripts/spacex_dash_app.py
```

Start Jupyter Lab from the repository root, then open notebooks in order: API, scraping, SQL, EDA, map and machine learning. For the snapshot fallback notebooks, run from the `notebooks` folder so that `../data/` resolves correctly. The executed SQL, EDA, ML and map notebooks already contain their outputs.

## Source and limitations

The fixed datasets were downloaded from IBM DS0321EN course resources. The live SpaceX API returned HTTP 525 and the archived Wikipedia page timed out in this environment. The fallback notebooks state these limitations rather than presenting snapshot rows as live API or scraping results. The model comparison uses a small 18-row held-out test set, so the 83.3% tie does not establish a unique best model.
