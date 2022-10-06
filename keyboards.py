def get_text_button(label, color):
    return {
                'action': {
                    'type': 'text',
                    'payload': "{}",
                    'label': f'{label}'
                },
                'color': f'{color}'
            }


SECTIONS = {
    'Главное меню': {
        'keyboard': {
                    'one_time': False,
                    'buttons': [
                        [
                            get_text_button('Торты', 'primary'),
                            get_text_button('Пирожные', 'primary')
                        ],
                        [
                            get_text_button('Хлеб', 'primary'),
                            get_text_button('Блинчики', 'primary')
                        ]
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
