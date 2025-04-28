'Посчитайте долю затрат на рекламные кампании каждой платформы и каждого города'
import csv

# Открываем файл csv и читаем данные в список словарей
with open(campaign_data.csv, mode='r', encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    data = [row for row in reader]

results = {}

for row in data:
    # Получаем значения из словаря
    campaign_id = row['ID Кампании']
    start_date = row['Начальная дата']
    end_date = row['Конечная дата']
    campaign_type = row['Тип кампании']
    platform = row['Платформа']
    budget = row['Бюджет']
    city = row['Город']
    shows = row['Показы']
    clicks = row['Клики']
    conversion = row['Конверсия']
    revenue = row['Доход']

    # Формируем ключ для группировки по типу кампании и платформе
    key = (platform)

    # Если ключ еще не был добавлен в словарь, то добавляем его и создаем пустой список для хранения результатов
    if key not in results:
        results[key] = {'cities': {}, 'total_budget': 0}
    

    # Добавляем значение города для данной кампании в словарь результатов
    if city not in results[key]['cities']:
        results[key]['cities'][city] = 0
   
    # Считаем затраты на данную кампанию
    budget = round(float(budget))
    results[key]['total_budget'] += budget

    # Увеличиваем количество затрат для данного города
    results[key]['cities'][city] += budget

print(results)


with open("/home/user/Рабочий стол/Создать папку 7/питон/Глава 14/Кейс 2/platform_city_results.txt", mode="w", encoding="utf-8") as output_file:
    # Выводим результаты для каждой группы (тип кампании и платформа)
    for key in results:
        cities = results[key]['cities']
        total_budget = results[key]['total_budget']

        # Сортируем города по количеству затрат на рекламу
        sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)

        # Записываем результаты в файл
        output_file.write(f"Для группы {key}:\n")
        for city, budget in sorted_cities:
            percent_of_budget = round(budget / total_budget * 100, 2)
            output_file.write(f"- Город: {city}, доля затрат на рекламу: {percent_of_budget}%\n")