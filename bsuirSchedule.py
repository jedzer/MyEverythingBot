import requests
import datetime

usersGroupNumber = {}
userSchedule = {}
daysOfTheWeek = {"Понедельник":1, "Вторник":2, "Среда":3, "Четверг":4, "Пятница":5, "Суббота":6}


def getFileFromAPI(url):
    return requests.get(url, headers={'User-agent': 'your bot 0.1'})

def setUserGroupNumber(userId, group):
    if checkIfGroupExists(group):
        usersGroupNumber[userId] = group
        return "--ADDED--"
    return "--NO SUCH GROUP--"

def getUserGroupNumber(userId):
    return usersGroupNumber[userId]


def checkIfGroupExists(groupNumber):
    groups = getFileFromAPI("https://students.bsuir.by/api/v1/groups")
    groupsJSON = groups.json()
    if groupNumber == None:
        return False
    for group in groupsJSON:
        if group["name"] == groupNumber:
            return True
    return False

def getWeek():
    return int(datetime.datetime.today().isocalendar()[1] + 2) % 4


def getOneDaySchedule(userId):
    if usersGroupNumber.get(userId):
        if checkIfGroupExists(usersGroupNumber[userId]):
            week = getWeek()
            group = getFileFromAPI("https://students.bsuir.by/api/v1/studentGroup/schedule.json?studentGroup=" + usersGroupNumber[userId])
            groupJSON = group.json()
            schedule = ""
            for group in groupJSON["schedules"]:
                if daysOfTheWeek[group["weekDay"]] == datetime.datetime.today().weekday() + 1:
                    schedule += "\n--" + group["weekDay"] + "--\n"
                    for subject in group["schedule"]:
                        for weekNumber in subject["weekNumber"]:
                            if weekNumber == week:
                                if subject["employee"] != []:
                                    schedule += subject["lessonTime"] + " " + \
                                                subject["subject"] + " " + \
                                                subject["auditory"][0] + "\n" + \
                                                subject["employee"][0]["fio"] + "\n"
                                else:
                                    schedule += subject["lessonTime"] + " " + \
                                                subject["subject"] + "\n"
            return schedule
        else:
            return "ERROR. No group: " + usersGroupNumber[userId]
    else:
        return "ENTER GROUP FIRST!"


def getOneWeekSchedule(userId, week):
    if usersGroupNumber.get(userId):
        if datetime.datetime.today().weekday() == 7 - 1:
            week += 1
        group = getFileFromAPI("https://students.bsuir.by/api/v1/studentGroup/schedule.json?studentGroup=" + usersGroupNumber[userId])
        groupJSON = group.json()
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
    if usersGroupNumber.get(userId):
        group = getFileFromAPI("https://students.bsuir.by/api/v1/studentGroup/schedule.json?studentGroup=" + usersGroupNumber[userId])
        groupJSON = group.json()
        schedule = ""
        for group in groupJSON["examSchedules"]:
            schedule += "\n--" + group["weekDay"] + "--\n"
            for subject in group["schedule"]:
                    if subject["employee"] != []:
                        schedule += subject["lessonTime"] + " " + \
                                    subject["subject"] + " " + \
                                    subject["auditory"] + "\n" + \
                                    subject["employee"][0]["fio"] + "\n"
                    else:
                        schedule += subject["lessonTime"] + " " + \
                                    subject["subject"] + " " + \
                                    subject["auditory"] + "\n"
        return schedule
    else:
        return "ENTER GROUP FIRST!"