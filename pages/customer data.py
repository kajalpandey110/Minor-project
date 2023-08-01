import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')

#function to load the data only once
@st.cache_data()
def load_spend_data():
    df = pd.read_csv('datasets/Customer_Data.csv')
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
BALANCE = df['BALANCE']
CUST_count = df['CUST_ID'].value_counts()
BALANCE_count = df['BALANCE_FREQUENCY'].value_counts()

c1, c2,c3 = st.columns(3)
c1.metric('Total customers', rows)    
c2.metric('Total Columns', cols)

st.subheader('Analysis of  customer records')
fig1 = px.pie(BALANCE_count, BALANCE_count.index, BALANCE_count.values, title='Customer distribution')
st.plotly_chart(fig1, use_container_width=True)

PURCHASE_df=df.groupby('PURCHASES')['BALANCE_FREQUENCY'].sum()
# st.write(education_df)
fig2=px.bar(PURCHASE_df,PURCHASE_df.index,'BALANCE_FREQUENCY',title='PURCHASES in differentBALANCE_FREQUENCY ')
st.plotly_chart(fig2,use_container_width=True)

CREDIT_df=df.groupby('CREDIT_LIMIT')['PAYMENTS'].sum()
fig3=px.area(CREDIT_df,CREDIT_df.index,'PAYMENTS',title='CREDIT_df in different PAYMENT')
st.plotly_chart(fig3,use_container_width=True)

MINIMUM_df=df.groupby('MINIMUM_PAYMENTS')['PAYMENTS'].sum()
fig4=px.area(CREDIT_df,CREDIT_df.index,'PAYMENTS',title='MINIMUM_df in different PAYMENT')
st.plotly_chart(fig4,use_container_width=True)