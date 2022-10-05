import os
import sqlite3

import vk_api
import json
from dotenv import load_dotenv
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id

from keyboards import SECTIONS


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv()

TOKEN = os.getenv('TOKEN')

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')


authorize = vk_api.VkApi(token=TOKEN)
longpool = VkLongPoll(authorize)
upload = vk_api.VkUpload(authorize)

def write_message(user_id, keyboard, message='', attachment=None):
    authorize.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': get_random_id(),
        'keyboard': keyboard,
        'attachment': attachment
    })

def write_to_file(data):
    with open('tmp_img.jpg', 'wb') as file:
        file.write(data)

def get_bot_keybord(keyboard):
    return str(json.dumps(keyboard, ensure_ascii=False).encode('utf-8').decode('utf-8'))

def get_assortment():
    connect = sqlite3.connect('db.sqlite')
    cursor = connect.cursor()
    
    cursor.execute('''
        SELECT product_name
        FROM assortment
    ''')

    cursor_value = tuple(cursor)
    connect.commit()
    connect.close()

    return [value[0] for value in tuple(cursor_value)]

def get_product_info(product_name: str) -> str:
    
    connect = sqlite3.connect('db.sqlite')
    cursor = connect.cursor()
    
    query = (
        'SELECT assortment.product_description, sections.section_name '
        'FROM assortment, sections '
        'WHERE assortment.section_id = sections.id '
        f'AND assortment.product_name = \'{product_name}\''
    )
    
    cursor.execute(query)
    connect.commit()
    cursor_value = tuple(cursor)[0]
    connect.close()
    return cursor_value[0], cursor_value[1]

def get_product_photo(product_name: str) -> str:
    
    connect = sqlite3.connect('db.sqlite')
    cursor = connect.cursor()
    
    query = (
        'SELECT product_photo '
        'FROM assortment '
        f'WHERE product_name = \'{product_name}\''
    )
    
    cursor.execute(query)
    connect.commit()

    photo = tuple(cursor)[0][0]

    connect.close()

    write_to_file(photo)
    product_photo = upload.photo_messages('tmp_img.jpg')[0]
    os.remove('tmp_img.jpg')
    
    owner_id = product_photo['owner_id']
    id = product_photo['id']
    access_key = product_photo['access_key']
    
    return f'photo{owner_id}_{id}_{access_key}'


ASSORTMENT = get_assortment()


for event in longpool.listen():
    attachment = None
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == '\start':
            keyboard = SECTIONS['Главное меню']['keyboard']
            message = 'Выберите раздел:'
            write_message(event.user_id, get_bot_keybord(keyboard), message)
        if event.text in list(SECTIONS):
            keyboard = SECTIONS[event.text]['keyboard']
            message = f'Вы находитесь в разделе \"{event.text}\"'
            write_message(event.user_id, get_bot_keybord(keyboard), message)
        if event.text in ASSORTMENT:
            message, section = get_product_info(event.text)
            keyboard = SECTIONS[section]['keyboard']
            attachment = get_product_photo(event.text)
            write_message(event.user_id, get_bot_keybord(keyboard), message, attachment)
