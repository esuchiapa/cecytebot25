from telegram import Update
from telegram.ext import CallbackContext
from src.nlp.responses import generate_response
import random


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('¡Hola! Soy Cecy, ¿Cómo te puedo ayudar hoy?, recuerda que puedes preguntar por temas sobre bullying, acoso, etc')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Puedes hablar conmigo sobre bullying, embarazos adolescentes, drogas o tu salud mental ¿tienes alguna duda al respecto?')


async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()  # Convertir el texto a minúsculas
    
    if text == "salir":
        await update.message.reply_text('¡Adiós! Espero haberte ayudado. Para volver a hablar conmigo, escribe /hola.')
        # Detener el bot
        context.application.stop()
    else:
        response = generate_response(text)
        await update.message.reply_text(response)
 