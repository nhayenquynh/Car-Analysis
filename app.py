import streamlit as st
import pandas as pd
import plotly_express as px

st.title("Sprint 4 Project: Analyzing Car Advertising Dataset")

df =pd.read_csv('/Users/quynhnguyen/Desktop/sprint_4_project/vehicles_us.csv')

st.write(df.head(5))

st.header("Comparing Different Vehicle and Average purchased Price")

car_price = df.groupby('type').agg({'price': 'mean'}).sort_values(by= ['price'], ascending= False).reset_index()
st.write(px.histogram(car_price, y='price', x='type', color='type'))
st.markdown("Bus, truck and pickup cost the most on average. Mini-van, sedan, and hatchback cost less on average. This can be explained by their small size. ")

st.header("Car Revenue per year")
year = df.groupby('model_year').agg({'price': 'sum'}).reset_index()
year1 = year.drop(index = 0) #removing car that doesnt have model_year
st.write(px.scatter(year1, y='model_year', x='price', title= 'Car sales per Year', color='model_year'))
st.markdown('From the scatterplot, most car sales were made around 2018s. Before 2000, it looks like people were using other modes of transporation.')

st.header('How long it takes a car to sell on average with different Conditions')
condition = df.groupby('condition').agg({'days_listed': 'mean'}).reset_index()
st.write(px.histogram(condition, x='condition', y='days_listed', color='condition'))
st.markdown('The average number of days to sell cars, for all condition, is 39 days.')

st.header('Different Cylinders and Its Average Price')
cylinder = df.groupby('cylinders').agg({'price':'mean'}).reset_index()
cylinder1 = cylinder.drop(index=1)
st.write(px.scatter(cylinder1, x='cylinders', y='price', color='cylinders'))
st.markdown('There is an increased in price as the number of cyclinder increases. Except for 0 and 10 cyclinders, these can be considered as outliers.')