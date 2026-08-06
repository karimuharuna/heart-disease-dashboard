# Heart Disease Data Dashboard

An interactive dashboard exploring patterns in heart disease severity using 
the UCI Heart Disease dataset (920 patients, 16 clinical features).

🔗 **Live app:** [https://karimuharuna-heart-disease-dashboard-dashboard-qqvs5h.streamlit.app/]

## Background

As a medical doctor transitioning into health data/IT, I built this project 
to combine clinical knowledge with hands-on data analysis and web app 
development — going from raw CSV to a deployed, interactive tool.

## What it does

- Loads and cleans the UCI Heart Disease dataset
- Explores relationships between patient characteristics (sex, age, 
  cholesterol, fasting blood sugar) and heart disease severity
- Visualizes findings as interactive bar charts in a web dashboard

## Key findings

- Average disease severity was notably higher in male patients (1.15) 
  than female patients (0.42) in this dataset
- Average disease severity was noted higher with high fasting blood sugar as well as high cholestorol as show in the chart
  
## Tech stack

- **Python** — pandas for data handling, matplotlib for visualization
- **Streamlit** — interactive web app framework
- **Streamlit Community Cloud** — deployment

## Data source

[UCI Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) 
via Kaggle

## What I'd add next

- Additional filters (e.g. by chest pain type, age range)
- Handle missing data in `ca` and `thal` columns more rigorously
- Add a simple prediction model alongside the exploratory charts

## Run it locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```
