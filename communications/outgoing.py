import requests


def question_to_server(question_dict):
    header = {"Content-Type": "application/json"}
    payload = question_dict
    r = requests.post('http://localhost:3000/serviceapi/participants/update/woof', data=payload, header=header)

def change_condition(studyId,attribute,value):
    header = {"Content-Type": "application/json"}
    payload = {"studyId":studyId,"attribute":attribute,"value":value}
    r = requests.post('http://localhost:3000/serviceapi/participants/update/:token', json=payload)
    print(r)

Data={"studyId":"1234","attribute": "settings.implementationIntention","value": "yes"}
Data2={"studyId":"1234","attribute": "settings.selfAffirmation","value": "no"}
Data3={"studyId":"1234","attribute": "settings.control","value": "no"}
change_condition("1234","settings.implementationIntention","yes")




