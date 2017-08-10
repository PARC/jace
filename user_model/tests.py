

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import *

class QuestionModelTests(TestCase):

    def test_modulo(self):
        """
        tests if given a date that is not every two weeks it returns false
        """
        time = timezone.now() + datetime.timedelta(days=30)
        non_twoweek= User(identifier="Joel",language="ENG",uuid="12345",timestamp=timezone.now(),deletedIndicator=False,
                          startdate=0,Days_since_start=17,Days_since_last_report=2)
        is_twoweek =  u = User(identifier="Joel",language="ENG",uuid="12345",timestamp=timezone.now(),deletedIndicator=False,
                               startdate=0,Days_since_start=14,Days_since_last_report=2)
        self.assertIs(non_twoweek.was_published_recently(), False)
        self.assertIs(non_twoweek.was_published_recently(), True)
