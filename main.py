import requests


def request_processing(todos_data, users_data):
    for i in todos_data:
        print(i)


if __name__ == '__main__':

    todos_data = requests.get("https://json.medrocket.ru/todos").json()
    users_data = requests.get("https://json.medrocket.ru/users").json()
    request_processing(todos_data, users_data)
