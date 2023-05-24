import openai

openai.api_key = 'PEGAR AQUI APIKEY'

def generar_respuesta(prediccion,respuestas_estudiante):
    prompt=""
    if (prediccion == 0):
        prompt = 'Hola, yo entrené un algoritmo random forest con un dataset de las pruebas icfes saber pro.\n'
        prompt += 'Sucede que este algoritmo lo que predice es si un estudiante, al momento de presentar las pruebas ICFES Saber Pro, va a estar por encima o por debajo de la media.\n'
        prompt += 'El dataset utilizado cuenta con las siguientes columnas:\n'
        prompt += '["ESTU_PAIS_RESIDE"], "ESTU_DEPTO_RESIDE", "ESTU_INST_DEPARTAMENTO", "ESTU_PRGM_ACADEMICO", "ESTU_METODO_PRGM", "ESTU_VALORMATRICULAUNIVERSIDAD", "ESTU_DEPTO_PRESENTACION", "ESTU_PAGOMATRICULABECA", "ESTU_PAGOMATRICULACREDITO", "ESTU_HORASSEMANATRABAJA", "ESTU_PRIVADO_LIBERTAD", "ESTU_NACIONALIDAD", "ESTU_GENERO", "ESTU_PAGOMATRICULAPADRES", "ESTU_PAGOMATRICULAPROPIO", "FAMI_EDUCACIONPADRE", "FAMI_TIENEAUTOMOVIL", "FAMI_TIENELAVADORA", "FAMI_ESTRATOVIVIENDA", "FAMI_TIENECOMPUTADOR", "FAMI_TIENEINTERNET", "FAMI_EDUCACIONMADRE", "INST_ORIGEN".\n\n'
        
        prompt += 'Un estudiante ingresó los siguientes inputs:\n'
        prompt += str(respuestas_estudiante)
        prompt += '\n\n'

        prompt += '.Y el algoritmo le arrojó que su resultado estará por debajo de la media. ¿Qué consejos le darías para que pueda obtener un puntaje por encima de la media? \n\n'
        prompt += 'Teniendo también en cuenta los datos que ingresó, como si cuenta con internet, el estrato, etc. Ya que, por ejemplo, si no posee internet, no le podrías dar recomendaciones dirigidas a usar internet.\n'
        prompt += 'Es por ello que debes analizar cada una de las respuestas que ingresó el estudiante para que los tips sean específicos para él. Responde dirigiéndote a ese estudiante y comienza hablando así:\n\n'
        prompt += '"Hola, no te preocupes."\n\n'

   
    else:
        

        prompt = 'Hola, yo entrené un algoritmo random forest con un dataset de las pruebas icfes saber pro.\n'
        prompt += 'Sucede que este algoritmo lo que predice es si un estudiante, al momento de presentar las pruebas ICFES Saber Pro, va a estar por encima o por debajo de la media.\n'
        prompt += 'El dataset utilizado cuenta con las siguientes columnas:\n'
        prompt += '["ESTU_PAIS_RESIDE"], "ESTU_DEPTO_RESIDE", "ESTU_INST_DEPARTAMENTO", "ESTU_PRGM_ACADEMICO", "ESTU_METODO_PRGM", "ESTU_VALORMATRICULAUNIVERSIDAD", "ESTU_DEPTO_PRESENTACION", "ESTU_PAGOMATRICULABECA", "ESTU_PAGOMATRICULACREDITO", "ESTU_HORASSEMANATRABAJA", "ESTU_PRIVADO_LIBERTAD", "ESTU_NACIONALIDAD", "ESTU_GENERO", "ESTU_PAGOMATRICULAPADRES", "ESTU_PAGOMATRICULAPROPIO", "FAMI_EDUCACIONPADRE", "FAMI_TIENEAUTOMOVIL", "FAMI_TIENELAVADORA", "FAMI_ESTRATOVIVIENDA", "FAMI_TIENECOMPUTADOR", "FAMI_TIENEINTERNET", "FAMI_EDUCACIONMADRE", "INST_ORIGEN".\n\n'
        
        prompt += 'Un estudiante ingresó los siguientes inputs:\n'
        prompt += str(respuestas_estudiante)
        prompt += '\n\n'

        prompt += '. Y el algoritmo le arrojó que su resultado estará por por encima de la media. ¿Qué consejos le darías para que pueda obtener un buen puntaje? \n\n'
        prompt += 'Teniendo también en cuenta los datos que ingresó, como si cuenta con internet, el estrato, etc. Ya que, por ejemplo, si no posee internet, no le podrías dar recomendaciones dirigidas a usar internet.\n'
        prompt += 'Es por ello que debes analizar cada una de las respuestas que ingresó el estudiante para que los tips sean específicos para él. Responde dirigiéndote a ese estudiante y comienza hablando así:\n\n'
        prompt += 'Hola,  tienes altas probabilidades.'

       
        
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