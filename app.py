from flask import Flask, request, jsonify
import joblib
import pandas as pd
from IA import generar_respuesta

app = Flask(__name__)

# Carga el modelo y el diccionario de mapeo
rf = joblib.load('modelopruebaforest8.joblib')
mapping_dict = joblib.load('mapping_dictGripPrueba71.joblib')

@app.route('/')
def index():
    return 'Welcome To the API'

@app.route('/predict', methods=['POST'])
def predict():
    # Obtiene los datos de entrada del JSON enviado en la solicitud
    input_data = request.get_json()

    # Mapea los valores categóricos a valores numéricos utilizando el diccionario de mapeo
    input_codes = {}
    for key, value in input_data.items():
        input_codes[key] = [mapping_dict[key][value[0]]]

    # Crea un DataFrame con los datos de entrada codificados
    input_df = pd.DataFrame(input_codes)

    # Realiza la predicción con el modelo
    prediction = rf.predict(input_df)

  
    return jsonify({'prediction': int(prediction[0])})




@app.route('/predict_tips', methods=['POST'])
def predict_tips():
    # Obtiene los datos de entrada del JSON enviado en la solicitud
    input_data = request.get_json()

    # Mapea los valores categóricos a valores numéricos utilizando el diccionario de mapeo
    input_codes = {}
    for key, value in input_data.items():
        input_codes[key] = [mapping_dict[key][value[0]]]

    # Crea un DataFrame con los datos de entrada codificados
    input_df = pd.DataFrame(input_codes)

    # Realiza la predicción con el modelo
    prediction = rf.predict(input_df)

    # LlamaDA A la funcion generar_respuesta que se encuentra en el archivo IA :)
    respuesta_openai = generar_respuesta(int(prediction[0]),input_data)

    #  predicción y la respuesta de GPT :V 
    return jsonify({'prediction': int(prediction[0]), 'respuesta_Api_GPT': respuesta_openai})
    
   


if __name__ == '__main__':
    app.run()