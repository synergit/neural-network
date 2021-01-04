class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'imagepath'):
            setattr(self, field, kwargs.get(field, None))