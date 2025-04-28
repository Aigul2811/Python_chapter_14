#Напишите функцию, которая будет принимать на вход путь к файлу и возвращать сгруппированные данные по городам, содержащие суммарный бюджет и количество кликов

import csv

def group_campaign_data(file_csv):
    with open(file_csv, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]   
           
    result = {}

    for row in data:
    # Получаем значения из словаря
        city = row['Город']            
        budget = int(row['Бюджет'])
        clicks = float(row['Клики'])

        if city not in result:
            result[city] = {"Город": city, "Количество кликов": 0, "Суммарный бюджет": 0}

        result[city]['Количество кликов'] += clicks
        result[city]['Суммарный бюджет'] += budget


    res = [result[i] for i in result]
    res_sort = sorted(res, key = lambda i: i['Город'])  
    return res_sort 

print(group_campaign_data('campaign_data.csv'))