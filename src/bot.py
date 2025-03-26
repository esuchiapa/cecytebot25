from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.config.config import TELEGRAM_BOT_TOKEN
from src.handlers import start, help_command, handle_message

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("iniciar", start))
    app.add_handler(CommandHandler("comenzar", start))
    app.add_handler(CommandHandler("hola", start))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == '__main__':
    main()
