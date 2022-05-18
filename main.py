import telebot

bot = telebot.TeleBot("5386042733:AAHD-WrHTfR3_GFACToO3_kfJoPJctqX6SY")
user_data = {}

class User:
    def __init__(self, fname):
        self.fname = fname
        self.lname = ''


@bot.message_handler(commands=['start', 'help'])
def send_name(message):
    msg = bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(msg, process_fname_step)


def process_fname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_lname_step)
    except Exception as e:
        bot.reply_to(message, 'что-то пошло не так')


def process_lname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.lname = message.text
        bot.send_message(message.chat.id, "Регистрация завершена")
    except Exception as e:
        bot.reply_to(message, 'что-то пошло не так')


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling(none_stop=True)
