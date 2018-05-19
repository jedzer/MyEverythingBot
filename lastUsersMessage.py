class Users:
    usersLastMessage = {}

    def lastMessage(self, userId):
        toReturn = self.usersLastMessage[userId]
        return toReturn

    def setLastMessage(self, userId, message):
        self.usersLastMessage[userId] = message
