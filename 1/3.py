'''
Напишите функцию sub_renewal_by_day, которая принимает на вход путь к файлу с логами и анализирует взаимосвязь дня продления подписки 
и количества продлений в этот день. Функция должна записать в файл weekdays.txt
'''
from datetime import datetime, date
import collections

def sub_renewal_by_day(log_file_path):
    logs_list = []
    with open (log_file_path, 'r') as logs:
        for line in logs:
            logs_list.append(line.split('|'))          
   
    #qnt_update =  {(datetime.strptime(i[1].strip(' '), '%Y-%m-%d %H:%M:%S,%f').date()): int(i[4].split(':')[1]) for i in logs_list if 'количество людей с автопродлением подписки:' in i[4]}
    #print(qnt_update[date(2023, 1, 19)]) # если import datetime, то qnt_update[datetime.date(2023, 1, 19)]
    suc_update = collections.Counter([(datetime.strptime(i[1].strip(' '), '%Y-%m-%d %H:%M:%S,%f').weekday()) for i in logs_list if 'Обновляем подписку пользователю id:' in i[4]])
    unsuc_update_ = collections.Counter([(datetime.strptime(i[1].strip(' '), '%Y-%m-%d %H:%M:%S,%f').weekday()) for i in logs_list if '- ошибка при списании:' in i[4]])
    
   
    days_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']    

    with open('/home/user/Рабочий стол/Создать папку 7/питон/Глава 14/Кейс 1/' + 'weekdays.txt', 'w') as w:
        w.write('Количество обновлений подписки по дням недели:\n')        
        for i, day in enumerate(days_week):
            print(f'{day}: {suc_update[i]-unsuc_update_[i]}', file = w)    

log_file_path = 'auto_purchase.log'
sub_renewal_by_day('auto_purchase.log')
