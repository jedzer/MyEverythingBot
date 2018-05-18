class Users:
    users = {}


    def lastMessage(self, userId):
        # isHere = False
        # for k in range(len(self.users)):
        #     if self.users[k] == userId:
        #         isHere = True

        toReturn = self.users[userId]
        # if isHere:
        return toReturn

    def setLastMessage(self, userId, message):
        self.users[userId] = message



