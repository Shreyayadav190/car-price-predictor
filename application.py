#flask, pandas, scikit-learn, pickle-pixin
import pandas as pd
from flask import Flask, render_template

app=Flask(__name__)
car = pd.read_csv(r"C:\Users\SHREYA\Desktop\car price predicter\cleaned car.csv")


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted[car['name'].unique()]
    year = sorted(car['Year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_models=car_models, Years=year, fuel_type=fuel_type)

if __name__=="__main":
    app.run(debug=True) 
    
