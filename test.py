from durable.lang import *
with ruleset('test'):
    @when_all(m.subject == 'World')
    def say_hello(c):
        print ('Hello {0}'.format(c.m.subject))

    @when_start
    def start(host):
        host.post('test', {'subject': 'World'})

run_all([{'host': 'docker.for.mac.localhost', 'port': 32768}], port=32768)