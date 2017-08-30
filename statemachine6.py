
import redis
from durable.lang import *
import os

with ruleset('coach'):

    @when_all(m.timeChange == True)
    def determine_con(c):
        """
        Will activate if it is time for the user to change conditions based on a two week interval
        :return:
        """
        #todo send message to API to turn on each condition randomly
        # question_to_server(
        #     '{"studyId":{},"attribute":"settings.selfAffirmation", "value":""}'.format(
        #         random.choice(c.m.studyID,["yes", "no"])))
        # question_to_server(
        #     '{"studyId":"shszxqlpkw89s98f6","attribute":"settings.implementationIntention", "value":"y{}"}'.format(
        #         random.choice(["yes", "no"])))
        pass
    @when_all(m.timeChange == False)
    def turn_on_reminders(c):
        """
        Will activate if the number of lack responces is greater than 3.
        :return:
        """
        #todo send message to API to turn on reminders
        # question_to_server(question_to_server(
        #     '{"studyId":"shszxqlpkw89s98f6","attribute":"settings.selfCompassion", "value":"y{}"}'.format(
        #         random.choice(["yes", "no"]))))
        print("hello")


    @when_start
    def start(host):
        for i in range(3):
            host.post('coach',{"timeChange":False})




if __name__ == '__main__':
    """
    This runs the program. Perhaps. copy over to API to start it for each case?
    """
    redis.StrictRedis(host=os.environ['REDIS'].split(':')[0], port=os.environ['REDIS'].split(':')[1]).flushall()
    #redis.StrictRedis(port=32768).flushall()
    #run_all([{'host': "localhost", 'port':32768}],port=2000,host_name="localhost")
    run_all([{'host': 'docker.for.mac.localhost', 'port': 32768}],host_name="docker.for.mac.localhost"); #c command can't bbbe done using split

