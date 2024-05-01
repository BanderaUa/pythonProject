import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('7102318266:AAGteGaM-xoYKVjLHpzI5rQVKOBBJhnsmqM')

conn = sqlite3.connect('active_cards.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               card1 TEXT,
               card2 TEXT,
               card1_balance INTEGER,
               card2_balance INTEGER
               )''')
conn.commit()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        markup = types.InlineKeyboardMarkup()
        button_cabinet = types.InlineKeyboardButton('Особистий кабінет🏠', callback_data='personal_cabinet')
        button_support = types.InlineKeyboardButton('Служба підтримки🗣', callback_data='support')
        button_license = types.InlineKeyboardButton('Ліцензія від НБУ🏦', callback_data='license')
        button_exit = types.InlineKeyboardButton('Завершити роботу⛔', callback_data='exit')
        markup.add(button_cabinet)
        markup.add(button_support)
        markup.add(button_license)
        markup.add(button_exit)

        bot.send_message(message.chat.id,
                         f"<b>Добрий день, {message.from_user.username}, Христос посеред нас!</b>😊",
                         parse_mode='HTML', reply_markup=markup)

    elif message.text == '/help':
        markup = types.InlineKeyboardMarkup()
        button_cabinet = types.InlineKeyboardButton('Особистий кабінет🏠', callback_data='personal_cabinet')
        button_support = types.InlineKeyboardButton('Служба підтримки🗣', callback_data='support')
        button_license = types.InlineKeyboardButton('Ліцензія від НБУ🏦', callback_data='license')
        button_exit = types.InlineKeyboardButton('Завершити роботу⛔', callback_data='exit')
        markup.add(button_cabinet)
        markup.add(button_support)
        markup.add(button_license)
        markup.add(button_exit)
        bot.send_message(message.chat.id, "<b>Cхоже, у вас трапилась халепа, що саме вас цікавить?</b>&#128516;",
                         parse_mode='HTML', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def photo_reply(message):
    bot.reply_to(message, "<b>Дуже гарне фото, але давайте повернемося до фінансів&#128521</b>",
                 parse_mode='HTML')


@bot.message_handler(content_types=['audio'])
def audio_reply(message):
    bot.reply_to(message,
                 "<b>У вас гарний музичний смак, але нажаль в нас немає часу на оцінку цього треку, тож повернемося до банківської справи&#128521</b>",
                 parse_mode='HTML')


@bot.message_handler(content_types=['video'])
def video_reply(message):
    bot.reply_to(message,
                 "<b>На превеликий жаль ми не можемо завантажити це відео. \nТрафік рахунок цінує!&#128521</b>",
                 parse_mode='HTML')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message_main_page(callback):
    if callback.data == 'personal_cabinet':
        markup = types.InlineKeyboardMarkup()
        button_my_cards = types.InlineKeyboardButton('Мої картки💳', callback_data='my_cards')
        button_open_card = types.InlineKeyboardButton('Відкрити картку💸', callback_data='open_card')
        button_credit = types.InlineKeyboardButton('Кредитний ліміт💰', callback_data='credit')
        button_my_debt = types.InlineKeyboardButton('Заборгованості📥', callback_data='debt')
        button_limits = types.InlineKeyboardButton('Ліміти на оплату❗', callback_data='limits')
        button_accumulation = types.InlineKeyboardButton('Накопичення💹', callback_data='accumulation')
        button_cashback = types.InlineKeyboardButton('Кешбек💵', callback_data='cashback')
        button_conditions = types.InlineKeyboardButton('Умови і тарифи🧾', callback_data="conditions")
        button_auto = types.InlineKeyboardButton('Автострахування🚘', callback_data='auto')
        button_friends = types.InlineKeyboardButton('Запросити друга🫂', callback_data='friends')
        button_charity = types.InlineKeyboardButton('Благодійність🙏', callback_data='charity')
        button_terminals = types.InlineKeyboardButton('Точки поповнення💱', callback_data='terminals')
        button_exit = types.InlineKeyboardButton('Повернутися на головну сторінку🔙', callback_data='exit')
        markup.row(button_my_cards, button_open_card)
        markup.row(button_credit, button_my_debt)
        markup.row(button_limits, button_accumulation)
        markup.row(button_cashback, button_conditions)
        markup.row(button_auto, button_friends)
        markup.row(button_terminals, button_charity)
        markup.row(button_exit)
        bot.send_message(callback.message.chat.id,
                         f"<b>{callback.from_user.username}, Ви увійшли у ваш персональний кабінет💫\n</b>"
                         '\n'
                         '\n'
                         "<i>Будь ласка оберіть, що саме вас цікавить⬇</i>", parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'license':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, """
<i>Повне найменування</i>:\nАКЦІОНЕРНЕ ТОВАРИСТВО КОМЕРЦІЙНИЙ БАНК «Slavik Industries»\n
<i>Скорочене найменування</i>:\nАТ КБ «SlavikBanking»\n
<i>Кореспондентський рахунок</i>:\n1337228131288 у Національному банку України\n
<i>IBAN-код Кореспондентського рахунку у Національному банку України АКЦІОНЕРНОГО ТОВАРИСТВА КОМЕРЦІЙНОГО БАНКУ «SlavikBanking»</i>:\nUA173000010000032003102901026\n
<i>МФО Національного банку України</i>:\n101001\n
<i>МФО</i>:\n1488234\n
<i>ЄДРПОУ</i>:\n14881312\n
<i>ІПН</i>:\n144535701251\n
<i>Свідоцтво</i>:\n№100238888\n
<i>Ліцензія НБУ</i>:\n№88 від 13.12.2003.\n
<i>SWIFT</i>:\nSLINUA2X\n
<i>SPRINT</i>:\nSLAVIK/UKRPACK
""",
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'support':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,
                         """🙋<b>Будь ласка наберіть наш номер телефону :\n<i>+380 66 148 88 88</i>\n
І ми обов'язково вам відповімо</b>.\n
\n
<i>📲Швидкість відповіді нашого співробітника залежить від загруженості банку.\n
⌛Зазвичай це займає не більше
5 - 10 хвилин</i>\n
""", parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'my_cards':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,
                         f"<b>{callback.from_user.username}, Наразі у вас немає відкритих карток у нашому банку😓\n</b>"
                         '\n'
                         '\n'
                         "<i>Якщо ви бажаєте відкрити картку у нашому банку, ви можете це зробити двома шляхами☺</i>:\n\n1) Перейти у головне меню➡ Натиснути Особистий кабінет🏠➡ Відкрити картку💸\n\n2) Зателефонувати оператору на гарячу лінію📲\nНаш номер телефону: +380 66 148 88 88\n",
                         parse_mode='HTML', reply_markup=markup)
    elif callback.data == 'credit':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,"<b>Так як ви зареєструвались у нашому банку,до його офіційного релізу,то ваш кредитний ліміт дорівнює - 700 000 гривень‼🙀</b>\n\nВи можете отримати його на вашу кредитну картку у розділі➡ <b>Відкрити картку💸</b>",reply_markup=markup,parse_mode='HTML')

    elif callback.data == 'limits':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,"Ми не встаномлюємо жодних лімітів на ваші платежі,можете робити операції скільки завгодно і куди завгодно.\n\nАле якщо ващі операції викличуть інтерес у працівников подактової інспекції ми вас попередимо!",reply_markup=markup,parse_mode='HTML')

    elif callback.data == 'terminals':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, """
         <b>Поповнити картки від Slavik можна у будь-якому термінали нашої країни, абсолютно без комісії 🙅💸</b>
                                                 """, parse_mode="HTML", reply_markup=markup)

    elif callback.data == 'conditions':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,
                         "<b>Умови обслуговуванння від Slavik🧾</b>\n\n<i>Умови дебітових карток💳:</i>\nКомісія за перекази - 0%\nКомісія за зняття готівки в банкоматах - 0%\nКомісія за перекази на картки іншого банку - 0%\n\n<i>Умови кредитних карток💳:</i>\nКомісія за перекази - 0%\nКомісія за зняття готівки в банкоматах - 0%\nКомісія за перекази на картки іншого банку - 0%\n\n<b><i>Ми не будемо дерти з вас по 100 гривень за переказ, як наші колеги із зеленого банку😅</i></b>.",
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'exit':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)

    elif callback.data == 'charity':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,
                         'Наразі Slavik не проводить благодійні збори, але з радістю дасть вам лінки на благодійні збори у Monobank🐈◼\n\nКотики Азову🐱\n🔗https://send.monobank.ua/jar/A6ExTgYxLa🔗\nРій помсти 2.0🦟\n🔗https://send.monobank.ua/jar/5TxaBie9Jm🔗\nМаркус Фундейшн🛡️\n🔗https://send.monobank.ua/jar/8QzzQ2r3uH🔗\nЯнголи Азову👼\n🔗https://send.monobank.ua/jar/4WbHXAaq2p🔗\nПовернись живим🫂\n🔗https://send.monobank.ua/jar/4Dyucs5PBU🔗',
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'friends':

        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, "🔹<b>Коли Slavik вийде з вeta-версії,вам буде наданий код,за яким ви зможете запросити товарищів та отримати 10$ за кожного.</b>🔹\n\nА поки користуйтеся самі і отримуйте задоволення,якщо помітите якісь баги ,або недоліки - звоніть на гарячу лінію!🙋\n\n\n<b>P.S.<i>(За це на вас чекатиме приємний сюрприз😘)</i></b>", reply_markup=markup,parse_mode="HTML")

    elif callback.data == 'accumulation':

        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, "<b>Slavik зараз знаходиться в прототипі,тому ще не може брати ваші гроші на збереження🤷</b>\n\n<i>Але коли ми вийдемо на рівень <u>зеленого</u> банку,то дамо вам найкращі умови для зберігання ваших коштів😽</i>", reply_markup=markup,parse_mode='HTML')

    elif callback.data == 'open_card':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        button_credit_card = types.InlineKeyboardButton('Кредитна💰', callback_data='credit_card')
        button_debit_card = types.InlineKeyboardButton('Дебітова💳', callback_data='debit_card')
        markup.add(button_credit_card)
        markup.add(button_debit_card)
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, "Ми дуже вдячні вам за те, що ви вирішили відкрити картку у нашому банку, будь ласка оберіть тип картки:\n<b>Кредитна💰</b>\n<b>Дебітова💳</b>\n\n<i>Нагадуємо, що максимальна кількість усіх карток - 5 штук😉</i>", parse_mode='HTML', reply_markup=markup )


    elif callback.data == 'credit_card':

        bot.send_message(callback.message.chat.id, "<b>Будь ласка вкажіть нижче бажану суму кредитного ліміту👇</b>",

                         parse_mode='HTML')

        @bot.message_handler(func=lambda message: message.text.isdigit())
        def get_credit_limit(message):

            global summ

            summ = int(message.text)


            conn = sqlite3.connect('active_cards.db')

            cur = conn.cursor()


            conn.commit()


            cur.close()

            conn.close()

            markup = types.InlineKeyboardMarkup()

            button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')

            markup.add(button_exit)

            bot.send_message(callback.message.chat.id, f"<b>Вам схвалено кредитний ліміт у {summ} гривень🥰\n\nКартка буде активована протягом 24 годин,та ви зможете її побачити у розділі-<b>Мої картки💳</b>\n<i>Будь ласка трішки зачекайте🥰</i></b>",
                             parse_mode='HTML', reply_markup=markup)

        @bot.message_handler(func=lambda message: not message.text.isdigit())
        def not_valid_input(message):

            bot.send_message(callback.message.chat.id, "<b>Будь ласка, введіть число</b>", parse_mode='HTML')
    elif callback.data == 'debit_card':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id, "<b>Ми дуже вдячні вам за те, що ви вирішили відкрити картку у нашому банку🥰\n\nКартка буде активована протягом 24 годин,та ви зможете її побачити у розділі-<b>Мої картки💳</b>\n<i>Будь ласка трішки зачекайте🥰</i></b>",parse_mode='HTML',reply_markup=markup)

    elif callback.data == 'debt':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,"<b>Коли у вас активуютсья кредитні картки,або ви візьмете кредит,тут буде відображена вся інформація🙋💰</b>\n\n<i>Зараз ви нічого нам не винні😉</i>",parse_mode='HTML',reply_markup=markup)

    elif callback.data == 'auto':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,"""🚘ОСАГО: від 1000 до 3000 грн на рік, залежно від регіону та параметрів автомобіля.🚘\n
\n🏍КАСКО: від 5000 до 15000 грн на рік, залежно від типу автомобіля та покриття.🏍\n
\n🏎Додаткове страхування від угону: від 500 до 1500 грн на рік.🏎\n
\n🏎Страхування від стихійних лих: від 500 до 2000 грн на рік.🏎\n
\n🏍ДСАГО (страхування від нещасного випадку): від 300 до 800 грн на рік.🏍\n
\n🚘Страхування від вандалізму: від 200 до 700 грн на рік.🚘\n
\n🚘Страхування від громадянської відповідальності перед пасажирами: від 200 до 500 грн на рік.🚘\n\n\nПовна інформація,консультація та оформлення за номером:\n<i>+380 66 148 88 88</i>\n\nДзвоніть та оформляйте страхування без відділень,бумажок і проблем🙋📞""",parse_mode="HTML",reply_markup=markup)

    elif callback.data == 'cashback':
        markup = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton('Назад🔙', callback_data='exit')
        markup.add(button_exit)
        bot.send_message(callback.message.chat.id,"""Список категорій за покупки в яких ви отримуєте кешбек😻💸\n
<b>За покупки пального: ⛽️</b>
1% з кредитної/ 3% з дебітової\n\n
<b>За покупки в супермаркетах: 🛒</b>
3% з кредитної/ 5% з дебітової\n\n
<b>За покупки у кофейнях : ☕</b>
4% з кредитної/ 8% з дебітової\n\n
<b>За покупки в інтернет-магазинах: 🛍️</b>
0.5% з кредитної/ 1% з дебітової\n\n
<b>За ресторанні витрати: 🍽️</b>
2% з кредитної/ 7% з дебітової\n\n
<b>За оплату у салонах краси: 💇‍♀️</b>
3% з кредитної/ 5% з дебітової""",reply_markup=markup,parse_mode='HTML')













#НЕ ТРОГАТЬ ДАЖЕ ПОД УГРОЗОЙ СМЕРТИ ИЛИ ГЛИСТОВ
bot.polling(none_stop=True)


