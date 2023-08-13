"""⁡⁣⁣⁢​‌‍‌Restaurant​⁡"""

from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "6518258026:AAHRDCq1XY1FvVhbfiYunETiIRI9hhuvk50"

RANDOM_IMAGE = "You may like these pictures!"
GET_MP3 = "Quiet music! 🎵"
GET_MP4 = "About telegram bot! 😊"
RANDOM_IMAGE_URL = "https://picsum.photos/1200"

#Declare IMAGE_COUNTER as a global variable
global IMAGE_COUNTER
IMAGE_COUNTER = 0

print("Running up the bot...")

# This command is used to register the commands
# that the bot will be able to recognize and execute.
# use_context=True is used to tell the bot to use the new context based callbacks
# instead of the old deprecated ones.

def start(update, context):
    # SENDING HELLO MESSAGE
    # .reply_text(message, reply_markup=None, **kwargs)
    # update.message.reply_text("Hello there! I'm bot. Nice to see you!")
    # ###################################################################
    # SENDING PHOTO
    _send_local_file(update, context)  

def _send_local_file(update, context):
    """
        We must open the file in binary mode,
        otherwise Telegram will not be able to process it correctly
        ------------------------------------------------------------
        RU: Мы должны открыть файл в двоичном режиме,
        иначе Telegram не сможет обработать его правильно
    """
    with open("me.jpg", "rb") as f:
        """
        update.message.reply_photo(photo, caption=None)
        photo  - Photo to send
        caption - Photo caption, 0-1024 characterrs
        """
        update.message.reply_photo(f, caption="Hello! \nWelcome to our restaurant bot! \n/help 👌 \nOur foods!👇👇👇")
    
    with open("food.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 22$")
    with open("food1.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 18$")
    with open("food2.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 11$")
    with open("food3.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 21$")
    with open("food4.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 30$")
    with open("food5.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 7.3$")
    with open("food6.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Cost: 9.1$")


def _send_mp3(update: Update, context: CallbackContext):
    with open("music.mp3", "rb") as f:
        update.message.reply_audio(f, caption="We wish you good mood! 🎧😊")



def _send_mp4(update: Update, context: CallbackContext):
    with open("video.mp4", "rb") as f:
        update.message.reply_video(f, caption="😃😃😃 \nWelcome to our restaurant!!!")

def get_buttons(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton(RANDOM_IMAGE)],
        [KeyboardButton(GET_MP3)],
        [KeyboardButton(GET_MP4)]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose option:",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

def message_handler(update: Update, context: CallbackContext):
    # Use the global keyword to modify IMAGE_COUNTER
    global IMAGE_COUNTER
    IMAGE_COUNTER += 1
    if update.message.text == RANDOM_IMAGE:
        image = get(RANDOM_IMAGE_URL).content
        context.bot.sendMediaGroup(
            chat_id=update.effective_chat.id,
            media=[InputMediaPhoto(image, caption=f"    random {IMAGE_COUNTER} \nDon't like it?😒 \nPress the button again! 😊")]
        )
    elif update.message.text == GET_MP3:
        _send_mp3(update, context)
    elif update.message.text == GET_MP4:
        _send_mp4(update, context)

def help(update, context):
    update.message.reply_text(""""
/start   - Start the bot
/help    - Help
/buttons - Get Optional buttons
"""
                                )

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler('buttons', get_buttons))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()
updater.idle()