import requests

API_URL = 'https://api-metrika.yandex.ru/stat/v1/data'
API_token = 'YOU_TOKEN'
params = {
    'date1': '10daysAgo',
    'date2': 'today',
    'id': 95281988,
    'metrics': 'ym:s:visits,ym:s:users',
    'dimensions': 'ym:s:TrafficSource',
    'filters': "ym:s:isRobot=='No'",
    'limit': 1000
}

# Выполняем запрос к API
response = requests.get(API_URL, params=params, headers={'Authorization': API_token})

# Проверяем успешность запроса
if response.status_code == 200:
    # Извлекаем данные из ответа
    data = response.json().get('data', [])

    # Проверяем, есть ли данные в ответе
    if data:
        for item in data:
            print(f"Источник трафика: {item['dimensions'][0]['name']}")
            print(f"Количество посещений: {item['metrics'][0]}")
            print(f"Количество пользователей: {item['metrics'][1]}")
            print("-" * 30)
    else:
        print('Данные не найдены в ответе API.')
else:
    print(f'Ошибка при запросе к API. Код ответа: {response.status_code}')
