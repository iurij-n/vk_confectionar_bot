import os

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv()

TOKEN = os.getenv('TOKEN')

authorize = vk_api.VkApi(token=TOKEN)
longpool = VkLongPoll(authorize)

def write_message(user_id, message):
    authorize.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.text, event.user_id)
        if event.text == 'Привет':
            write_message(event.user_id, 'И тебе привет! )))')