from flask import Flask, render_template, request, redirect
import pickle
from sklearn.ensemble import RandomForestRegressor
from datetime import date

app = Flask(__name__)


def model():
  with open('model_rfr_rscv.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

  return loaded_model


@app.route('/', methods=['GET', 'POST'])
def index():
  m = model()
  # formvalues = {'seller_type': 'dealer',
  #               'transmission': 'automatic',
  #               'fuel_type': 'petrol',
  #               'owners': 0,
  #               'kms_driven': 40000,
  #               'present_price': 40000,
  #               'year': 2014}
  if request.method == 'POST':
    seller_type = request.form['seller-type']
    transmission = request.form['transmission']
    fuel_type = request.form['fuel-type']
    owners = request.form.get('owners')
    kms_driven = request.form.get('kms-driven')
    present_price = request.form.get('present-price')
    year = request.form.get('year')
    formvalues = {'seller_type': seller_type,
                  'transmission': transmission,
                  'fuel_type': fuel_type,
                  'owners': owners,
                  'kms_driven': kms_driven,
                  'present_price': present_price,
                  'year': year}

    years_old = date.today().year - int(year)
    present_price = float(present_price)
    kms_driven = float(kms_driven)
    fuel_type_diesel = 0
    fuel_type_petrol = 0
    if fuel_type == 'diesel':
      fuel_type_diesel = 1
    elif fuel_type == 'petrol':
      fuel_type_petrol = 1

    if seller_type == 'individual':
      seller_type_individual = 1
    else:
      seller_type_individual = 0

    if transmission == 'manual':
      transmission_manual = 1
    else:
      transmission_manual = 0

    # Owner not included in Model -> PLEASE CHANGE MODEL
    test_input = [[years_old, present_price, kms_driven, fuel_type_diesel, fuel_type_petrol, seller_type_individual, transmission_manual]]
    m = model()
    pred = m.predict(test_input)
    return render_template('index.html', formvalues=formvalues, pred=round(pred[0],2))

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
