import time
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

try:
    from MonitorPack.monitor import get_container_metrics as gcm
except Exception as e:
    print("Docker isn't working!", str(e))

try:
    API_TOKEN = "7808737665:AAFiu4y69YA8n8u28bvqOdm5E4MhEh342Yc"
    if not API_TOKEN:
        raise ValueError("The API-TOKEN hasn't been found!")
    bot = telebot.TeleBot(API_TOKEN)
except ValueError:
    print("The API-TOKEN hasn't been found!")

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = KeyboardButton("🔍 Help")
    btn2 = KeyboardButton("📊 Status")
    btn3 = KeyboardButton("ℹ️ Clear")
    markup.add(btn1, btn2, btn3)
    return markup

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi! I'm the monitor container telegram bot", reply_markup=main_keyboard())

# Handle '/help'
@bot.message_handler(func=lambda message: message.text == "🔍 Help")
def send_help(message):
    bot.reply_to(message, "Help information: Use Status to get container stats, Clear to clear chat.")

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
            print("The docker is not running now!", str(exc))
            bot.reply_to(message, "The docker is not running now!")
            break

# Handle '/clear'
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
        except Exception as exc:
            print("The docker is not running now!", str(exc))
            time.sleep(5)


