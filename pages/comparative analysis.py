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

if st.sidebar.checkbox("Show spend dataset"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 
    
st.subheader('Comparative analysis')
st.sidebar.write(df.columns)

catcols = df.select_dtypes(include=object).columns
cat = st.radio("select a column to color", catcols[1:])
fig1 = px.scatter(df, 'age','income', color=cat)
st.plotly_chart(fig1 , use_container_width=True)

fig2 = px.scatter(df, 'spending','income', color=cat)
st.plotly_chart(fig2 , use_container_width=True)
fig3 = px.sunburst(df, path=['education','gender'], values='income',title='comparison between education and gender with respect to income' )
st.plotly_chart(fig3 , use_container_width=True)
fig4=px.scatter(df,'country','income',color=cat,title='comparison between country and income')
st.plotly_chart(fig4,use_container_width=True)
fig5=px.bar(df, 'purchase_frequency','income',color=cat,title='comparison between purchase_frequency and income')
st.plotly_chart(fig5,use_container_width=True)
fig6=px.scatter(df,'gender','country',color=cat,title='comparison between gender and country')
st.plotly_chart(fig6,use_container_width=True)
fig7 = px.sunburst(df, path=['education','age'], values='income',title=' comparison between education and age with respect to income' )
st.plotly_chart(fig7,use_container_width=True)
fig8 = px.sunburst(df, path=['education','country'], values='income',title=' comparison between education and country with respect to income' )
st.plotly_chart(fig8,use_container_width=True)
fig9 = px.sunburst(df, path=['purchase_frequency','education'], values='income',title='comparison between purchase frequency and eduaction with respect to income')
st.plotly_chart(fig9,use_container_width=True)
fig10= px.sunburst(df, path=['purchase_frequency','spending'], values='income',title='comparison between purchase frequency and spending   with respect to income')
st.plotly_chart(fig10,use_container_width=True)
fig11=px.sunburst(df, path=['education','gender'], values='income',title='comparison between education and gender with respect to income')
st.plotly_chart(fig11,use_container_width=True)
fig12=px.sunburst(df, path=['purchase_frequency','gender'], values='income',title='comparison between purchase frequency and gender with respect to income')
st.plotly_chart(fig12,use_container_width=True)
fig13=px.sunburst(df, path=['gender','age'], values='spending',title='comparison between gender and age with respect to income')
st.plotly_chart(fig13,use_container_width=True)
fig14=px.sunburst(df, path=['gender','education'], values='spending',title='comparison between gender and education with respect to income')
st.plotly_chart(fig14,use_container_width=True)
fig15=px.sunburst(df, path=['country','gender'], values='spending',title='comparison between country and gender with respect to income')
st.plotly_chart(fig15,use_container_width=True)
