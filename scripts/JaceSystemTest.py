import requests
from user_model.rules import upkeep
from user_model.models import User

"""

need to clear django



To get task for a person for a date: /serviceapi/taskDone/:userId/:scheduledDate/:token


[11:56]
Need API to time travel


[11:59]
To get questions for that day: Not implemented: Should look like: /serviceApi/questionsDone/:studyId/:scheduledDate/:token


[12:01]
Need API to set answers for a person on a day
"""
number_of_days = 98
for day in range(number_of_days):
    # start of day:
    for user in User.objects.all():
        date = day
        userId = user.userId
        studyId = user.studyId
        r = requests.get('localhost:3000/serviceapi/taskDone/{userId}/{date}/woof')
        r.json()
        # modify r
        r = requests.post('localhost:3000/serviceapi/taskDone/{userId}/{date}/woof', json=r)
        r = requests.get('localhost:3000/serviceApi/questionsDone/{studyId}/{date}/woof')


    # get question, and answer it
    # answer task
    # get question, answer it
    upkeep()
