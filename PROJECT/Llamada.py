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
    
    nEmbarazoD = nEmbarazo[0],
    pArterialD =pArterial[0],
    mmPielD =mmPiel[0],
    pesoD = peso[0],
    alturaD = altura[0],
    edadD = edad[0],
    insulinaD = insulina[0]
    
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

    print("**********ESTOY AQUI")
    print(type((3,4,5)))
    #print(type(peso),str(peso[0]))
    print(type(alturaD),alturaD[0])
    nEmbarazoDato = float(nEmbarazoD[0]),
    pArterialDato = float(pArterialD[0]),
    mmPielDato =    float(mmPielD[0]),
    pesoDato =      float(pesoD[0]),
    alturaDato =    float(alturaD[0]),
    edadDato =      float(edadD[0]),
    insulinaDato =  float(insulinaD[0])
    print(params)
    bmi = (pesoDato[0]/((alturaDato[0]/100)**2))
    print(type(nEmbarazoDato[0]),nEmbarazoDato)
    print(nEmbarazoDato[0]*params[1])
    print(pArterialDato[0]*params[2])
    print(mmPielDato[0]*params[3])
    print(bmi*params[4])
    print(insulinaDato*params[5])
    print(edadDato[0]*params[6])
    print(params[0])
    pronostico = (nEmbarazoDato[0]*params[1])+(pArterialDato[0]*params[2])+(mmPielDato[0]*params[3])+(bmi*params[4])+(insulinaDato*params[5])+(edadDato[0]*params[6])+params[0]
    ##Agregar fórmula de regresión multivariable
    print(pronostico)
    return str(int(pronostico))+"(mg/dl)"


