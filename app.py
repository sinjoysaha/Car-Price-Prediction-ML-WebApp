from flask import Flask, render_template, request, redirect
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

def model():
    with open('model_rfr_rscv.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    return loaded_model

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        seller_type = request.form['seller-type']
        transmission = request.form['transmission']
        fuel_type = request.form['fuel-type']
        owner = request.form.get('owners')
        kms_driven = request.form.get('kms-driven')
        present_price = request.form.get('present-price')
        year = request.form.get('year')
        formvalues = {'seller_type':seller_type,
                      'transmission':transmission,
                      'fuel_type':fuel_type,
                      'owner':owner,
                      'kms_driven':kms_driven,
                      'present_price':present_price,
                      'year':year}
        return render_template('index.html', formvalues=formvalues)

    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
