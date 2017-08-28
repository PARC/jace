import requests

def post_to_redis(question_dict):
    payload = question_dict
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:5000/coach/events/20',json=payload,headers=headers)
    print(r.json())
    r.close()

