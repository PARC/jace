import requests


def question_to_server(question_dict):
    header = {"Content-Type": "application/json"}
    payload = question_dict
    r = requests.post('http://localhost:3000/serviceapi/participants/update/woof', data=payload, header=header)
