import telebot

bot = telebot.TeleBot("7375821198:AAEzG1AcKC3I7QByF4zkxeZLRsv67hTj1v8")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет,меня зовут Алексей.В этом году я сдал ЕГЭ и хочу поделиться своим опытом,могу чем-нибудь помочь?")

@bot.message_handler(commands=["werty"])
def werty_handler(message):
    bot.send_message(message.chat.id, " Я сдавал 3 премета: Русский язык, физику и профильную математику ,русский сдал на 60,профиль на 78, физику а 68.")

@bot.message_handler(commands=["lesson"])
def inform1_handler(message):
    bot.send_message(message.chat.id, " Я занимался индивидуально: и в школе, и дома прорешивал варианты,но особый вклад внесла онлайн школа умскул, я занимался по физике и по математике.")

@bot.message_handler(commands=["teacher"])
def teacher_handler(message):
    bot.send_message(message.chat.id, "Я занимался у Макса Теслы по физике, у Аделии Адамовой и Артура Шарафиева по профилю")

@bot.message_handler(commands=["ok"])
def ok_handler(message):
    bot.send_message(message.chat.id, "Обращайтесь ,буду рад помочь")

bot.infinity_polling()