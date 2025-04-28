'''
Ваша задача написать функцию count_success_and_failure, которая принимает на вход путь к файлу с логами и подсчитывает количество успешных продлений и ошибок при списании. 
Функция должна вернуть кортеж из двух значений: количества успешных попыток и неуспешных.
'''
def count_success_and_failure(file_path):
    logs_list = []
    with open (file_path, 'r') as logs:
        lines = logs.readlines()            
        for line in lines:
            logs_list.append(line.split('|'))

    cnt_failure = len(list(filter(lambda x: 'ошибка при списании' in x[4], logs_list)))
    cnt_success = len(list(filter(lambda x: 'payment_method_id:' in x[4], logs_list))) - cnt_failure
    res = (cnt_success, cnt_failure)
    return res

file_path = 'auto_purchase.log'
print(count_success_and_failure('auto_purchase.log'))
