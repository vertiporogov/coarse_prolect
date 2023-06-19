import json
import datetime

def load_json_file(file_name):
    '''

    :param file_name:
    :return:
    '''
    with open(file_name, "r", encoding="utf-8") as file:
        operations_file_list = json.load(file)

    return operations_file_list

def five_last_operations(operations_list):
    '''

    :param operations_list:
    :return:
    '''
    five_operation_list = []
    for i in operations_list:
        if i["state"] == "EXECUTED":
            five_operation_list.append(i)

        five_operation_list = sorted(five_operation_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)

        return five_operation_list[-5:]


def output_information()