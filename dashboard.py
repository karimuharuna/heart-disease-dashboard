import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.title('Heart Disease Data Dashboard')

# Load data
df = pd.read_csv('heart_disease_uci.csv')

st.write('Here is a preview of the data:')
st.dataframe(df.head())

# Chart: sex vs severity
st.write('Average disease severity by sex:')
fig, ax = plt.subplots()
df.groupby('sex')['num'].mean().plot(kind='bar', ax=ax)
ax.set_ylabel('Average severity score (0-4)')
st.pyplot(fig)

# --- Prepare data for the model ---
df['has_disease'] = (df['num'] > 0).astype(int)

features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak']
X = df[features].copy()
y = df['has_disease']

for col in ['trestbps', 'chol', 'thalch', 'oldpeak']:
    X[col] = X[col].fillna(X[col].median())
for col in ['fbs', 'restecg', 'exang']:
    X[col] = X[col].fillna(X[col].mode()[0])

X = pd.get_dummies(X, columns=['sex', 'cp', 'fbs', 'restecg', 'exang'], drop_first=True)
model_columns = X.columns  # save this order, we'll need it for predictions

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- Prediction form ---
st.header('Predict Disease Risk')

age_input = st.slider('Age', 20, 90, 50)
sex_input = st.selectbox('Sex', ['Male', 'Female'])
cp_input = st.selectbox('Chest pain type', ['typical angina', 'atypical angina', 'non-anginal', 'asymptomatic'])
trestbps_input = st.slider('Resting blood pressure', 80, 200, 120)
chol_input = st.slider('Cholesterol', 100, 400, 200)
fbs_input = st.selectbox('Fasting blood sugar > 120 mg/dl', ['False', 'True'])
restecg_input = st.selectbox('Resting ECG', ['normal', 'st-t abnormality', 'other'])
thalch_input = st.slider('Max heart rate achieved', 60, 220, 150)
exang_input = st.selectbox('Exercise-induced angina', ['False', 'True'])
oldpeak_input = st.slider('ST depression (oldpeak)', 0.0, 6.0, 1.0)

if st.button('Predict'):
    # Build a single-row dataframe matching the training data's format
    input_df = pd.DataFrame([{
        'age': age_input,
        'trestbps': trestbps_input,
        'chol': chol_input,
        'thalch': thalch_input,
        'oldpeak': oldpeak_input,
        'sex_Male': 1 if sex_input == 'Male' else 0,
        'cp_atypical angina': 1 if cp_input == 'atypical angina' else 0,
        'cp_non-anginal': 1 if cp_input == 'non-anginal' else 0,
        'cp_typical angina': 1 if cp_input == 'typical angina' else 0,
        'fbs_True': 1 if fbs_input == 'True' else 0,
        'restecg_normal': 1 if restecg_input == 'normal' else 0,
        'restecg_st-t abnormality': 1 if restecg_input == 'st-t abnormality' else 0,
        'exang_True': 1 if exang_input == 'True' else 0,
    }])

    # Ensure column order matches training data exactly
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    probability = model.predict_proba(input_df)[0][1]
    st.write(f'**Predicted probability of heart disease: {probability:.1%}**')

    if probability >= 0.35:
        st.warning('Model suggests elevated risk — flagged using a lowered threshold (0.35) to prioritize catching true cases.')
    else:
        st.success('Model suggests lower risk.')