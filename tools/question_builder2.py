'''
*************************************************************************
*
*  © [2018] PARC Inc., A Xerox Company
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Xerox Corporation.
* The intellectual and technical concepts contained
* herein are proprietary to PARC Inc. and Xerox Corp.,
* and may be covered by U.S. and Foreign Patents,
* patents in process, and may be protected by copyright law.
* This file is subject to the terms and conditions defined in
* file 'LICENSE.md', which is part of this source code package.
*
**************************************************************************
'''


import json
from collections import OrderedDict
import random
import pprint as pp


class question():

    def __init__(self,text,responce_format,tag,choices):
        self.text = text
        self.responce_format = responce_format
        self.tag = tag
        self.choices = choices
    def dtize(self):
        return {"text":self.text,"responceFormat":self.responce_format,"tag":self.tag,"choices":self.choices}


class question_list():
    def __init__(self,name,attribute,value,askdate,asktime,expiredate,expiretime,sequencebase,questions):
        self.name = name
        self.attribute = attribute
        self.value = value
        self.askdate = askdate
        self.asktime = asktime
        self.expiredate = expiredate
        self.expiretime = expiretime
        self.seqeuncebase = sequencebase
        self.questions = questions
    def jsonize(self):
        constraints = [{"attribute":self.attribute,"value":self.value}]
        data = {"sequences":[{"name":self.name,"constraints":constraints,"sequenceBase":self.seqeuncebase,"askDate":self.askdate,"askTime":self.asktime,
                              "expireDate":self.expiredate,"expireTime":self.expiretime,"questions":self.questions}]}
        json_str = json.dumps(data, sort_keys=True)
        return data



# def quistion(name,attribute,value,askdate,asktime,expireDate,ExpireTime,sequenceBase,link_to_activity,tag,q_type,text,
#              choices): # Generates Q
#     name = name
#     constraints = [{"attribute": attribute, "value": value}]
#     data = {"sequences": [{"name": name, "constraints": constraints, "askDate": askdate,
#                            "askTime": asktime,
#                            "expireDate": expireDate,
#                            "expireTime": ExpireTime, "sequenceBase": sequenceBase,
#                            "linkToActivity": link_to_activity, "quistions": {"tag": tag,"text": text,
#                                                                              "responseFormat": q_type,
#                                                                              "choices": choices}}]}
#     json_str = json.dumps(data, sort_keys=True)
#     return data
#
#
# class quistion_obj():
#
#     #makes a quistion json object
#     def __init__(self,name, attribute, value, askdate, asktime, expireDate, ExpireTime, sequenceBase, link_to_activity, tag,
#                  q_type, text, choices):
#
#         self.name = name
#         self.attribute = attribute
#         self.value = value
#         self.askdate = askdate
#         self.asktime = asktime
#         self.expireDate = expireDate
#         self.ExpireTime = ExpireTime
#         self.sequenceBase = sequenceBase
#         self.link_to_activity = link_to_activity
#         self.tag = tag
#         self.q_type = q_type
#         self.text = text
#         self.choices = choices
#
#     #########
#     #
#     #######
#     def jsonize(self):  # Generates Q
#         constraints = [{"attribute": self.attribute, "value": self.value}]
#         data = {"sequences": [{"name": self.name, "constraints": constraints, "askDate": self.askdate,
#                                "askTime": self.asktime,
#                                "expireDate": self.expireDate,
#                                "expireTime": self.ExpireTime, "sequenceBase": self.sequenceBase,
#                                "linkToActivity": self.link_to_activity, "quistions": {"tag": self.tag, "text": self.text,
#                                                                                  "responseFormat": self.q_type,
#                                                                                  "choices": self.choices}}]}
#         json_str = json.dumps(data, sort_keys=True)
#         return data
#
#
if __name__ in "__main__":
    self_aff_eat_1 = "Research shows that  having a positive self-image is important to making healthy lifestyle changes"
    selfaff_eat_2 = "I’m going to ask you to use a tool called a self-affirmation for the eat slower program"
    selfaff_eat3 = "Here’s how it works. A self-affirmation means taking a bit of time to  think positively about your " \
                   "past successes, things that are important to you, your  values, or what you stand for."
    selfaff_eat4 = "Use a self-affirmation in situations that diminishes your motivation or threatens your self-image"
    selfaff_eat5 = "It helps to make tiny plans to do your self-affirmations using statements of the form: “IF situation" \
                   " X is encountered THEN I will do a self-affirmation"
    selfaff_eat6 = "The “IF” part is a specific situation that  diminishes your motivation or threatens your self-image" \
                   " The “THEN” part is  a specific self affirmation"
    list_self_aff = [self_aff_eat_1,selfaff_eat_2,selfaff_eat3,selfaff_eat4,selfaff_eat5,selfaff_eat6]
    list_self_aff = [question(text=item,responce_format="list-choose-one",tag=i,choices="Okay").dtize() for i,item in enumerate(list_self_aff)]
    print(list_self_aff)
    grouping = [question_list(name="SA",attribute="SA",value=True,askdate=i,asktime="10:00",expiredate="200",
                             expiretime="23:59",sequencebase=200,questions=list_self_aff).jsonize() for i in range(102) if i % 14 ==0]


    with open('q.json','w') as outfile:
        json.dump(grouping, outfile)
    pp.pprint (grouping)



