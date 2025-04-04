import spacy

# Cargar el modelo de spaCy
nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    # Convertir el texto de entrada a minúsculas
    user_input = user_input.lower()
    
    doc = nlp(user_input)
    #Preguntas bullying ////////////////////////////////////////////////////////
    #Pregunta 1
    if "escuela" in user_input and(
        "acoso" in user_input and
        "broma" in user_input
    ):
        return """
        Si te hacen sentir mal, te insultan, te excluyen o te lastiman y lo hacen varias veces, eso es acoso. No importa si dicen que es "broma", lo que importa es cómo te sientes tú. 🫵
        """
    #Pregunta 2
    elif "bullying" in user_input and(
        "miedo" in user_input and
        "contar" in user_input
    ):
        return """
        Es normal sentir miedo, pero no tienes que enfrentar esto solo. Busca a alguien de confianza, como un maestro, un amigo o alguien de tu familia. Hablarlo es el primer paso para solucionarlo. 🫂        
        """
    #Pregunta 3
    elif "amigos" in user_input and(
        "burla" in user_input and
        "tiempo" in user_input
    ):
        return """
       Si sus bromas te hacen sentir mal y no respetan cuando les dices que paren, entonces no son verdaderos amigos. Rodéate de personas que te respeten y te hagan sentir bien. :)
       """
    
    #Pregunta 4
    elif "defiendo" in user_input and(
        "meterme" in user_input and
        "problemas" in user_input
    ):
        return """
        No necesitas pelear para defenderte. Puedes responder con firmeza, ignorar al agresor y buscar ayuda en un adulto. Lo importante es no quedarte callado. 💪
        """
    
    #Pregunta 5
    elif "acosado" in user_input and(
        "meterme" in user_input and
        "problemas" in user_input
    ):
        return """
        No tienes que enfrentarte al agresor directamente, pero puedes apoyar a la víctima o contarle a un maestro. A veces, solo hacerle saber a esa persona que no está sola ya es una gran ayuda. 🫂✨
        """
    
    #Pregunta 6
    elif "bullying" in user_input and(
        "afectando" in user_input and
        "mucho" in user_input
    ):
        return """
        No es fácil, pero recuerda que lo que dicen de ti no define quién eres 😉. Rodéate de personas que te apoyen y haz actividades que te gusten para fortalecer tu autoestima, como paracticr algún deporte o hacer alguna actividad recreativa. 🏋️
        """
    
    #Pregunta 7
    elif "acoso" in user_input and(
        "maestro" in user_input
    ):
        return """
        Si un maestro te humilla, te ignora o te trata de forma injusta, cuéntaselo a otro adulto de confianza, como el director de la escuela o tus papás. Tienes derecho a ser tratado con respeto. 🫡     
        """

    #Pregunta 8
    elif "denuncio" in user_input and(
        "bullying"  in user_input and
        "situación" in user_input
    ):
        return """
        Al principio puede ser difícil, pero no hacer nada solo permite que siga ocurriendo. Con apoyo de maestros y familia, la situación puede mejorar. 😄
        """

    #Pregunta 9
    elif "ciberacoso" in user_input and(
        "grave" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, y a veces peor, porque las burlas pueden llegar a muchas personas. No tengas miedo de bloquear, denunciar y hablar con alguien si te está afectando.
        """
    
    #Pregunta 10
    elif "escuela" in user_input and(
        "fuerte" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, pero antes de tomar esa decisión, intenta hablar con alguien para buscar soluciones dentro de la escuela. No tienes que huir del problema, hay formas de enfrentarlo con apoyo. 🫶
        """
    
    #Pregunta 11
    elif "personas" in user_input and(
        "hacen" in user_input and
        "bullying"  in user_input
    ):
        return """
        Muchas veces lo hacen porque tienen problemas en casa, quieren sentirse poderosos o simplemente no piensan en el daño que causan. Pero nada de eso justifica su comportamiento. 🤷
        """
    
    #Pregunta 12
    elif "convierto" in user_input and(
        "agresor" in user_input and
        "cuenta" in user_input
    ):
        return """
        Si alguna vez te diste cuenta de que hiciste sentir mal a alguien, aún estás a tiempo de cambiar. Pedir disculpas y tratar a los demás con respeto demuestra madurez. 🤍
        """
    
    #Pregunta 13
    elif "recuperar" in user_input and(
        "confianza" in user_input and
        "bullying"  in user_input
    ):
        return """
        Rodéate de personas que te valoren, recuerda tus cualidades y haz cosas que te hagan sentir bien contigo mismo. No dejes que las palabras de los demás definan quién eres. 🫂
        """
    
    #Pregunta 14
    elif "escuela" in user_input and(
        "ayudarme" in user_input and
        "nada" in user_input
    ):
        return """
        Si la escuela no te escucha, habla con tus papás o con alguna autoridad fuera de la escuela. Nadie tiene derecho a ignorar tu situación. 🙅
        """
    
    #Pregunta 15
    elif "puede" in user_input and(
        "superar" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, con el tiempo y con apoyo, las heridas sanan ❤️‍🩹. Lo más importante es no dejar que el bullying defina tu vida. Tú vales mucho más que las palabras de alguien que no sabe respetar ✨.
        """
    
    #Preguntas drogas////////////////////////////////////////////////////////////////
    #Pregunta 1
    elif "jóvenes" in user_input and(
        "consumir" in user_input and
        "drogas" in user_input
    ):
        return """
        Por curiosidad, por presión de amigos o para olvidar problemas. Al principio parece que "no pasa nada", pero muchas veces se vuelve un problema difícil de controlar. 😕
        """
    
    #Pregunta 2
    elif "pruebo" in user_input and(
        "volverme" in user_input and
        "adicto" in user_input
    ):
        return """
        Depende de la droga y de tu cuerpo, pero algunas pueden engancharte desde la primera vez. Es un riesgo que no vale la pena tomar. 😵‍💫
        """
    
    #Pregunta 3
    elif "amigo" in user_input and(
        "consumir" in user_input and
        "hago" in user_input
    ):
        return """
        No lo juzgues, pero háblale con sinceridad. Dile que te preocupa y que puede contar contigo si necesita ayuda. 🫂
        """
    
    #Pregunta 4
    elif "ofrecen" in user_input and(
        "decir" in user_input and
        "no" in user_input
    ):
        return """
        Un simple "No, gracias" es suficiente. Si alguien insiste, cambia de tema o aléjate. No necesitas probar nada para encajar ‼️.        
        """
    
    #Pregunta 5
    elif "afectan" in user_input and(
        "drogas" in user_input and
        "cerebro" in user_input
    ):
        return """
        Dañan la memoria, la concentración y el autocontrol. A largo plazo pueden afectar tu toma de decisiones y tu capacidad para aprender 🧠.
        """
    
    #Pregunta 6
    elif "drogas" in user_input and(
        "ayudan" in user_input and
        "relajarse" in user_input
    ):
        return """
        Puede parecer que sí en el momento, pero el efecto es temporal. A largo plazo pueden aumentar la ansiedad y la depresión. 🙅
        """
    
    #Pregunta 7
    elif "afecta" in user_input and(
        "drogadicción" in user_input and
        "familia" in user_input
    ):
        return """
        Genera peleas, desconfianza y mucho sufrimiento. No solo afecta a quien consume, sino a todos a su alrededor. ☹️    
        """
    
    #Pregunta 8
    elif "siento" in user_input and(
        "dependiendo" in user_input and
        "sustancia" in user_input
    ):
        return """
        Buscar ayuda es el primer paso. Hablar con un profesional puede hacer una gran diferencia. No tienes que enfrentarlo solo. 😓
        """
    
    #Pregunta 9
    elif "redes" in user_input and(
        "acceso" in user_input and
        "drogas" in user_input
    ):
        return """
        Sí, algunas personas venden drogas en línea. Es importante estar alerta y no dejarse engañar. ‼️
        """
    
    #Pregunta 10
    elif "evitar" in user_input and(
        "presión" in user_input and
        "consumir" in user_input
    ):
        return """
        Rodéate de personas que respeten tus decisiones y confía en ti mismo. No necesitas seguir a los demás para ser aceptado. 🤍
        """
    
    #Pregunta 11
    elif "drogas" in user_input and(
        "más" in user_input and
        "peligrosas" in user_input
    ):
        return """
        Todas pueden serlo, pero algunas como la metanfetamina, la heroína y el fentanilo son extremadamente adictivas y mortales. 💀  
        """
    
    #Pregunta 12
    elif "alcohol" in user_input and(
        "tabaco" in user_input and
        "drogas" in user_input
    ):
        return """
        Sí, a pesar de que su venta es legal, pueden ser igual de adictivos y dañinos que las drogas ilegales. 🍻 🚬 
        """
    
    #Pregunta 13
    elif "ayudar" in user_input and(
        "contra" in user_input and
        "adicción" in user_input
    ):
        return """
        Escúchalo sin juzgar y sugiérele buscar ayuda. Puedes acompañarlo a un especialista o hablar con un adulto de confianza. 🧑‍⚕️
          """
    
    #Pregunta 14
    elif "familia" in user_input and(
        "problemas" in user_input and
        "adicción" in user_input
    ):
        return """
        No es tu responsabilidad resolverlo, pero puedes buscar apoyo en otras personas para ayudarlo. 👬
        """
    
    #Pregunta 15
    elif "puede" in user_input and(
        "salir" in user_input and
        "adicción" in user_input
    ):
        return """
        Sí, con apoyo y tratamiento adecuado, muchas personas logran recuperarse. No es fácil, pero es posible ❤️‍🩹 🫂.
        """
    
    #Preguntas embarazos ///////////////////////////////////////////////////
    #Pregunta 1
    elif "creo" in user_input and(
        "puedo" in user_input and
        "embarazada" in user_input
    ):
        return """
    Lo primero es hacerte una prueba de embarazo para estar segura. Puedes comprar una en la farmacia o acudir a un centro de salud. No entres en pánico, busca apoyo en alguien de confianza ☺️.
    """

    #Pregunta 2
    elif "embarazada" in user_input and(
        "digo" in user_input and
        "papás" in user_input
    ):
        return """
    Sé que puede dar miedo, pero intenta hablar con ellos en un momento tranquilo. Puedes decirles cómo te sientes y que necesitas su apoyo. Es mejor enfrentar la situación con alguien a tu lado. 🫂
    """

    #Pregunta 3
    elif "embarazada" in user_input and(
        "seguir" in user_input and
        "estudiando" in user_input
    ):
        return """
        ¡Sí! La escuela no puede negarte tu derecho a la educación. Puede ser difícil, pero hay programas y apoyos para que continúes con tus estudios 👩‍🎓.
        """
    
    #Pregunta 4
    elif "novio" in user_input and(
        "no quiere" in user_input and
        "condón" in user_input
    ):
        return """
        Protegerse es responsabilidad de ambos. No se trata de confianza, sino de salud. Si realmente te respeta, aceptará usar protección. De lo contrio, reconsidera esa relación ☝️.
        """
    
    #Pregunta 5
    elif "pareja" in user_input and(
        "embarazo" in user_input and
        "mi probelma" in user_input
    ):
        return """
        Eso no es justo. Un embarazo es responsabilidad de ambos. Si él no quiere apoyarte, busca ayuda en tu familia o en personas que realmente se preocupen por ti 🫂.
        """
    
    #Pregunta 6
    elif "riesgos" in user_input and(
        "embarazo" in user_input and
        "adolescente" in user_input
    ):
        return """
        Hay más posibilidades de tener complicaciones en el parto, bebés con bajo peso o problemas de salud. También puede ser un reto emocional y económico. 🤕 💸
        """
    
    #Pregunta 7
    elif "quedar" in user_input and(
        "embarazada" in user_input and
        "primera vez" in user_input
    ):
        return """
        Sí, es un mito que en la primera vez no hay riesgo. Si tienes relaciones sin protección, puedes quedar embarazada sin importar cuántas veces hayas tenido sexo antes. Siempre usa protección ‼️.
        """
    
    #Pregunta 8
    elif "evitar" in user_input and(
        "embarazo" in user_input and
        "no planeado" in user_input
    ):
        return """
        La mejor forma es usando anticonceptivos como el condón, las pastillas o el DIU. También es importante estar bien informado sobre sexualidad. 💊
        """
    
    #Pregunta 9
    elif "menstruación" in user_input and(
        "no puedo" in user_input and
        "embarazada" in user_input
    ):
        return """
        No, aunque el riesgo es menor, aún es posible. Siempre usa protección si no quieres quedar embarazada. ⚠️
        """
    
    #Pregunta 10
    elif "coito interrumpido" in user_input and(
        "funciona" in user_input and
        "anticonceptivo" in user_input
    ):
        return """
        No es un método seguro. Muchas personas quedan embarazadas porque no se dan cuenta de que antes de la eyaculación ya hay espermatozoides en el líquido preseminal. 🤰
        """
    
    #Pregunta 11
    elif "dónde" in user_input and(
        "recibir apoyo" in user_input and
        "embarazada" in user_input
    ):
        return """
        Puedes acudir a un centro de salud, organizaciones de apoyo o hablar con un orientador en tu escuela. No tienes que enfrentar esto sola 🫂 🤍.
        """
    
    #Pregunta 12
    elif "cuánto" in user_input and(
        "cuesta" in user_input and
        "bebé" in user_input
    ):
        return """
        Desde consultas médicas hasta pañales y comida, criar a un bebé puede costar decenas de miles de pesos. Por eso es tan importante planearlo bien antes de tomar la decisión. 💸
        """
    
    #Pregunta 13
    elif "no quiero" in user_input and(
        "tener" in user_input and
        "bebé" in user_input
    ):
        return """
        Es una decisión difícil y personal. Habla con alguien de confianza y conoce todas tus opciones antes de tomar una decisión. ☝️
        """
    
    #Pregunta 14
    elif "afecta" in user_input and(
        "embarazo" in user_input and
        "vida" in user_input
    ):
        return """
        Puede cambiar tu rutina, tu relación con tu familia y tus oportunidades a futuro. Es una gran responsabilidad, por eso es importante tomar decisiones informadas. 👩‍💻
        """
    
    #Pregunta 15
    elif "alguien" in user_input and(
        "presiona" in user_input and
        "relaciones sexuales" in user_input
    ):
        return """
        Nadie tiene derecho a presionarte. Si no te sientes lista, di que no. Tu cuerpo es tuyo y tú decides qué hacer con él 🫶. 
        """
    #SALUD MENTAL EN ADOLESCENTES
    #Pregunta 1
    elif "Últimamente" in user_input and(
        "razón" in user_input and
        "deprimido" in user_input
    ):
        return """
        Sentirse triste a veces es normal, pero si esta sensación dura mucho tiempo y te impide disfrutar tu vida, podrías estar pasando por depresión. No ignores lo que sientes y busca apoyo. 🤍 
        """
    #Pregunta 2
    elif "miedo" in user_input and(
        "papás" in user_input and
        "terapia" in user_input
    ):
        return """
        Puedes explicarles que últimamente no te has sentido bien y que hablar con un profesional podría ayudarte. A veces los papás no lo entienden de inmediato, pero si lo explicas con calma, podrían apoyarte. 👪
        """
    #Pregunta 3
    elif "ansiedad" in user_input and(
        "concentrarme" in user_input and
        "hacer" in user_input
    ):
        return """
        Respirar profundamente, hacer pausas y organizar tu tiempo pueden ayudarte. Si la ansiedad es muy fuerte, hablar con un especialista puede ser una buena idea. 💡
        """
    #Preunta 4
    elif "cuesta" in user_input and(
        "dormir" in user_input and
        "mejorar" in user_input
    ):
        return """
        Evita el celular antes de dormir, trata de relajarte con música suave o respiraciones profundas, y mantén una rutina de sueño regular. 😴
        """
    #Pregunta 5
    elif "ayudo" in user_input and(
        "amigo" in user_input and
        "deprimido" in user_input
    ):
        return """
        Escúchalo sin juzgar, hazle saber que estás ahí para él y anímalo a buscar ayuda si lo necesita. A veces, solo estar presente ya es un gran apoyo. 😄
        """
    #Pregunta 6 
    elif "Siento" in user_input and(
        "nadie" in user_input and
        "entiende" in user_input
    ):
        return """
        Es normal sentirse así a veces, pero no estás solo. Intenta hablar con alguien que realmente te escuche o busca espacios donde puedas expresarte sin miedo. ❤️‍🩹
        """
    #Pregunta 7
    elif "controlar" in user_input and(
        "pensamientos" in user_input and
        "negativos" in user_input
    ):
        return """
        Cuestiona esos pensamientos: ¿Realmente son ciertos? A veces nuestra mente exagera las cosas. También ayuda distraerte con actividades que te gusten. 🏃
        """
    #Pregunta 8
    elif "sentirse" in user_input and(
        "ansioso" in user_input and
        "tiempo" in user_input
    ):
        return """
        No es raro, pero si la ansiedad interfiere con tu vida, es importante buscar formas de manejarla o hablar con alguien que pueda ayudarte.
        """
    #Pregunta 9
    elif "sociales" in user_input and(
        "sentir" in user_input and
        "conmigo" in user_input
    ):
        return """
        Recuerda que en redes, la mayoría solo muestra su mejor versión. Deja de seguir cuentas que te hacen sentir mal y rodéate de contenido positivo. 🙌
        """
    #Pregunta 10
    elif "comparo" in user_input and(
        "inferior" in user_input and
        "autiestima" in user_input
    ):
        return """
        Cada persona tiene su propio camino. En lugar de compararte, concéntrate en tus propias metas y en lo que te hace feliz. ❤️‍🩹
        """
    #Pregunta 11 
    elif "manejar" in user_input and(
        "estrés" in user_input and
        "escolar" in user_input
    ):
        return """
        Organiza tu tiempo, haz pausas y recuerda que no tienes que hacerlo todo perfecto. También ayuda hacer ejercicio o actividades que te relajen. 🤸‍♂️
        """
    #Preguta 12 
    elif "llorar" in user_input and(
        "razón" in user_input and
        "malo" in user_input
    ):
        return """
        No, llorar es una forma natural de liberar emociones. Si sientes que algo te afecta demasiado, hablarlo con alguien puede ayudarte a sentirte mejor. 👥      
        """
    #Pregunta 13
    elif "buscar" in user_input and(
        "ayuda" in user_input and
        "profesional" in user_input
    ):
        return """
        Si sientes que lo que estás pasando afecta tu vida diaria, buscar ayuda es una gran decisión. No tienes que esperar a que la situación sea grave para hacerlo. 
        """
    #Pregunta 14 
    elif "sentirme" in user_input and(
        "mejor" in user_input and
        "conmigo" in user_input
    ):
        return """
        Empieza hablándote con más amabilidad. Todos tenemos cosas buenas y áreas de mejora. Rodéate de personas que te valoren y haz cosas que te hagan sentir bien. 🥰
        """
    #Pregunta 15
    elif "pensamientos" in user_input and(
        "hacerme" in user_input and
        "daño" in user_input
    ):
        return """
        No ignores esos pensamientos. Habla con alguien de confianza lo antes posible. Hay personas que te quieren y quieren ayudarte a salir adelante. No estás solo 🫂      
        """
    
    elif "gracias" in user_input and(
        "por" in user_input and
        "ayuda"
    ):
        return """
        No hay de que agradecer para mi es un gusto ayudarte, espero todo mejore pronto y recuerda que siempre estare aqui cuando necesites ayuda ☺️
        """
    else:
        return """
        Por el momento no tengo información sobre lo que me consultas, pero estamos trabajando para rendir un mejor desempeño espero poder ayudarde pronto ⚙️
        """
    