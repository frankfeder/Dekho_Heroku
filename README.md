# Car Dekho - Selling Price Prediction

## Link to Google Slides Presentation:
https://docs.google.com/presentation/d/1_ncOAyJNE6pDFfBaeFreSG21d3WS8ew_Qi82QEE2kSE/edit?usp=sharing

## Link to dashboard (Heroku Link):
https://car-dekho-prediction04.herokuapp.com/

## Project Overview
### Selected topic
This project will use data from Car Dekho, an online vehicle marketplace, to train a machine learning model to predict a car's selling price based on features in the data including vehicle year, mileage, and fuel type.

### Why this topic?
Pricing a car can feel like more of an art than a science when using a naive human estimation approach, so this seems like a perfect opportunity to leverage machine learning. This dataset is also relatively generic in terms of the data provided for each vehicle, making it extendible if later we want to increase the size of the training data by adding records from other online vehicle marketplaces.

### Questions to investigate
What are the most significant factors that determine a car's value? Do cars that use diesel fuel lose value more quickly as vehicle mileage increases?

## Technologies Used

Python, Machine learning, HTML and PostgresSQL


### Data Cleaning and Analysis
Pandas will be used to clean the data. All data manipulation will be performed in Python.

### Machine Learning
SciKit-Learn's linear regression model package and Classification model will be used to create a machine learning model.

### Data Storage
PostgreSQL will be used to host the tables of the database.

### Summary Analysis 

Our Analysis for this segment was based on what are other models that we can use during our prediction. For this time we have decided to use a classification model to predict “price bins” based on each records features instead of linear regression which was initially being used. We are also pursuing K-nearest neighbor and decision tree models.

![Summary_car_sold](https://user-images.githubusercontent.com/74233163/121831740-d1f6ce80-cc8d-11eb-9f0a-9df58d4d1035.png)



