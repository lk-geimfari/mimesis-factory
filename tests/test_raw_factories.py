# -*- coding: utf-8 -*-

import factory

from mimesis_factory import MimesisField


class User(object):
    def __init__(self, uid, email):
        self.uid = uid
        self.email = email


class UserFactory(factory.Factory):
    class Meta:
        model = User

    uid = factory.Sequence(lambda n: n)
    email = MimesisField('email')


def test_direct_factory():
    users = UserFactory.create_batch(10)

    uids = {u.uid for u in users}
    emails = {u.email for u in users}

    assert len(users) == len(emails)
    assert len(users) == len(uids)
