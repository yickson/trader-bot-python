import telebot

TOKEN = '1742970522:AAEri7_sHRWeyHrGd5NJDxZCFNd-pQlUFwE'
userId = '360495416'
tb = telebot.TeleBot(TOKEN)

number = 445.789045
text = 'BAKE'
message = 'Preparing to buy: %f %s' % (number, text)
tb.send_message(userId, message)
