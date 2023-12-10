import requests
from termcolor import colored
import json
from tabulate import tabulate


def paint_text(text, color):
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text


def make_get_request(url):
    try:
        r = requests.get(url)
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        raise e


def wrap_in_list(obj):
    if isinstance(obj, dict):
        return [obj]
    elif isinstance(obj, list):
        return obj


def api_data_to_type(data, type='original'):
    wrapped_data = wrap_in_list(data)
    result = ''

    if type == 'original':
        result = '\n' + str(wrapped_data) + '\n'
    elif type == 'list':
        for obj in wrapped_data:
            result += '\n' + json.dumps(obj, indent=4) + '\n'
    elif type == 'table':
        result_dict = {}
        for d in wrapped_data:
            for key, value in d.items():
                if key not in result_dict:
                    result_dict[key] = []
                result_dict[key].append(value)
        result = '\n' + tabulate(result_dict, headers="keys") + '\n'

    return result


def api_data_to_type_painted(data, type='original', color='green'):
    result = api_data_to_type(data, type)
    painted = paint_text(result, color)

    return painted


def text_file_saver(filename, text):
    with open(filename, "w") as file:
        file.write(text)
    print(f"text  was saved into {filename}")


def json_file_saver(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"json  was saved into {filename}")
