import os
import sqlite3

import vk_api
import json
from dotenv import load_dotenv
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv()

TOKEN = os.getenv('TOKEN')

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')


authorize = vk_api.VkApi(token=TOKEN)
longpool = VkLongPoll(authorize)

def write_message(user_id, message, keyboard):
    authorize.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': get_random_id(),
        'keyboard': keyboard
        # 'keyboard': keyboard.get_keyboard()
    })


def get_text_button(label, color):
    return {
                'action': {
                    'type': 'text',
                    'payload': "{}",
                    'label': f'{label}'
                },
                'color': f'{color}'
            }


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
    
    cursor.execute('''
        SELECT product_name, product_description
        FROM assortment
    ''')
    
    
    cursor_value = tuple(cursor)
    
    connect.commit()
    connect.close()
    
    
    return [value[1] for value in tuple(cursor_value) if value[0] == product_name]
    
    
# SECTION_LIST = ['Торты', 'Пирожные', 'Хлеб', 'Блинчики']

# MAIN_KEYBOARD = {
#     'one_time': False,
#     'buttons': [
#         [get_text_button('Торты', 'primary'), get_text_button('Пирожные', 'primary')],
#         [get_text_button('Хлеб', 'primary'), get_text_button('Блинчики', 'primary')]
#     ]
# }
ASSORTMENT = get_assortment()

print(ASSORTMENT)

SECTIONS = {
    'Главное меню': {
        'keyboard': {
                    'one_time': False,
                    'buttons': [
                        [get_text_button('Торты', 'primary'), get_text_button('Пирожные', 'primary')],
                        [get_text_button('Хлеб', 'primary'), get_text_button('Блинчики', 'primary')]
                    ]
                }
        },
    'Торты': {
        'keyboard': {
                     'one_time': False,
                     'buttons': [
                         [
                             get_text_button('Прага', 'primary'),
                             get_text_button('Йогуртовый', 'primary')
                         ],
                         [
                             get_text_button('Главное меню', 'secondary')
                         ]
                     ]
                    }
        },
    'Пирожные': {
        'keyboard': {
                    'one_time': False,
                    'buttons': [
                        [
                            get_text_button('Медовое', 'primary'),
                            get_text_button('Брауни', 'primary')
                        ],
                        [
                            get_text_button('Главное меню', 'secondary')
                        ]
                    ]
                }
        },
    'Хлеб': {
        'keyboard': {
                    'one_time': False,
                    'buttons': [
                        [
                            get_text_button('Ржаной', 'primary'),
                            get_text_button('Рижский', 'primary')
                        ],
                        [
                            get_text_button('Главное меню', 'secondary')
                        ]
                    ]
                }
        },
    'Блинчики': {
        'keyboard': {
                    'one_time': False,
                    'buttons': [
                        [
                            get_text_button('С вишней', 'primary'),
                            get_text_button('С клубникой', 'primary')
                        ],
                        [
                            get_text_button('Главное меню', 'secondary')
                        ]
                    ]
                }
    }
}

# CAKE_KEYBOARD = {
#     'one_time': False,
#     'buttons': [
#         [
#             get_text_button('Прага', 'primary'),
#             get_text_button('Йогуртовый', 'primary')
#         ],
#         [
#             get_text_button('В главное меню', 'secondary')
#         ]
#     ]
# }

# PIE_KEYBOARD = {
#     'one_time': False,
#     'buttons': [
#         [
#             get_text_button('Медовое', 'primary'),
#             get_text_button('Брауни', 'primary')
#         ],
#         [
#             get_text_button('В главное меню', 'secondary')
#         ]
#     ]
# }

# PANCAKE_KEYBOARD = {
#     'one_time': False,
#     'buttons': [
#         [
#             get_text_button('С вишней', 'primary'),
#             get_text_button('С клубникой', 'primary')
#         ],
#         [
#             get_text_button('В главное меню', 'secondary')
#         ]
#     ]
# }

# BREAD_KEYBOARD = {
#     'one_time': False,
#     'buttons': [
#         [
#             get_text_button('Ржаной', 'primary'),
#             get_text_button('Рижский', 'primary')
#         ],
#         [
#             get_text_button('В главное меню', 'secondary')
#         ]
#     ]
# }


# MAIN_KEYBOARD = get_bot_keybord(MAIN_KEYBOARD)

# main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
# main_keyboard = str(main_keyboard.decode('utf-8'))
# keyboard = VkKeyboard(one_time=False)
# keyboard.add_button('&#127829;Первая кнопка', color=VkKeyboardColor.SECONDARY)
# keyboard.add_button('&#127846;Вторая кнопка', color=VkKeyboardColor.PRIMARY)
# keyboard.add_line()
# keyboard.add_button('&#127851;Третья кнопка', color=VkKeyboardColor.NEGATIVE)
# keyboard.add_button('&#127856;Четвертая кнопка', color=VkKeyboardColor.POSITIVE)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.type, event.text, event.user_id)
        if event.text == '\start':
            keyboard = SECTIONS['Главное меню']['keyboard']
            message = 'Выберите раздел:'
        if event.text in list(SECTIONS):
            keyboard = SECTIONS[event.text]['keyboard']
            message = f'Вы находитесь в разделе \"{event.text}\"'
        if event.text in ASSORTMENT:
            message = get_product_info(event.text)
        
        # if event.text == 'Торты':
        #     keyboard = CAKE_KEYBOARD
        #     message = 'Раздел \"Торты\"'
        # elif event.text == 'Пирожные':
        #     keyboard = PIE_KEYBOARD
        #     message = 'Раздел \"Пирожные\"'
        # elif event.text == 'Хлеб':
        #     keyboard = BREAD_KEYBOARD
        #     message = 'Раздел \"Хлеб\"'
        # elif event.text == 'Блинчики':
        #     keyboard = PANCAKE_KEYBOARD
        #     message = 'Раздел \"Блинчики\"'        
        # elif event.text == 'В главное меню':
        #     keyboard = MAIN_KEYBOARD
        #     message = 'Выберите раздел'         
        
        
        write_message(event.user_id, message, get_bot_keybord(keyboard))
