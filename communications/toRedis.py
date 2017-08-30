import requests

def post_to_redis(value):
    payload = {"timeChange":value}
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:2000/coach/events/2',json=payload,headers=headers)
    print(r.json())
    r.close()

post_to_redis(False)
