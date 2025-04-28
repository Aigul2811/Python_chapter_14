'''
Ваша задача написать функцию auto_renewal_sub, которая принимает на вход путь к файлу с логами и обрабатывает количество клиентов с автопродлением подписки. 
Мы хотим посмотреть на изменение этого показателя в динамике: посчитайте сглаженные значения с помощью метода скользящего среднего и метода медианного сглаживания.
Примечание: При сглаживании берем все предыдущие значения, включая текущее, будущие значения не берем. Если в один день наблюдаем несколько записей об 
автопродлении - берем максимальное из имеющихся число клиентов с подпиской.
Функция должна записать в файл auto_renewal_sub.txt два списка, предварив их соответствущими обозначениями:
Среднее: [2.0, 1.0, 0.67...]
Медиана: [2, 2, 0...]
'''
from datetime import datetime
import statistics

def auto_renewal_sub(log_file_path):
    logs_list = []
    with open (log_file_path, 'r') as logs:
        lines = logs.readlines()           
        for line in lines:
            logs_list.append(line.split('|'))
   
    filt_logs_list =  [(datetime.strptime(i[1].strip(' '), '%Y-%m-%d %H:%M:%S,%f').date(), i[4].split(':')[1]) for i in logs_list if 'количество людей с автопродлением подписки:' in i[4]]
    
    # Определяем количество дней от начала предложения обновлений до конца
    date_beg = filt_logs_list[0][0]
    date_end = filt_logs_list[-1][0]
    period = int((date_end - date_beg).total_seconds()/86400)

    values = [0 for i in range(period + 1)]
        
    for i in filt_logs_list:
         day = (i[0] - date_beg).days 
         if int(i[-1]) > values[day]:                   
            values[day] = int(i[-1])      
             
    ma = list(map(lambda i: round(sum(values[:i+1])/len(values[:i+1]), 2), range(len(values))))
    med = [int(statistics.median(values[:i+1])) for i in range(len(values))]
    
    with open('/home/user/Рабочий стол/Создать папку 7/питон/Глава 14/Кейс 1/' + 'auto_renewal_sub.txt', 'w') as auto_renewal_sub_file:
        auto_renewal_sub_file.write('Среднее: ')
        print(ma, file = auto_renewal_sub_file)      

        auto_renewal_sub_file.write('Медиана: ')
        print(med, file = auto_renewal_sub_file)

log_file_path = 'auto_purchase.log'
auto_renewal_sub('auto_purchase.log')
