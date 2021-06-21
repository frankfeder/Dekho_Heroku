# Route to a webpage with a form
# Post route from the form (Asynchronously called by AJAX)
# Call the machine learning model .predict method on the data that passed from the form
# return Json and python dictionaries (Jsonify)
# AJAX calling function on the webform will update a div id with the results

from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn


app = Flask(__name__)
model = pickle.load(open("./Machine Learning Modeling/dtree_model.sav", 'rb'))
final_prediction = "No prediction yet."

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['YearInput'])
        Km_Driven = int(request.form['KmDrivenInput'])
        Fuel_Type = request.form['FuelTypeInput']

        if(Fuel_Type == 'Petrol'):
            Fuel_Diesel = 0
            Fuel_Other = 0
            Fuel_Petrol = 1
        elif(Fuel_Type == 'Diesel'):
            Fuel_Diesel = 1
            Fuel_Other = 0
            Fuel_Petrol = 0
        else:
            Fuel_Diesel = 0
            Fuel_Other = 1
            Fuel_Petrol = 0
        Seller_Type = request.form['SellerTypeInput']
        if(Seller_Type == 'Individual'):
            Seller_Type_Dealer = 0
            Seller_Type_Individual = 1
            Seller_Type_TrustmarkDealer = 0
        elif(Seller_Type == 'Dealer'):
            Seller_Type_Dealer = 1
            Seller_Type_Individual = 0
            Seller_Type_TrustmarkDealer = 0
        else:
            Seller_Type_Dealer = 0
            Seller_Type_Individual = 0
            Seller_Type_TrustmarkDealer = 1
        Transmission = request.form['TransmissionTypeInput']
        if(Transmission == 'Automatic'):
            Transmission_Automatic = 1
            Transmission_Manual = 0
        else:
            Transmission_Automatic = 0
            Transmission_Manual = 1
        Made_in = request.form['MadeInInput']
        if(Made_in == 'America'):
            Made_in_America = 1
            Made_in_Asia = 0
            Made_in_Europe = 0
            Made_in_India = 0
            Made_in_Unknown = 0
        elif(Made_in == 'Asia'):
            Made_in_America = 0
            Made_in_Asia = 1
            Made_in_Europe = 0
            Made_in_India = 0
            Made_in_Unknown = 0
        elif(Made_in == 'Europe'):
            Made_in_America = 0
            Made_in_Asia = 0
            Made_in_Europe = 1
            Made_in_India = 0
            Made_in_Unknown = 0
        elif(Made_in == 'India'):
            Made_in_America = 0
            Made_in_Asia = 0
            Made_in_Europe = 0
            Made_in_India = 1
            Made_in_Unknown = 0
        else:
            Made_in_America = 0
            Made_in_Asia = 0
            Made_in_Europe = 0
            Made_in_India = 0
            Made_in_Unknown = 1

        to_predict = [[Year, Km_Driven, Fuel_Diesel, Fuel_Other, Fuel_Petrol, Seller_Type_Dealer, Seller_Type_Individual, Seller_Type_TrustmarkDealer,
                                   Transmission_Automatic, Transmission_Manual, Made_in_America, Made_in_Asia, Made_in_Europe, Made_in_India, Made_in_Unknown]]
        prediction = model.predict(to_predict)
        output = prediction

        return render_template('withPredict.html', final_prediction=f"The car can be sold at {output} rupees.")

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)        
