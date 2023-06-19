from json import load
import datetime

def load_json_file(file_name):
    '''

    :param file_name:
    :return:
    '''
    with open(file_name, "r", encoding="utf-8") as file:
        operations_file_list = load(file)

    return operations_file_list

def five_last_operations(operations_list):
    '''

    :param operations_list:
    :return:
    '''
    five_operation_list = []
    for i in operations_list:
        if 'date' in i and 'state' in i and 'from' in i and i['state'] == 'EXECUTED':
            five_operation_list.append(i)

    five_operation_list = sorted(five_operation_list, key=lambda d: d['date'])[-5:]
    return sorted(five_operation_list, key=lambda d: d['date'], reverse=True)



def output_information(operations_list):
    '''

    :param operations_list:
    :return:
    '''
    information_str = ''
    for i in operations_list:
        data = i['date']
        description = i['description']

        account = i['from'].split()[-1]
        hidden = account[0:4] + ' ' + account[4:6] + '**' + ' ****' + ' ' + account[-5:-1]
        operation_from = ' '.join(i['from'].split()[0:-1]) + ' ' + hidden
        operation_to = i['to'].split()[0].strip() + ' **' + i['to'][-5:-1]

        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']

        information_str += data + ' ' + description + '\n'
        information_str += operation_from + ' -> ' + operation_to + '\n'
        information_str += amount + ' ' + currency + '\n' * 2

    return information_str

