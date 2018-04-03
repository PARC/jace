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


import requests
import random

"""
controls the
"""
def question_to_server(question_dict):
    header = {"Content-Type": "application/json"}
    payload = question_dict
    r = requests.post('http://localhost:3000/serviceapi/participants/update/woof', data=payload,
                      header=header)  # set this to wherever the app is located

def change_condition(studyId,attribute,value):
    header = {"Content-Type": "application/json"}
    payload = {"studyId":studyId,"attribute":attribute,"value":value}
    r = requests.post('http://docker.for.mac.localhost:3000/serviceapi/participants/update/woof',
                      json=payload)  #set this to whereever the app is located
    print(r)
