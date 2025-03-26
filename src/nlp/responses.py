import spacy

# Cargar el modelo de spaCy
nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    # Convertir el texto de entrada a minúsculas
    user_input = user_input.lower()
    
    doc = nlp(user_input)
    if "escuela" in user_input and(
        ("acoso" or "bullying") in user_input and
        "broma" in user_input
    ):
        return """
        Si te hacen sentir mal, te insultan, te excluyen o te lastiman y lo hacen varias veces, eso es acoso. No importa si dicen que es "broma", lo que importa es cómo te sientes tú.
        """
    
    elif ("bullying" or "acoso") in user_input and(
        "miedo" in user_input and
        "contar" in user_input
    ):
        return """
        Es normal sentir miedo, pero no tienes que enfrentar esto solo. Busca a alguien de confianza, como un maestro, un amigo o alguien de tu familia. Hablarlo es el primer paso para solucionarlo. 🫂        
        """
    
    elif "amigos" in user_input and(
        "burla" in user_input and
        "tiempo" in user_input
    ):
        return """
       Si sus bromas te hacen sentir mal y no respetan cuando les dices que paren, entonces no son verdaderos amigos. Rodéate de personas que te respeten y te hagan sentir bien. :)
       """
    
    elif "defiendo" in user_input and(
        "meterme" in user_input and
        "problemas" in user_input
    ):
        return """
        No necesitas pelear para defenderte. Puedes responder con firmeza, ignorar al agresor y buscar ayuda en un adulto. Lo importante es no quedarte callado. 💪
        """
    
    elif "acosado" in user_input and(
        "meterme" in user_input and
        "problemas" in user_input
    ):
        return """
        No tienes que enfrentarte al agresor directamente, pero puedes apoyar a la víctima o contarle a un maestro. A veces, solo hacerle saber a esa persona que no está sola ya es una gran ayuda.
        """
    
    elif ("bullying" or "acoso") in user_input and(
        "afectando" in user_input and
        "mucho" in user_input
    ):
        return """
        No es fácil, pero recuerda que lo que dicen de ti no define quién eres 😉. Rodéate de personas que te apoyen y haz actividades que te gusten para fortalecer tu autoestima, como paracticr algún deporte o hacer alguna actividad recreativa.
        """
    
    elif ("acoso" or "bullying") in user_input and(
        "maestro" in user_input
    ):
        return """
        Si un maestro te humilla, te ignora o te trata de forma injusta, cuéntaselo a otro adulto de confianza, como el director de la escuela o tus papás. Tienes derecho a ser tratado con respeto.      
        """

    elif "denuncio" in user_input and(
        "bullying"  in user_input and
        "situación" in user_input
    ):
        return """
        Al principio puede ser difícil, pero no hacer nada solo permite que siga ocurriendo. Con apoyo de maestros y familia, la situación puede mejorar. 😄
        """

    elif "ciberacoso" in user_input and(
        "grave" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, y a veces peor, porque las burlas pueden llegar a muchas personas. No tengas miedo de bloquear, denunciar y hablar con alguien si te está afectando.
        """

    elif "escuela" in user_input and(
        "fuerte" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, pero antes de tomar esa decisión, intenta hablar con alguien para buscar soluciones dentro de la escuela. No tienes que huir del problema, hay formas de enfrentarlo con apoyo. 🫶
        """
    
    elif "personas" in user_input and(
        "hacen" in user_input and
        "bullying"  in user_input
    ):
        return """
        Muchas veces lo hacen porque tienen problemas en casa, quieren sentirse poderosos o simplemente no piensan en el daño que causan. Pero nada de eso justifica su comportamiento.
        """
    
    elif "convierto" in user_input and(
        "agresor" in user_input and
        "cuenta" in user_input
    ):
        return """
        Si alguna vez te diste cuenta de que hiciste sentir mal a alguien, aún estás a tiempo de cambiar. Pedir disculpas y tratar a los demás con respeto demuestra madurez. 🤍
        """
    

    elif "recuperar" in user_input and(
        "confianza" in user_input and
        "bullying"  in user_input
    ):
        return """
        Rodéate de personas que te valoren, recuerda tus cualidades y haz cosas que te hagan sentir bien contigo mismo. No dejes que las palabras de los demás definan quién eres. 🫂
        """
    
    elif "escuela" in user_input and(
        "ayudarme" in user_input and
        "nada" in user_input
    ):
        return """
        Si la escuela no te escucha, habla con tus papás o con alguna autoridad fuera de la escuela. Nadie tiene derecho a ignorar tu situación.
        """
    
    elif "puede" in user_input and(
        "superar" in user_input and
        "bullying" in user_input
    ):
        return """
        Sí, con el tiempo y con apoyo, las heridas sanan ❤️‍🩹. Lo más importante es no dejar que el bullying defina tu vida. Tú vales mucho más que las palabras de alguien que no sabe respetar
        """
    else:
        return """si"""
