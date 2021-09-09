import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests

token = '90029351296abbb21ddb4ef51f62a9dbfd0276e46e94fab1341402dd9d00cb3d981d01f9d401df56aecb9'
group_id = '193939883'


def main():
    vk_session = vk_api.VkApi(
        token=token)

    longpoll = VkBotLongPoll(vk_session, group_id)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            mess = event.obj.message

            response = requests.get('https://api.vk.com/method/users.get',
                                    params={'user_ids': event.obj.message['from_id'],
                                            'access_token': token,
                                            'v': '5.103'}).json()
            fullname = response['response'][0]['first_name'] + ' ' + response['response'][0]['last_name']

            data = {'text_question': mess['text'], 'vk_id': mess['id'], 'vk_id_author': mess['from_id'],
                    'vk_name_author': fullname}
            response = requests.post('http://192.168.0.228:8000/api/message/', json=data, data=data).json()
            if response:
                text_message = f"Message Id={mess['id']}. {mess['text']}"
                telegram_response = requests.get(f"https://api.telegram.org/bot1937675661:AAEwE1U0255l9MgPSMNfcIXdOeCjzaIEsVw/sendMessage?chat_id=-581581642&parse_mode=Markdown&text={text_message}")
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Здравствуйте {fullname}!\n Ваш вапрос принят к рассмотрению.",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
