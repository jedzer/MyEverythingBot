import requests
import datetime
import usersGroup
import json
import sqlite3


daysOfTheWeek = {
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6
}

databaseIsUsed = False


def updateDatabase():
    global databaseIsUsed
    while databaseIsUsed:
        pass
    databaseIsUsed = True
    connection = sqlite3.connect("groups.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT date
        FROM lastUpdate
    """)
    lastUpdate = cursor.fetchone()
    cursor.execute("""DELETE FROM groups""")
    cursor.execute("""
        INSERT INTO lastUpdate VALUES (?)
    """, (datetime.datetime.today().day,))
    time = datetime.datetime(2018, 5, 26, 1, 1, 00).hour + 4
    if lastUpdate[0] < datetime.datetime.today().day and time == datetime.datetime.today().hour + 4 or lastUpdate[0] > 29:
        usersGroup.update()
    databaseIsUsed = False


def getFileFromAPI(url):
    return requests.get(url, headers={'User-agent': 'your bot 0.1'})


def setUserGroupNumber(userId, group):
    return usersGroup.setGroup(userId, group)


def getUserGroupNumber(userId):
    return usersGroup.get(userId)


def getWeek():
    return int(datetime.datetime.today().isocalendar()[1] + 2) % 4


def getOneDaySchedule(userId):
    global databaseIsUsed
    while databaseIsUsed:
        pass
    databaseIsUsed = True
    if usersGroup.get(userId):
        group = usersGroup.getJSON(usersGroup.get(userId))
        groupJSON = json.loads(group)
        schedule = ""
        schedule += groupJSON["todayDate"] + "\n"
        for schedules in groupJSON["todaySchedules"]:
            schedule += schedules["lessonTime"] + " " +\
                        schedules["subject"] + " (" + \
                        schedules["lessonType"] + ")\n" + \
                        schedules["employee"][0]["fio"] + "\n"
        databaseIsUsed = False
        return schedule
    databaseIsUsed = False
    return "ERROR"



def getOneWeekSchedule(userId, week):
    global databaseIsUsed
    while databaseIsUsed:
        pass
    databaseIsUsed = True
    if usersGroup.get(userId):
        if datetime.datetime.today().weekday() == 7 - 1:
            week += 1
        group = usersGroup.getJSON(usersGroup.get(userId))
        groupJSON = json.loads(group)
        schedule = ""
        for group in groupJSON["schedules"]:
            schedule += "\n--" + group["weekDay"] + "--\n"
            for subject in group["schedule"]:
                for weekNumber in subject["weekNumber"]:
                    if weekNumber == week:
                        if subject["employee"] != []:
                            tmp = (subject["lessonTime"] + " " +
                                        subject["subject"] + " " +
                                        subject["auditory"][0] + "\n" +
                                        subject["employee"][0]["fio"] + "\n")
                            schedule += tmp
                        else:
                            schedule += (subject["lessonTime"] + " " +
                                        subject["subject"] + "\n")
        databaseIsUsed = False
        return schedule
    else:
        databaseIsUsed = False
        return "ENTER GROUP FIRST!"


def getCurrentWeekSchedule(userId):
    return getOneWeekSchedule(userId, getWeek())

def getExams(userId):
    global databaseIsUsed
    while databaseIsUsed:
        pass
    databaseIsUsed = True
    if usersGroup.get(userId):
        group = usersGroup.getJSON(usersGroup.get(userId))
        groupJSON = json.loads(group)
        schedule = ""
        for group in groupJSON["examSchedules"]:
            schedule += "\n--" + group["weekDay"] + "--\n"
            for subject in group["schedule"]:
                    if subject["employee"] != []:
                        schedule += subject["lessonTime"] + " " + \
                                    subject["subject"] + " " + \
                                    subject["auditory"][0] + "\n" + \
                                    subject["employee"][0]["fio"] + "\n"
                    else:
                        schedule += subject["lessonTime"] + " " + \
                                    subject["subject"] + " " + \
                                    subject["auditory"] + "\n"
        databaseIsUsed = False
        return schedule
    else:
        databaseIsUsed = False
        return "ENTER GROUP FIRST!"