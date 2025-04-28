'Найдите самую эффективную платформу по средним значениям конверсий'
import csv, statistics

with open(campaign_data.csv, mode="r", encoding="utf-8", newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',', quotechar='"') # Можно написать reader = csv.DictReader(csv_file)
    
    # Создание словаря, где ключ - название платформы, а значение - массив конверсий
    platform_dict = {}   
    for row in reader:     
        if row['Платформа'] not in platform_dict:
            platform_dict[row['Платформа']] = [int(row['Конверсия'])]
        else:    
            platform_dict[row['Платформа']].append(int(row['Конверсия'])) 

# Вычисление средних значений конверсий для каждой платформы 
platform_avg_conversions = {platform: statistics.mean(conversions) for platform, conversions in platform_dict.items()}

most_effective_platform = max(platform_avg_conversions, key=platform_avg_conversions.get)

print(most_effective_platform)
print(platform_dict)

