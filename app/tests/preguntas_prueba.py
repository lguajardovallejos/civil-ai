preguntas_prueba = [
    # Preguntas directas
    {
        "pregunta": "¿Cuál es el espesor mínimo de losa para un edificio de 5 pisos según la NCh433?",
        "tipo": "directa",
        "respuesta_esperada": "Según la NCh433 - 2012, el espesor mínimo de losa para edificios de 5 pisos debe ser de 15 cm."
    },
    {
        "pregunta": "¿Qué establece la NCh2369 sobre el diseño sísmico de estructuras?",
        "tipo": "directa",
        "respuesta_esperada": "La NCh2369 - 2003 establece los requisitos para el diseño sísmico de estructuras, incluyendo los coeficientes de modificación de respuesta y los factores de reducción de resistencia."
    },
    {
        "pregunta": "¿Cuáles son los requisitos de resistencia al fuego según la NCh430?",
        "tipo": "directa",
        "respuesta_esperada": "La NCh430 - 2015 establece que los elementos estructurales deben tener una resistencia al fuego mínima de 60 minutos para edificios de hasta 4 pisos."
    },
    {
        "pregunta": "¿Qué especifica la NCh2123 sobre el diseño de fundaciones?",
        "tipo": "directa",
        "respuesta_esperada": "La NCh2123 - 2018 especifica los requisitos para el diseño de fundaciones, incluyendo la capacidad portante del suelo y los asentamientos permisibles."
    },
    {
        "pregunta": "¿Cuál es el factor de seguridad mínimo para el diseño de muros de contención según la NCh1537?",
        "tipo": "directa",
        "respuesta_esperada": "La NCh1537 - 2009 establece un factor de seguridad mínimo de 1.5 para el diseño de muros de contención."
    },

    # Preguntas comparativas
    {
        "pregunta": "¿Cuál es la diferencia en los requisitos de resistencia al fuego entre la NCh430 y la NCh2369?",
        "tipo": "comparativa",
        "respuesta_esperada": "La NCh430 - 2015 se enfoca en la resistencia al fuego de elementos estructurales, mientras que la NCh2369 - 2003 aborda el diseño sísmico general. La NCh430 requiere 60 minutos de resistencia para edificios de hasta 4 pisos, mientras que la NCh2369 no especifica tiempos de resistencia al fuego."
    },
    {
        "pregunta": "¿Cómo se comparan los requisitos de diseño sísmico entre la NCh433 y la NCh2369?",
        "tipo": "comparativa",
        "respuesta_esperada": "La NCh433 - 2012 y la NCh2369 - 2003 tienen enfoques complementarios. La NCh433 establece los requisitos generales de diseño sísmico, mientras que la NCh2369 proporciona coeficientes específicos de modificación de respuesta."
    },
    {
        "pregunta": "¿Qué diferencias hay en los requisitos de fundaciones entre la NCh2123 y la NCh1537?",
        "tipo": "comparativa",
        "respuesta_esperada": "La NCh2123 - 2018 se enfoca en el diseño general de fundaciones, mientras que la NCh1537 - 2009 se centra específicamente en muros de contención y sus fundaciones."
    },
    {
        "pregunta": "¿Cómo varían los requisitos de resistencia al fuego según el tipo de estructura en la NCh430?",
        "tipo": "comparativa",
        "respuesta_esperada": "La NCh430 - 2015 establece diferentes requisitos de resistencia al fuego según el tipo de estructura: 60 minutos para estructuras de hormigón armado de hasta 4 pisos, y 90 minutos para estructuras de acero."
    },
    {
        "pregunta": "¿Qué diferencias hay en los factores de seguridad entre la NCh2123 y la NCh1537?",
        "tipo": "comparativa",
        "respuesta_esperada": "La NCh2123 - 2018 establece un factor de seguridad de 2.0 para fundaciones, mientras que la NCh1537 - 2009 requiere 1.5 para muros de contención."
    },

    # Preguntas de inferencia
    {
        "pregunta": "¿Qué implicaciones tiene un factor de seguridad de 1.5 en muros de contención sobre el diseño de fundaciones?",
        "tipo": "inferencia",
        "respuesta_esperada": "Según la NCh1537 - 2009 y la NCh2123 - 2018, un factor de seguridad de 1.5 en muros de contención implica que las fundaciones deben diseñarse para soportar cargas incrementadas en un 50% sobre las cargas de servicio."
    },
    {
        "pregunta": "¿Cómo afecta la resistencia al fuego de 60 minutos a la selección de materiales según la NCh430?",
        "tipo": "inferencia",
        "respuesta_esperada": "La NCh430 - 2015 implica que los materiales seleccionados deben mantener su resistencia estructural durante al menos 60 minutos bajo condiciones de incendio, lo que afecta la selección de recubrimientos y protecciones."
    },
    {
        "pregunta": "¿Qué se puede inferir sobre la importancia de la capacidad portante del suelo según la NCh2123?",
        "tipo": "inferencia",
        "respuesta_esperada": "La NCh2123 - 2018 sugiere que la capacidad portante del suelo es un factor crítico que determina el tipo y dimensiones de las fundaciones, ya que establece requisitos específicos para su evaluación."
    },
    {
        "pregunta": "¿Qué implicaciones tiene el diseño sísmico de la NCh433 sobre la selección de sistemas estructurales?",
        "tipo": "inferencia",
        "respuesta_esperada": "La NCh433 - 2012 implica que los sistemas estructurales deben seleccionarse considerando su comportamiento sísmico, ductilidad y capacidad de disipación de energía."
    },
    {
        "pregunta": "¿Cómo afecta la NCh2369 a la distribución de rigidez en un edificio?",
        "tipo": "inferencia",
        "respuesta_esperada": "La NCh2369 - 2003 sugiere que la distribución de rigidez debe ser uniforme para evitar concentraciones de esfuerzos y asegurar un comportamiento sísmico adecuado."
    },

    # Preguntas de aplicación
    {
        "pregunta": "Para un edificio de 8 pisos en zona sísmica, ¿qué normativas aplican y qué requisitos específicos debe cumplir?",
        "tipo": "aplicación",
        "respuesta_esperada": "Según la NCh433 - 2012 y NCh2369 - 2003, el edificio debe cumplir con requisitos de diseño sísmico, incluyendo coeficientes de modificación de respuesta y factores de reducción de resistencia. Además, según la NCh430 - 2015, debe tener una resistencia al fuego de 90 minutos."
    },
    {
        "pregunta": "En un proyecto de muro de contención de 6 metros de altura, ¿qué normativas y requisitos específicos aplican?",
        "tipo": "aplicación",
        "respuesta_esperada": "Según la NCh1537 - 2009, el muro debe diseñarse con un factor de seguridad mínimo de 1.5 y considerar la estabilidad global. La NCh2123 - 2018 aplica para el diseño de la fundación."
    },
    {
        "pregunta": "Para una estructura de acero en zona costera, ¿qué normativas y requisitos específicos aplican?",
        "tipo": "aplicación",
        "respuesta_esperada": "La NCh2369 - 2003 establece los requisitos de diseño sísmico, la NCh430 - 2015 especifica la resistencia al fuego de 90 minutos, y se deben considerar requisitos adicionales para protección contra corrosión en ambiente marino."
    },
    {
        "pregunta": "En un proyecto de fundación sobre suelo blando, ¿qué normativas y requisitos específicos aplican?",
        "tipo": "aplicación",
        "respuesta_esperada": "La NCh2123 - 2018 establece los requisitos para el diseño de fundaciones, incluyendo la evaluación de la capacidad portante y los asentamientos permisibles. Se debe considerar un factor de seguridad de 2.0."
    },
    {
        "pregunta": "Para un edificio de 3 pisos con uso comercial, ¿qué normativas y requisitos específicos aplican?",
        "tipo": "aplicación",
        "respuesta_esperada": "Según la NCh433 - 2012 y NCh2369 - 2003, debe cumplir con requisitos de diseño sísmico. La NCh430 - 2015 establece una resistencia al fuego de 60 minutos para elementos estructurales."
    }
] 