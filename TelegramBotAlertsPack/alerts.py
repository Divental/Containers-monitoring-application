import sys
import LoggerPack.log_container as lc
from dotenv import load_dotenv
import os
import time
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

if __name__ == "__main__":
    lc.logger.error("This file cannot be run as main!")
    print("\nThis file cannot be run as main!")
    sys.exit()

try:
    from MonitorPack.monitor import get_container_metrics as gcm
except FileNotFoundError as exc:
    lc.logger.error("Docker isn't working!")
    print("Docker isn't working!")

# Load environment variables from the .env file
try:
    load_dotenv()
except NameError as ne:
    lc.logger.error("Unable to load the environment!")
    print("Unable to load the environment!")


try:
    API_TOKEN = os.getenv("API_TOKEN")
    if not API_TOKEN:
        raise ValueError
    bot = telebot.TeleBot(API_TOKEN)
except ValueError as ve:
    lc.logger.error("The API-TOKEN hasn't been found!")
    print("The API-TOKEN hasn't been found!")

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = KeyboardButton("🔍 Help")
    btn2 = KeyboardButton("📊 Status")
    btn3 = KeyboardButton("ℹ️ Clear")
    markup.add(btn1, btn2, btn3)
    return markup

# Handle '/start'
@bot.message_handler(commands=['start']) # The ‘bot’ highlighting occurs due to the possible failure to launch the bot when checking in the try/except block ^^^
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi! I'm the monitor container telegram bot", reply_markup=main_keyboard())

# Handle '/help'
@bot.message_handler(func=lambda message: message.text == "🔍 Help")
def send_help(message):
    bot.reply_to(message, "Help information: Use Status to get container stats, Clear to clear chat.")

@bot.message_handler(commands=['help'])
def send_help_instruction(message):
    send_help(message)

# Handle '/status'
@bot.message_handler(func=lambda message: message.text == "📊 Status")
def sen_containers_stats(message):
    count = 0
    while True:
        try:
            container_stats_text = "\n".join(gcm())
            bot.reply_to(message, container_stats_text)
            count += 1
            if count == 5:
                bot.reply_to(message, "You have received five information containers")
                break
        except Exception as exc:
            lc.logger.error("The containers is not running now!")
            bot.reply_to(message, "The docker containers is not running now!")
            break

@bot.message_handler(commands=['status'])
def send_status_instruction(message):
    sen_containers_stats(message)

# Handle '/clear'
@bot.message_handler(func=lambda message: message.text == "ℹ️ Clear")
def clear_chat(message):
    chat_id = message.chat.id
    last_message_id = message.message_id

    for msg_id in range(last_message_id, last_message_id - 100, -1):
        try:
            bot.delete_message(chat_id, msg_id)
            time.sleep(0.1)
        except Exception as exc:
            pass

@bot.message_handler(commands=['clear'])
def send_clear_instruction(message):
    clear_chat(message)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# The start telegram bot function
def start_telegram_bot():
    # while True:
        try:
            bot.infinity_polling(none_stop=True, timeout=60)
        except Exception as exc:
            lc.logger.error("The telegram bot is not running now!")
            print("The telegram bot is not running now!")
            time.sleep(5)


