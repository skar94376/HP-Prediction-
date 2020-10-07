from flask import Flask, render_template, request, jsonify
import pickle
import util

app = Flask(__name__) 
# model = pickle.load(open('model.pkl','rb'))

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    return render_template('index.html')

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    sqft = request.form['sqftarea']
    location = request.form['location'] 
    bhk = request.form['BHK']
    bath = request.form['Bath']
    # response = jsonify({'estimated price':util.get_estimated_price(location,sqft,bhk,bath)})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    response = util.get_estimated_price(location,sqft,bhk,bath)
    return render_template('index.html',prediction_text = '    Price is {} lakh.'.format(response))

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)

