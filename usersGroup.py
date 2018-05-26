import sqlite3
import requests


def update():
    connection = sqlite3.connect("groups.db")
    cursor = connection.cursor()
    groups = requests.get("https://students.bsuir.by/api/v1/groups", headers={'User-agent': 'your bot 0.1'})
    groupsJSON = groups.json()
    cursor.execute("""DELETE FROM groups""")
    i = 0
    toInsert = []
    for group in groupsJSON:
        json = requests.get("https://students.bsuir.by/api/v1/studentGroup/schedule.json?studentGroup=" + group["name"], headers={'User-agent': 'your bot 0.1'})
        toInsert = (i, group["name"], json.text)
        i += 1
        cursor.execute("INSERT INTO groups VALUES (?,?,?)", toInsert)
        connection.commit()
        print(i)
    connection.close()
    print("DONE")


def get(userId):
    connection = sqlite3.connect("groups.db")
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT selectedGroup
                    FROM users
                    WHERE userID = ?
    """, (userId,))
    userGroupData = cursor.fetchone()
    connection.close()
    if userGroupData:
        return userGroupData[0]
    return "NULL"


def setGroup(userId, group):
    connection = sqlite3.connect("groups.db")
    cursor = connection.cursor()
    cursor.execute("SELECT groupName FROM groups WHERE groupName = ?", (group, ))
    exists = cursor.fetchone()
    if exists:
        toInsert = [(userId, group)]
        cursor.execute("DELETE FROM users WHERE userID=?", (userId, ))
        connection.commit()
        cursor.executemany("INSERT INTO users VALUES(?,?)", toInsert)
        connection.commit()
        connection.close()
        return "Added"
    connection.close()
    return "Error, no such group!"


def getJSON(group):
    connection = sqlite3.connect("groups.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT schedule
                    FROM groups
                    WHERE groupName = ?
                   """, (group,))
    return cursor.fetchone()[0]


