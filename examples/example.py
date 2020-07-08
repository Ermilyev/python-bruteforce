import requests
from datetime import datetime

site_url = ["Список сайтов"]

for url in site_url:
    m = 0
    for i in range(200):
        file = open('../log.txt', 'a', encoding='utf-8')
        start_time = datetime.now()
        response = requests.get(url)
        print(f'Caйт - {url}, Обращение - {i}, Код статуса - {response.status_code}, '
              f'Время запроса -  {datetime.now() - start_time}')
        file.write(f'Caйт - {url}, Обращение - {i}, Код статуса - {response.status_code}, '
                   f'Время запроса -  {datetime.now() - start_time}\n')

print("Завершение программы")