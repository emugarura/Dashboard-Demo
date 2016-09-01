from flask import Flask
from flask import render_template
import json
import pandas as pd

app = Flask(__name__)

data_path = './static/data'

@app.route("/")
def index():
    return render_template("index.html")
    # return "Hello world!"

@app.route('/data')
def get_data():
    with open(data_path + '/yelp_test_set_business.json') as data_file:    
        business_data = pd.read_json(data_file)
    return business_data.to_json(orient='records')


if __name__ == "__main__":
    app.run(port=5000,debug=True)