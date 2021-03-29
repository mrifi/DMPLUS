from flask import Flask, jsonify, request as req
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
    glucosa = req.form["nEmbarazo"],"pArterial","mmPiel","Peso","altura","edad"]
    print(glucosa)
    #guardar en base de datos
    return "Datos:",glucosa
