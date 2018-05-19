users = {}


def get(userId):
    return users.get(int(userId))


def set(userId, group):
    users.setdefault(int(userId), group)
