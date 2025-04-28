'Найдите самый успешный город проведения кампании по средним значениям конверсий'
import csv, statistics
campaign_d = []

with open(campaign_data.csv, 'r') as campaign_data:
    reader = csv.DictReader(campaign_data, delimiter=',', quotechar='"')
    for line in reader:
        campaign_d.append(line)

pl_conv = {}

for i in campaign_d:
    if i['Город'] not in pl_conv:
        pl_conv[i['Город']] = [int(i['Конверсия'])]    
    pl_conv[i['Город']].append(int(i['Конверсия'])) 
 
for i in pl_conv:
    pl_conv[i] = statistics.mean(pl_conv[i])

most_successful_city = max(pl_conv, key=pl_conv.get)