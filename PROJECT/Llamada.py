from flask import Flask, jsonify, request as req
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from Ubicacion_csv import Ubicacion_csv


app = Flask(__name__)

@app.route('/')
def helloworld():
    return '¡Hola mundo 3!'

@app.route('/saludar/<nombre>', methods=['GET'])
def saludar(nombre):
    return "Hola " + nombre

@app.route('/saludar/json/<nombre>', methods=['GET'])
def saludar_json(nombre):
    return jsonify({"nombre": nombre})


@app.route('/saludar/', methods=['GET'])
def saludarConParametro():
    nombre = req.args.get('nombre')
    return jsonify({"nombre": nombre})

@app.route('/pronostico/', methods=['POST'])
def guardarDatos():
    nEmbarazo = int(req.form["nEmbarazo"])
    pArterial = int(req.form["pArterial"])
    mmPiel =    int(req.form["mmPiel"])
    peso =      int(req.form["peso"])
    altura =    int(req.form["altura"])
    edad =      int(req.form["edad"])
    insulina =  int(req.form["insulina"])
    
    ###Importar CSV
    file_path = str(Ubicacion_csv())
    df = pd.read_csv(file_path)
    X = df[['Pregnancies','BloodPressure','SkinThickness','BMI','Insulin','Age']]
    y = df['Glucose']
    X = sm.add_constant(X)
    est = sm.OLS(y, X).fit()
    params = []
    for param in est.params:
        params.append(param)
    bmi = (peso/((altura/100)**2))
    pronostico = (nEmbarazo*params[1])+(pArterial*params[2])+(mmPiel*params[3])+(bmi*params[4])+(insulina*params[5])+(edad*params[6])+params[0]
    ##Agregar fórmula de regresión multivariable
    print(pronostico)
    return str(int(pronostico))+"(mg/dl)"


