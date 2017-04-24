#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 排序不支持原生比较的对象


class User:
    def __init__(self, user_id, name=''):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


def sort_users():
    users = [User(23), User(3), User(99)]
    from operator import attrgetter
    print sorted(users, key=attrgetter('user_id', 'name'))


sort_users()
