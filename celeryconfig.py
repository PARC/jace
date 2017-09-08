broker_url = 'pyamqp://guest@localhost:32771//'
result_backend = 'rpc://guest@localhost:32772'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True
task_routes = {
    'tasks.add': 'low-priority',
}
beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
