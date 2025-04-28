'Напишите генератор, который будет генерировать даты, в которые НЕ запускались кампании'
import csv, datetime

def get_missing_campaign_dates(file_csv):
   # Открываем файл csv и читаем данные в список словарей
    with open(file_csv, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]    
        
     # Получаем значения из словаря               
    dates = {(datetime.datetime.strptime(row['Начальная дата'], '%Y-%m-%d')).date() for row in data}         
               
    res = []
    current_data, end_data_cam = min(dates), max(dates)
    while current_data < end_data_cam:         
        current_data += datetime.timedelta(days=1)
        if current_data not in dates:
            res.append(current_data)

    for d in sorted(res):
        yield d

get_missing_campaign_dates('campaign_data.csv')