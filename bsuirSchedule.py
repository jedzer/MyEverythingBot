import requests
import datetime
import usersGroup
import json
import time
from threading import Thread

daysOfTheWeek = {"Понедельник":1, "Вторник":2, "Среда":3, "Четверг":4, "Пятница":5, "Суббота":6}


def init():
    Thread(target=updateDatabase).start()


def updateDatabase():
    lastUpdate = datetime.datetime.today().day - 1
    while True:
        if lastUpdate < datetime.datetime.today().day:
            usersGroup.update()
            lastUpdate = datetime.datetime.today().day


def getFileFromAPI(url):
    return requests.get(url, headers={'User-agent': 'your bot 0.1'})


def setUserGroupNumber(userId, group):
    return usersGroup.setGroup(userId, group)


def getUserGroupNumber(userId):
    return usersGroup.get(userId)


def getWeek():
    return int(datetime.datetime.today().isocalendar()[1] + 2) % 4


def getOneDaySchedule(userId):
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
        return schedule
    return "ERROR"



def getOneWeekSchedule(userId, week):
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
        return schedule
    else:
        return "ENTER GROUP FIRST!"


def getCurrentWeekSchedule(userId):
    return getOneWeekSchedule(userId, getWeek())

def getExams(userId):
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
        return schedule
    else:
        return "ENTER GROUP FIRST!"