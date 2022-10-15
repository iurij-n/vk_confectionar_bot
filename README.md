### Описание
Чат-бот для социальной сети ВКонтакте - мини-витрина кондитерской. 4 раздела, в каждом по 2 товара. У каждого товара есть описание и фотография. Из раздела можно возвращаться назад, в главное меню с названиями разделов. Для навигации используются кнопки.

Бот работает через официальное api. Подключение к VK через longpoll.

Данные хранятся в базе данных sqlite в двух связанных таблицах 'sections' и 'assortment', работа с которыми ведется с помощью SQL-запросов. Фотографии хранятся в базе данных в виде двоичных объектов.

![ER-диаграмма базы данных](/ER-diagram.png "ER-диаграмма базы данных")

### Технологии
Python 3.7
SQL
sqlite

### Запуск проекта
- - Клонируйте репозиторий
```git clone https://github.com/iurij-n/vk_confectionar_bot.git```

- - Установите и активируйте виртуальное окружение
- - Установите зависимости из файла requirements.txt
``` pip install -r requirements.txt ``` 

- - На основе шаблона '.env.template' создайте файл '.env' и запишите в нем токен для доступа к чату сообщества
- - Используйте готовую базу данных из репозитория или создайте новую запустив скрипт   'create_db.py'
- - Запустите 'main.py'


### Автор
Novikov Jurij