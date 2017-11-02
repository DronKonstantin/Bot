import telebot
import misc
import requests
import os

appid = "e03925cafba20b665dc891e119dcd297"
#city_id for Abakana
city_id = 1512236
bot = telebot.TeleBot(misc.token)

#bot.send_message(305774189,"test")

#upd = bot.get_updates()
#print(upd)

#last_upd=upd[-1]
#message_from_user=last_upd.message
#print(message_from_user)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('новости', 'погода')
    user_markup.row('чаты', 'такси','интересное')
    user_markup.row('/start')
    bot.send_message(message.chat.id, 'Привет, меня зовут Колян, а ТЫ ПИДОР\U0001F60C\nМогу тебе показать:\n\U0001F4DDновости\n\U0001F31Fпогоду\n\U0001F6BBчаты', reply_markup=user_markup)

def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть. Шучу. Не рад. начнем?'.format(name=message.text))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "чаты":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('знакомства','где купить?')
        user_markup.row('/start')
        bot.send_message(message.chat.id, 'Выбор чатов', reply_markup=user_markup)
    if message.text == "новости":
        bot.send_message(message.chat.id, "переходи по ссылке @abakanlife")
    if message.text == "знакомства":
        directory='C:/photo'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            img=open(directory+'/'+file,'rb')
            bot.send_photo(message.from_user.id, img)
            img.close()
            bot.send_message(message.chat.id, "переходи по ссылке @abakan_pva ")
    if message.text == "такси":
        bot.send_message(message.chat.id, "Такси Саяны, 83902222222\nMaxim, 83902300102")
    if message.text[:7] == "Погода" or message.text[:7] == "погода" :
            city = message.text[7:]
            r = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = r.json()
            temp = data["main"]["temp"]
            conditions=data['weather'][0]['description']
            bot.send_message(message.chat.id, "\U000026C4Погода в Абакане:{} \nТемпература: {} C".format(city, temp))
            bot.send_message(message.chat.id, "Обстановочка{}: {} ".format(city, conditions))


bot.polling()