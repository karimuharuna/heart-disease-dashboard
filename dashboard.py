import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Heart Disease Data Dashboard')

df = pd.read_csv('heart_disease_uci.csv')

st.write('Here is a preview of the data:')
st.dataframe(df.head())
st.write('Average disease severity by sex:')
fig, ax = plt.subplots()
df.groupby('sex')['num'].mean().plot(kind='bar', ax=ax)
ax.set_ylabel('Average severity score (0-4)')
st.pyplot(fig)
st.write('Average disease severity by age:')
fig, ax = plt.subplots()
df.groupby('age')['num'].mean().plot(kind='bar', ax=ax)
ax.set_ylabel('Average severity score (0-4)')
st.pyplot(fig)
st.write('Average disease severity by cholesterol:')
fig, ax = plt.subplots()
df.groupby('chol')['num'].mean().plot(kind='bar', ax=ax)
ax.set_ylabel('Average severity score (0-4)')
st.pyplot(fig)
st.write('Average disease severity by fasting blood sugar:')
fig, ax = plt.subplots()
df.groupby('fbs')['num'].mean().plot(kind='bar', ax=ax)
ax.set_ylabel('Average severity score (0-4)')
st.pyplot(fig)
column = st.selectbox('Compare disease severity by:', ['sex', 'age', 'chol', 'fbs'])
fig, ax = plt.subplots()
df.groupby(column)['num'].mean().plot(kind='bar', ax=ax)
st.pyplot(fig)