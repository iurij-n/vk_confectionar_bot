import sqlite3

sections = [
    (1, 'Торты', 'Ежедневно готовим вкусные и недорогие торты'
        'из натуральных и свежих ингредиентов'),
    (2, 'Пирожные', 'Очень вкусные пирожные'),
    (3, 'Хлеб', 'Всякоразный хлеб'),
    (4, 'Блинчики', 'Cытные блинчики'),
]
products = [
    (1, 'Прага', 'Торт-классика Прага. Насыщенные шоколадные коржи в '
        'сочетании смасляно-заварным шоколадным кремом создают '
        'потрясающий шоколадный вкус.', 'img\img_06.jpg', 1),
    (2, 'Йогуртовый', 'Торт Йогуртовый. Нежный бисквитный торт с '
        'йогуртовой прослойкой. В составе: ванильные коржи, крем на '
        'основе йогурта и натуральных сливок, с добавлением '
        'консервированных персиков.', 'img\img_03.jpg', 1),
    (3, 'Медовое', 'Пирожное Медовое. Трёхслойное пирожное на основе '
        'медовых коржей с начинкой \"Варёная сгущенка\", '
        'посыпанное крошкой.', 'img\img_04.jpg', 2),
    (4, 'Брауни', 'Пирожное Брауни - классический насыщенный шоколадный '
        'десерт.', 'img\img_05.jpg', 2),
    (5, 'Ржаной', 'Ржаной хлеб-это разновидность хлеба, приготовленного из '
        'различных пропорций муки из ржаного зерна.', 'img\img_02.jpg', 3),
    (6, 'Рижский', 'Рижский хлеб богат клетчаткой, магнием, витаминами '
        'групп В, фосфором, железом и другими полезными веществами. '
        'Регулярное употребление заварного ржаного хлеба нормализует '
        'пищеварение, предупреждает образование холестериновых бляшек, '
        'активизирует обмен веществ.', 'img\img_01.jpg', 3),
    (7, 'С вишней', 'Румяный блинчик с вишней.', 'img\img_07.jpg', 4),
    (8, 'С клубникой', 'Румяный блинчик с клубникой.', 'img\img_08.jpg', 4),

]


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS sections(
    id INTEGER PRIMARY KEY,
    section_name TEXT NOT NULL,
    section_description TEXT
);

CREATE TABLE IF NOT EXISTS assortment(
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_description TEXT,
    product_photo BLOB,
    section_id INTEGER,
    FOREIGN KEY (section_id)  REFERENCES sections (id)
);
''')

cur.executemany('INSERT INTO sections VALUES(?, ?, ?);', sections)
con.commit()

for data in products:
    binary_img = convert_to_binary_data(data[3])
    data_tuple = (data[0], data[1], data[2], binary_img, data[4])
    cur.execute('INSERT INTO assortment VALUES(?, ?, ?, ?, ?);', data_tuple)
    con.commit()

con.close()
