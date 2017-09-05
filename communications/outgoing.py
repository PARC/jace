import requests


def question_to_server(question_dict):
    header = {"Content-Type": "application/json"}
    payload = question_dict
    r = requests.post('http://localhost:3000/serviceapi/participants/update/woof', data=payload, header=header)

def change_condition(condittion):
    header = {"Content-Type": "application/json"}
    payload = condittion
    r = requests.post('http://localhost:3000/serviceapi/participants/update/woof', json=payload)
    print(r.reason)

Data={"studyId":"BLeJvi5jc2fhPT77N","attribute": "selfAffirmation","value": "yes"}

#change_condition(Data)




