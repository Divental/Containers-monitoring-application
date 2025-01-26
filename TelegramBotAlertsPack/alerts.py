import time
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

try:
    from MonitorPack.monitor import get_container_metrics as gcm
except Exception:
    print("Docker isn't working!")

try:
    __API_TOKEN = '7808737665:AAFiu4y69YA8n8u28bvqOdm5E4MhEh342Yc'
    bot = telebot.TeleBot(__API_TOKEN)
except TypeError:
    print("The API-TOKEN hasn't been found!")

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = KeyboardButton("🔍 Help")
    btn2 = KeyboardButton("📊 Status")
    btn3 = KeyboardButton("ℹ️ Clear")
    markup.add(btn1, btn2, btn3)
    return markup

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi! I'm the monitor container telegram bot", reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: message.text == "🔍 Help")
def send_help(message):
    bot.reply_to(message, "Help information: Use /status to get container stats, /clear to clear chat.")

@bot.message_handler(func=lambda message: message.text == "📊 Status")
def sen_containers_stats(message):
    count = 0
    while True:
        try:
            str_list = "\n".join(gcm())
            bot.reply_to(message, str_list)
            count += 1
            if count == 5:
                bot.reply_to(message, "Ви отримали п'ять інформаційних контейнерів")
                break
        except Exception:
            print("Exception:")
            bot.reply_to(message, "Exception:")
            break

@bot.message_handler(func=lambda message: message.text == "ℹ️ Clear")
def clear_chat(message):
    chat_id = message.chat.id
    last_message_id = message.message_id

    for msg_id in range(last_message_id, last_message_id - 100, -1):
        try:
            bot.delete_message(chat_id, msg_id)
            time.sleep(0.1)
        except Exception:
            pass

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# The start telegram bot function
def start_telegram_bot():
    while True:
        try:
            bot.infinity_polling(none_stop=True, timeout=60)
        except Exception:
            print("Exception")
            time.sleep(5)
