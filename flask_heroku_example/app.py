#%%
from flask import Flask, render_template
# import myMachineLearningModel
#%%
app = Flask(__name__)
#%%
@app.route("/")
def home():
    return render_template('index.html')

#Route to a webpage with a form

#Post route from the form (Asynchronously called by AJAX)
# Call the machine learning model .predict method on the data that passed from the form
# return Json and python dictionaries (Jsonify)
# AJAX calling function on the webform will update a div id with the results
