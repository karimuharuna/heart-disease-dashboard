# Heart Disease Data Dashboard & Risk Predictor

An interactive dashboard and prediction tool exploring heart disease risk 
using the UCI Heart Disease dataset (920 patients, 16 clinical features).

🔗 **Live app:** [https://karimuharuna-heart-disease-dashboard-dashboard-qqvs5h.streamlit.app/]
kaggle link- https://www.kaggle.com/code/harunakarimu/notebookbb8f2ec435

## Background

As a medic with interest health data/IT, I built this project 
to combine clinical knowledge with hands-on data analysis, machine learning, 
and web app development — going from raw CSV to a deployed, interactive tool.

## What it does

- Loads and cleans the UCI Heart Disease dataset
- Visualizes patterns in disease severity by sex and other factors
- Trains a logistic regression model to predict disease risk
- Provides an interactive form where a user enters patient values and 
  gets a live risk prediction

## Key findings

- Average disease severity was notably higher in male patients (1.15) 
  than female patients (0.42)
- Model achieved ~80-82% accuracy on held-out test data
- Strongest predictors: sex, exercise-induced angina, and ST depression 
  (oldpeak) — all clinically consistent with known ischemic risk markers
- Chest pain type showed a counterintuitive pattern: asymptomatic 
  presentation was associated with *higher* predicted risk than named 
  chest pain types, likely reflecting silent ischemia in this referral 
  population
- Lowering the classification threshold from 0.5 to 0.35 improved recall 
  for true disease cases (82% → 87%) with only a small precision trade-off 
  — a clinically meaningful choice, since missing a real case is costlier 
  than a false alarm in a screening context

## Tech stack

- **Python** — pandas, scikit-learn (logistic regression)
- **Streamlit** — interactive dashboard and prediction form
- **Streamlit Community Cloud** — deployment

## Data source

[UCI Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) 
via Kaggle

## Limitations & what I'd add next

- Model trained on one dataset/population — not validated externally
- Numeric features aren't standardized, so coefficient magnitudes aren't 
  fully comparable across features
- `ca` and `thal` columns excluded due to high missingness — richer 
  models could handle this more carefully
- Would like to add: model comparison (e.g. random forest), saved/cached 
  model instead of retraining on every app run

## Run it locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

**Disclaimer:** This is a learning project, not a validated clinical tool.
