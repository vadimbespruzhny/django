
# import csv
# import django
import os
import os.path
import sqlite3
from sqlite3 import Error
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db.sqlite3')
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_site.settings'
# django.setup()




def create_connect(db):
    connection = None
    try:
        connection = sqlite3.connect(db)
        print('ok')
    except Error as e:
        print(f'Ошибка {e}')
    return connection


# create_connect(db_path)


def create_table(db):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    sql = "create table people (first_name text, last_name text)"
    cursor.execute(sql)
    print(cursor)

# create_table(db_path)


def create_data(db):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    sql = "insert into people values ('vasya', 'pupkin')"
    cursor.execute(sql)
    connect.commit()
    print('successfully creating data')

# create_data(db_path)


def get_data(db):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    sql = "select name from sqlite_master where type='table'"
    cursor.execute(sql)
    data = cursor.fetchall()
    print('successfully getting data', data)


get_data(db_path)
# with open('django_site/note_2.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';')
#     writer.writerow(['name, price'])

# with open('django_site/note_2.csv') as f:
#     print(f)
