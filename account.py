import datetime
import random


class Account(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.password = ''.join(str(random.randint(0, 10)) for _ in range(10))
        self.date_joined = datetime.datetime.today()

    def __str__(self):
        return '{} ({})'.format(self.username, self.email)
