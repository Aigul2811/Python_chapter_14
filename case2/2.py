'Найдите самый успешный тип рекламной кампании по средним значениям конверсий'
import csv, statistics
campaign_d = []

with open(campaign_data.csv, 'r') as campaign_data:
    reader = csv.DictReader(campaign_data, delimiter=',', quotechar='"')
    for line in reader:
        campaign_d.append(line)

pl_conv = {}

for i in campaign_d:
    if i['Тип кампании'] not in pl_conv:
        pl_conv[i['Тип кампании']] = [int(i['Конверсия'])]    
    pl_conv[i['Тип кампании']].append(int(i['Конверсия'])) 
 
for i in pl_conv:
    pl_conv[i] = statistics.mean(pl_conv[i])

most_successful_campaign_type = max(pl_conv, key=pl_conv.get)
