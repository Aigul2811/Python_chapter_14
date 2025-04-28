'''
Напишите генератор, который будет генерировать данные о кампаниях, запущенных в указанном городе и имеющих бюджет выше заданного значения
Функция campaign_generator должна принимать путь к файлу, город и бюджет и генерировать словари, отсортированные по возрастанию 'ID Кампании' в формате:
{'ID Кампании': '657', 'Тип': 'Контекстная', 'Платформа': 'Вконтакте', 'Доход': '10692'}
{'ID Кампании': '674', 'Тип': 'Нативная интеграция', 'Платформа': 'Яндекс', 'Доход': '20766'}
{'ID Кампании': '761', 'Тип': 'Соцсети', 'Платформа': 'Вконтакте', 'Доход': '15680'}
'''

import csv

def campaign_generator(file_csv, city, revenue):
    with open(file_csv, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]  

    fil1 = [{'ID Кампании': row['ID Кампании'], 'Тип': row['Тип кампании'], 'Платформа': row['Платформа'], 'Доход': row['Доход']} for row in data if row['Город'] == city]
    fil2 = list(filter(lambda row: int(row['Доход']) > revenue, fil1))
    sorted(fil2, key = lambda x: x['ID Кампании'])
    
    for row in fil2:
        # Получаем значения из словаря
        yield(row)
           

print(list(campaign_generator('campaign_data.csv', 'Москва', 25000)))
