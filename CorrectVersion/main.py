import telebot
import tokken
import requests
import os
import random

appid = "e03925cafba20b665dc891e119dcd297"
#city_id for Abakana
city_id = 1512236
bot = telebot.TeleBot(tokken.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('\U0001F4DDновости', '\U0001F302погода',)
    user_markup.row('\U00002665чаты', '\U0001F695такси', '\U000026A0sos')
    user_markup.row('/start', '\U0001F307Абакан')
    bot.send_message(message.chat.id, 'Привет! Меня зовут Коля\U0001F60C\n\nМогу тебе показать:\n\U0001F4DDновости\n\U0001F302погоду\n\U00002764чаты\n\U0001F695номера такси\n\U0001F6A8номера экстренных служб\n\U0001F307рассказать про Абакан', reply_markup=user_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "\U00002665чаты":
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('\U00002764знакомства','\U0001F697автолюбители')
        user_markup.row('/start')
        bot.send_message(message.chat.id, 'Выбор чатов', reply_markup=user_markup)
    if message.text == "\U0001F4DDновости":
        bot.send_message(message.chat.id, "\U00002709Последние события\n\U00002712Интересные статьи\n\U0001F3ADОбзоры\n\U0001F53Dпереходи по ссылке: \n@abakanlife")
    if message.text == "\U0001F697автолюбители":
        bot.send_message(message.chat.id, "\U0001F539события\n\U0001F539ситуации на дорогах\n\U0001F539покупка-продажа\n\U0001F53Dпереходи по ссылке: \n@auto_19")
    if message.text == "\U00002764знакомства":
        bot.send_message(message.chat.id, "\U0001F538добавляемся\n\U0001F538пишем возраст\n\U0001F538интересы\n\U0001F538общаемся\U0001F60C\n\U0001F53Dпереходи по ссылке: @abk_chat")
    if message.text == "\U0001F695такси":
        bot.send_message(message.chat.id, "Maxim\U0001F695 83902300102\nТакси Саяны\U0001F695 83902222222\nЛидер\U0001F695 83902222666")
    if message.text[:7] == "\U0001F302погода" or message.text[:7] == "погода" :
            city = message.text[7:]
            r = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = r.json()
            temp = data["main"]["temp"]
            conditions=data['weather'][0]['description']
            bot.send_message(message.chat.id, "\U000026C4Погода в Абакане:{} \nТемпература: {} C".format(city, temp))
            bot.send_message(message.chat.id, "Обстановочка{}: {} ".format(city, conditions))
    if message.text == "\U0001F307Абакан":
        bot.send_message(message.chat.id, "http://telegra.ph/Abakan-11-02")
    if message.text == "\U000026A0sos":
        bot.send_message(message.chat.id, "\U000026A0Единый телефон экстренных служб:\n112\n\U000026A0МЧС России:\n101\n\U000026A0Скорая помощь Абакан:ул. Т. Шевченко, 83 «А»\n83902226372\n83902223497")




bot.polling()