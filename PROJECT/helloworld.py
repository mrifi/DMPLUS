from flask import Flask, jsonify, request as req
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler


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
    edad = req.form["edad"]
    ###Importar CSV
    df = pd.read_csv('C:\\Users\\Matí\\Desktop\\DMPLUS\\PROJECT\\diabetes.csv')
    X = df[['Pregnancies','BloodPressure','SkinThickness','BMI','Insulin','Age']]
    y = df['Glucose']
    X = sm.add_constant(X)
    est = sm.OLS(y, X).fit()
    print(est.summary())
    params = []
    for param in est.params:
        params.append(param)
        print(param)
    return str((nEmbarazo,pArterial,mmPiel,peso,altura,edad))


