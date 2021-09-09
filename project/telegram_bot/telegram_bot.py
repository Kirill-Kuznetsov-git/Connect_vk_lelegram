import telebot
import requests

token = '1937675661:AAEwE1U0255l9MgPSMNfcIXdOeCjzaIEsVw'
chat_id = "-581581642"
bot_id = 1937675661
bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.reply_to_message.from_user.id == bot_id)
def catch_reply_message(message):
    message_vk_id = int(message.reply_to_message.text.split('.')[0].split('=')[1])

    data = {"telegram_id_who_answered": message.from_user.id,
            "telegram_name_author": message.from_user.username,
            "telegram_id": message.message_id,
            "text_answer": message.text}
    response = requests.patch(f'http://localhost:8000/api/message/{message_vk_id}', data=data).json()
    if response['status'] == "Success":
        response_vk = requests.get(f"https://api.vk.com/method/messages.send?user_id={response['message']['vk_id_author']}&message={message.text}&v=5.37&access_token=90029351296abbb21ddb4ef51f62a9dbfd0276e46e94fab1341402dd9d00cb3d981d01f9d401df56aecb9")


bot.polling()
