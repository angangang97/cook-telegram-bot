import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with an inline keyboard when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("SWIPE to Earn", web_app=WebAppInfo(url="https://ctsmesh-web.fly.dev/dashboard/facemesh"))],
        [InlineKeyboardButton("What's cooking? (Read Alpha)", url='https://ctsmesh-web.fly.dev/dashboard/kanban')],
        [InlineKeyboardButton("Learn More", url='https://dorahacks.io/buidl/16797/')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Replace with your actual image URL
    image_url = 'https://github.com/Purifiedhuman/ctsmesh-web/blob/master-norman-test/public/static/sample_cook.jpeg?raw=true'
    
    caption = "Let's COOK 🍳 Discover crypto alpha easily. Or swipe left/right to help degens navigate through the noise. 🔥🔥"

    await update.message.reply_photo(photo=image_url, caption=caption, reply_markup=reply_markup)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token("7902806278:AAHUTAeXzef0mIoDQeV8JVfxAI-gJ8j_X0g").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()