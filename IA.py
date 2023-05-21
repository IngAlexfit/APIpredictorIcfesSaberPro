import openai

openai.api_key = 'PEGAR AQUI APIKEY'

def generar_respuesta(prediccion):
    prompt=""
    if (prediccion == 0):
        prompt = """Hola, yo entrené un algoritmo random forest con un dataset con la siguiente estructura:
        {
            "ESTU_PAIS_RESIDE":["COLOMBIA"],
            "ESTU_DEPTO_RESIDE":["ATLANTICO"],
            "ESTU_INST_DEPARTAMENTO":["ATLANTICO"],
            "ESTU_PRGM_ACADEMICO":["INGENIERIA DE SISTEMAS"],
            "ESTU_METODO_PRGM":["PRESENCIAL"],
            "ESTU_VALORMATRICULAUNIVERSIDAD":["Entre 2.5 millones y menos de 4 millones"],
            "ESTU_DEPTO_PRESENTACION":["BOLIVAR"],
            "ESTU_PAGOMATRICULABECA":["No"],
            "ESTU_PAGOMATRICULACREDITO":["No"],
            "ESTU_HORASSEMANATRABAJA":["Entre 21 y 30 horas"],
            "ESTU_PRIVADO_LIBERTAD":["N"],
            "ESTU_NACIONALIDAD":["COLOMBIA"],
            "ESTU_GENERO":["M"],
            "ESTU_PAGOMATRICULAPADRES":["Si"],
            "ESTU_PAGOMATRICULAPROPIO":["No"],
            "FAMI_EDUCACIONPADRE":["Educación profesional completa"],
            "FAMI_TIENEAUTOMOVIL":["No"],
            "FAMI_TIENELAVADORA":["Si"],
            "FAMI_ESTRATOVIVIENDA":["Estrato 2"],
            "FAMI_TIENECOMPUTADOR":["Si"],
            "FAMI_TIENEINTERNET":["Si"],
            "FAMI_EDUCACIONMADRE":["Técnica o tecnológica completa"],
            "INST_ORIGEN":["OFICIAL NACIONAL"]
        } 
        Sucede que este algoritmo lo que predice es si un estudiante, al momento de presentar las pruebas ICFES Saber Pro, va a estar por encima o por debajo de la media.

        En el caso de que este estudiante le aparezca que su resultado estará por debajo de la media, ¿qué consejos le darías para que pueda obtener un puntaje por encima de la media, teniendo también en cuenta la estructura del dataset utilizado? Responde dirigiéndote a ese estudiante y comienza hablando así:

        "Hola, no te preocupes."""
    else:
        prompt = """Hola, yo entrene un algoritmo random forest con un dataset con la siguiente estructura:
        {
            "ESTU_PAIS_RESIDE":["COLOMBIA"],
            "ESTU_DEPTO_RESIDE":["ATLANTICO"],
            "ESTU_INST_DEPARTAMENTO":["ATLANTICO"],
            "ESTU_PRGM_ACADEMICO":["INGENIERIA DE SISTEMAS"],
            "ESTU_METODO_PRGM":["PRESENCIAL"],
            "ESTU_VALORMATRICULAUNIVERSIDAD":["Entre 2.5 millones y menos de 4 millones"],
            "ESTU_DEPTO_PRESENTACION":["BOLIVAR"],
            "ESTU_PAGOMATRICULABECA":["No"],
            "ESTU_PAGOMATRICULACREDITO":["No"],
            "ESTU_HORASSEMANATRABAJA":["Entre 21 y 30 horas"],
            "ESTU_PRIVADO_LIBERTAD":["N"],
            "ESTU_NACIONALIDAD":["COLOMBIA"],
            "ESTU_GENERO":["M"],
            "ESTU_PAGOMATRICULAPADRES":["Si"],
            "ESTU_PAGOMATRICULAPROPIO":["No"],
            "FAMI_EDUCACIONPADRE":["Educación profesional completa"],
            "FAMI_TIENEAUTOMOVIL":["No"],
            "FAMI_TIENELAVADORA":["Si"],
            "FAMI_ESTRATOVIVIENDA":["Estrato 2"],
            "FAMI_TIENECOMPUTADOR":["Si"],
            "FAMI_TIENEINTERNET":["Si"],
            "FAMI_EDUCACIONMADRE":["Técnica o tecnológica completa"],
            "INST_ORIGEN":["OFICIAL NACIONAL"]
        } 
        sucede que este algoritmo lo que predice es si un estudiante al momento de presentar las pruebas icfes saber pro va a estar por encima o por debajo de la media.


        en el caso de que este estudiante le aparezca que su resultado estara por encima de la media, que consejos le darias para que  pueda obtener un buen puntaje.
        Responde dirigiendote a ese estudiante. y comienza hablando asi:
        Hola,  tienes altas probabilidades."""

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=350,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    respuesta = response.choices[0].text.strip()
    return respuesta