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
    m = model()
    m = str(m.best_params_)
    return render_template('index.html', model=m)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
