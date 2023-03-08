import streamlit as st
import pandas as pd
import plotly_express as px

st.title("Sprint 4 Project: Analyzing Car Advertising Dataset")

st.markdown('Introduction: This project is to analyze a dataset of cars that is collected from 1970s-2010s. I will analyze the most common types of vehicles, how much revenue each year made, and the correlation between the numbers of cyclinder and cost.')

df =pd.read_csv('vehicles_us.csv')

st.write(df.head(5))

st.header("Comparing Different Vehicle and Average purchased Price")

car_price = df.groupby('type').agg({'price': 'mean'}).sort_values(by= ['price'], ascending= False).reset_index()
st.write(px.histogram(car_price, y='price', x='type', color='type'))
st.markdown("Bus, truck and pickup cost the most on average. Mini-van, sedan, and hatchback cost less on average. This can be explained by their small size. ")

st.header("Car Revenue per year")
year = df.groupby('model_year').agg({'price': 'sum'}).reset_index()
year1 = year.drop(index = 0) #removing car that doesnt have model_year
st.write(px.scatter(year1, y='price', x='model_year', title= 'Car sales per Year', color='model_year'))

car_sales_2000s = year1[year1['model_year'] >= 2000.0]
car_sales_1900s = year1[year1['model_year'] <= 2000.0]

if st.checkbox('2000s Revenue'):
    st.write(px.scatter(car_sales_2000s, y='price', x='model_year', title='Cars Revenue in the 2000s', color = "model_year")) 

if st.checkbox('1900s Revenue'):
    st.write(px.scatter(car_sales_1900s, y='price', x='model_year', title='Cars Revenue in the 1900s', color='model_year'))   

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


st.markdown('Conclusion: Analysis of car prices, car sales, how long it took to sell a car, and cyclinders were done. From the first graph, we see that bus, pickup, and truck cost the most, on average. Whereas smaller cars cost less. From graph 2, we see that car sale produce thousands of revenues in 1900s to billions in 2000s. However, there was a drop in car sale in 2019. Another analysis that was made was to see the average days it took to sell cars with different conditions. It takes 39 days, on average, in every condition. Cyclinder cost increases as the number of cyclinder increases, with outlier for 0 and 10 cyclinders.')
