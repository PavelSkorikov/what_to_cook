from bs4 import BeautifulSoup
from main_app.helpers.myip import get_html
import psycopg2
import psycopg2.extras
import uuid

psycopg2.extras.register_uuid()

def getData(url):
    r = get_html(url)
    ingredients = []
    if r:
        soup = BeautifulSoup(r, 'lxml')
        try:
            data = soup.find_all('a', class_='vertical_pseudo')
            for i in data:
                ingredients.append(i.get('title'))
        except:
            return 'Ошибка парсинга данных'
    else:
        return 'Не удалось получить данные'
    return ingredients

def write_in_bd(data_list):
    conn = psycopg2.connect(
        dbname='what_to_cook',
        user='pavel',
        password="1",
        host="127.0.0.1",
        port="5432"
    )
    print("Database opened successfully")
    cur = conn.cursor()
    id = 0
    try:
        for item in data_list:
            id += 1
            cur.execute("INSERT INTO main_app_ingridient VALUES (%s, %s)", (uuid.uuid4(), item))
    except Exception as e:
        print('error', e)
    conn.commit()
    print("Record inserted successfully")


if __name__ == '__main__':
    url = 'https://fitaudit.ru/categories/fds'
    print(getData(url))
    write_in_bd(getData(url))
