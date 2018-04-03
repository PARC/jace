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

from django.contrib.postgres import fields
from django.db import models

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048
SUPER_LONG = 9000
DBZ_LENGTH = 32365


class Report(models.Model):
    """

    Takes all reports from incoming app
    """
    studyName = models.CharField(max_length=MEDIUM_LENGTH)
    kind = models.CharField(max_length=MEDIUM_LENGTH)
    data = fields.JSONField()
    source = models.CharField(max_length=SHORT_LENGTH)
    def __repr__(self):
        return str(self.data)


