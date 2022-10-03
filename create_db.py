import sqlite3

sections = [
    (1, 'Торты', 'Ежедневно готовим вкусные и недорогие торты из натуральных и свежих ингредиентов'),
    (2, 'Пирожные', 'Очень вкусные пирожные'),
    (3, 'Хлеб', 'Всякоразный хлеб'),
    (4, 'Блинчики', 'Cытные блинчики'),
]
products = [
    (1, 'Прага', 'Торт-классика. Насыщенные шоколадные коржи в сочетании смасляно-заварным шоколадным кремом создают потрясающий шоколадный вкус.', 1),
    (2, 'Йогуртовый', 'Нежный бисквитный торт с йогуртовой прослойкой. В составе: ванильные коржи, крем на основе йогурта и натуральных сливок, с добавлением консервированных персиков.', 1),
    (3, 'Медовое', 'Трёхслойное пирожное на основе медовых коржей с начинкой \"Варёная сгущенка\", посыпанное крошкой.', 2),
    (4, 'Брауни', 'Классический насыщенный шоколадный десерт.', 2),
    (5, 'Ржаной', 'Ржаной хлеб-это разновидность хлеба, приготовленного из различных пропорций муки из ржаного зерна.', 3),
    (6, 'Рижский', 'Хлеб богат клетчаткой, магнием, витаминами групп В, фосфором, железом и другими полезными веществами. Регулярное употребление заварного ржаного хлеба нормализует пищеварение, предупреждает образование холестериновых бляшек, активизирует обмен веществ.', 3),
    (7, 'С вишней', 'Румяный блинчик с вишней.', 4),
    (8, 'С клубникой', 'Румяный блинчик с клубникой.', 4),

]

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS sections(
    id INTEGER PRIMARY KEY,
    section_name TEXT NOT NULL,
    section_description TEXT
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS assortment(
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_description TEXT,
    section_id INTEGER,
    FOREIGN KEY (section_id)  REFERENCES sections (id)
);
''')

cur.executemany('INSERT INTO sections VALUES(?, ?, ?);', sections)
cur.executemany('INSERT INTO assortment VALUES(?, ?, ?, ?);', products)
# con.commit()
# con.close()


con.commit()
con.close()