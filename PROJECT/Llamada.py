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

@app.route('/guardar/', methods=['POST'])
def guardarDatos():
    nEmbarazo = req.form["nEmbarazo"],
    pArterial =req.form["pArterial"],
    mmPiel = req.form["mmPiel"],
    peso = req.form["peso"],
    altura = req.form["altura"],
    edad = req.form["edad"],
    insulina = req.form["insulina"]

    nEmbarazo = int(nEmbarazo[0]),
    pArterial =int(pArterial[0]),
    mmPiel =int(mmPiel[0]),
    peso = int(peso[0]),
    altura = int(altura[0]),
    edad = int(edad[0]),
    insulina = int(insulina[0])

    ###Importar CSV
    file_path = str(Ubicacion_csv())
    df = pd.read_csv(file_path)
    X = df[['Pregnancies','BloodPressure','SkinThickness','BMI','Insulin','Age']]
    y = df['Glucose']
    X = sm.add_constant(X)
    est = sm.OLS(y, X).fit()
    print(est.summary())
    params = []
    for param in est.params:
        params.append(param)
        print(param)
    bmi = (peso/((altura/100)**2))
    pronostico = (nEmbarazo*params[1])+(pArterial*params[2])+(mmPiel*params[3])+(bmi*params[4])+(insulina*params[5])+(edad*params[6])+params[0]
    ##Agregar fórmula de regresión multivariable
    print(pronostico)
    return str(pronostico)


