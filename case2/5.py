'Напишите функцию, которая возвращает средний бюджет всех кампаний, запущенных на определенной платформе'
import csv, statistics

def calculate_average_budget(file_csv, platform_name):
    # Открываем файл csv и читаем данные в список словарей
    with open(file_csv, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

        results = {}

        for row in data:
            # Получаем значения из словаря
            campaign_id = row['ID Кампании']            
            platform = row['Платформа']
            budget = row['Бюджет']                 

            budget = float(budget) 

            key = (campaign_id) 

            if platform == platform_name:
                if key not in results:
                    results[campaign_id] = budget
                else:
                    results[campaign_id] += budget
        

        res = round(statistics.mean(results.values()), 2)         
                
        return res       

print(calculate_average_budget('campaign_data.csv', 'Google'))
