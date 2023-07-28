import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')

#function to load the data only once
@st.cache_data()
def load_spend_data():
    df = pd.read_csv('datasets/spend_data.csv')
    return df

st.title("CUSTOMER SEGMENTATION ANALYSIS ")

with st.spinner("loading dataset"):
    df=load_spend_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show spend datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 
    
st.subheader('Customer dataset')
rows,cols=df.shape       
age = df['age']
gender_count = df['gender'].value_counts()

c1, c2,c3 = st.columns(3)
c1.metric('Total customers', rows)    
c2.metric('Total Columns', cols)



st.subheader('Analysis of  customer records')
fig1 = px.pie(gender_count, gender_count.index, gender_count.values, title='gender distribution')
st.plotly_chart(fig1, use_container_width=True)
st.info("the dataset has equal gender distribution")

st.subheader('Area graph of income distribution')
df_inc = df.sort_values(by='income', ascending=False)
fig3 = px.histogram(df_inc,'income',title='income distribution')
education_df=df.groupby('education')['income'].sum()
#st.write(education_df)
fig4=px.pie(education_df,education_df.index,'income',title='income in different education level')
df_inc=df.sort_values(by='education',ascending=False)
fig5=px.bar(df_inc,'country',title='country distribution')
gender_df=df.groupby('gender')['income'].sum()
fig6=px.pie(gender_df,gender_df.index,'income',title='income in different gender distribution')
st.plotly_chart(fig3, use_container_width=True)
age_df=df.groupby('age')['income'].sum()
fig7=px.bar(age_df,age_df.index,'income',title='income in different age')
st.info("the income distributed is even,and there are no big difference in the group")
st.plotly_chart(fig4, use_container_width=True)
st.info("The bachelors group earns the most of these groups")
st.plotly_chart(fig5, use_container_width=True)
st.plotly_chart(fig6,use_container_width=True)
st.info("income in different gender distributionn is equal")
st.plotly_chart(fig7,use_container_width=True)
st.info("income  distribution respect to age")

