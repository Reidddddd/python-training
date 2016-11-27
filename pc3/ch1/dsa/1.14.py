"""
Sorting Objects Without Native Comparsion Support
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(sorted(users, key=lambda u: u.user_id))
print(users)
print()

users = [User(23), User(3), User(99), User(44)]
print(sorted(users, key=attrgetter('user_id')))
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
