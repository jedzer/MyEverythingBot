class Users:
    users = {}

    def lastMessage(self, userId):
        toReturn = self.users[userId]
        return toReturn

    def setLastMessage(self, userId, message):
        self.users[userId] = message
