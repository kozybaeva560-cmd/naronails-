bot.pyimport telebot
from telebot import types

# 👉 сюда вставь свой токен
TOKEN = "8474634796:AAEgxuUs5n27E8OulkCBr041B0JtKa0N_N0"
bot = telebot.TeleBot(TOKEN)

# Главное меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💅 Записаться")
    btn2 = types.KeyboardButton("📋 Прайс")
    btn3 = types.KeyboardButton("📞 Контакты")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 🌸\n"
        "Добро пожаловать в NARO NAILS!\n"
        "Выберите действие ниже 👇",
        reply_markup=markup
    )

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "💅 Записаться":
        bot.send_message(message.chat.id, "Чтобы записаться, напишите мне сюда 👉 @naro.nails 💛")
    elif message.text == "📋 Прайс":
        bot.send_message(message.chat.id, "💅 Маникюр — от 4000 тг\n💎 Наращивание — от 6000 тг\n✨ Дизайн — от 1000 тг")
    elif message.text == "📞 Контакты":
        bot.send_message(message.chat.id, "📍 Конаев\n📱 WhatsApp: +7 747 199 6243\n📸 Instagram: @naro.nails")
    else:
        bot.send_message(message.chat.id, "Выберите действие с помощью кнопок ниже 👇")

print("Бот запущен...")
bot.polling(none_stop=True)
