from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from database import models
from api import main as api_main
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from environment variables
API_TOKEN = os.getenv("API_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to the Video Reminder Bot! Use /help to see available commands.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "/add_topic <topic> - Add a new topic\n"
        "/set_importance <video_id> <level> - Set importance level for a video\n"
        "/remind_me <video_id> - Set a reminder for a video\n"
        "/list_topics - List all saved topics\n"
    )
    await update.message.reply_text(help_text)

def main() -> None:
    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # Add more handlers as needed

    application.run_polling()

if __name__ == '__main__':
    main()