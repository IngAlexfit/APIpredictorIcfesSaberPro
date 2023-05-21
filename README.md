# APIpredictorIcfesSaberPro
Api Prediccion Pruebas Saber Pro - Algoritmo RandomForest
API de Predicción y Consejos para Estudiantes
Esta API permite predecir si un estudiante tendrá un resultado por encima o por debajo de la media en las pruebas ICFES Saber Pro. Además, utiliza inteligencia artificial para proporcionar consejos personalizados al estudiante de acuerdo con la predicción obtenida.

Funcionamiento
La API consta de dos rutas:

/predict (POST): Esta ruta permite realizar la predicción del puntaje de un estudiante. Los datos de entrada deben enviarse en formato JSON con la siguiente estructura:

```json
{
  "ESTU_PAIS_RESIDE": ["COLOMBIA"],
  "ESTU_DEPTO_RESIDE": ["ATLANTICO"],
  "ESTU_INST_DEPARTAMENTO": ["ATLANTICO"],
  "ESTU_PRGM_ACADEMICO": ["INGENIERIA DE SISTEMAS"],
  "ESTU_METODO_PRGM": ["PRESENCIAL"],
  "ESTU_VALORMATRICULAUNIVERSIDAD": ["Entre 2.5 millones y menos de 4 millones"],
  "ESTU_DEPTO_PRESENTACION": ["BOLIVAR"],
  "ESTU_PAGOMATRICULABECA": ["No"],
  "ESTU_PAGOMATRICULACREDITO": ["No"],
  "ESTU_HORASSEMANATRABAJA": ["Entre 21 y 30 horas"],
  "ESTU_PRIVADO_LIBERTAD": ["N"],
  "ESTU_NACIONALIDAD": ["COLOMBIA"],
  "ESTU_GENERO": ["M"],
  "ESTU_PAGOMATRICULAPADRES": ["Si"],
  "ESTU_PAGOMATRICULAPROPIO": ["No"],
  "FAMI_EDUCACIONPADRE": ["Educación profesional completa"],
  "FAMI_TIENEAUTOMOVIL": ["No"],
  "FAMI_TIENELAVADORA": ["Si"],
  "FAMI_ESTRATOVIVIENDA": ["Estrato 2"],
  "FAMI_TIENECOMPUTADOR": ["Si"],
  "FAMI_TIENEINTERNET": ["Si"],
  "FAMI_EDUCACIONMADRE": ["Técnica o tecnológica completa"],
  "INST_ORIGEN": ["OFICIAL NACIONAL"]
}
```

La API utilizará el modelo Random Forest para realizar la predicción y devolverá un resultado de predicción (0 o 1) en formato JSON.

/predicts_consejos (POST): Esta ruta permite obtener la predicción del puntaje de un estudiante y recibir consejos personalizados utilizando inteligencia artificial. Los datos de entrada deben enviarse en el mismo formato que en el endpoint anterior. Además de la predicción, se devolverá una respuesta de la API de OpenAI con consejos específicos para el estudiante.
