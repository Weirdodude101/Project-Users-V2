from components import yaml
from components import Localizer
from components.Objects import *
import sys
import os
import os.path
peopleData = Localizer.peopleDatabase

personDict = {
}
"""
    TODO:
         - Finish create account
         - Add Find account
         - Add Login account
         - Add admin console
         - Add yaml creator
         - FINALLY (After all is done):
             - Clean up code to the best of my ability
"""

if sys.platform == "win32":
	os.system("title Project Users")
	os.system("cls")
else:
	sys.stdout.write("\x1b]2;Project User\x07")
	os.system("clear")

def setPeople(name):
    numPeople = getNumPeople()
    if numPeople < 0:
        print 'Less than 0 people'
        return None
    else:
        for x in range(0,numPeople):
            person = loadYaml(peopleData + name + ".yaml")
            personDict[person["Username"]] = {
                "Username": person["Username"],
                "Password": person["Password"],
                "FirstName": person["FirstName"],
                "LastName": person["LastName"],
                "Age": person["Age"],
                "Gender": person["Gender"],
                "Hobby": person["Hobby"]
            }

def startMenu():
    clearConsole()
    print "Welcome to Project Users V2"
    print "1: Create an account"
    print "2: Find an account"
    print "3: Login to your account"
    print "4: Login to the admin console"
    option = raw_input("Enter here: ")
    if option == "1": createAccount()
    if option == "2": findAccount()
    if option == "3": loginAccount()
    if option == "4": adminConsole()
    if option != "1" or option != "2" or option != "3" or option != "4":
        clearConsole()
        print "Invalid option, heading back to start"
        print "-------------------------------------"
        startMenu()

def createAccount():
    clearConsole()
    print "Welcome to create an account!"
    print "You will need to enter some information"
    username = raw_input("Enter a username: ")
    password = raw_input("Enter a password: ")
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")
    age = raw_input("Enter your age: ")
    gender = raw_input("Enter your gender: ")
    hobby = raw_input("Enter your hobby: ")
    newUser = Person(username, password, fname, lname, age, gender, hobby)
    personDict[username] = newUser.getInfo()
    createYaml("people/person_" + username + ".yaml",username)
    clearConsole()
    startMenu()

def findAccount():
    clearConsole()
    print "Find a person"
    print "--------------------"
    name = raw_input("Enter the persons username: ")
    setPeople(name)
    person = personDict[name]
    printInfo(person)
    print "1: Find another person"
    print "2: Create an account"
    print "3: Go back to start"
    option = raw_input("Enter here: ")
    if option == "1": findAccount()
    if option == "2": createAccount()
    if option == "3": startMenu()
    if option != "1" or option != "2" or option != "3":
        clearConsole()
        print "Invalid option, heading back to start"
        print "-------------------------------------"
        startMenu()

def printInfo(person):
    clearConsole()
    print "Information for user: " + person["Username"]
    print "############################"
    print "Username: " + person["Username"]
    print "Password: " + person["Password"]
    print "First name: " + person["FirstName"]
    print "Last name: " + person["LastName"]
    print "Age: " + person["Age"]
    print "Gender: " + person["Gender"]
    print "############################"

def getNumPeople():
    path = 'people/'
    num_files = len([f for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))])
    return num_files

def dumpYaml(filepath, option):
    with open(filepath, 'w') as outfile:
        newAttb = outfile.write(yaml.dump(option,default_flow_style=False) )
    return newAttb

def loadYaml(filepath):
    with open(filepath, "r") as file_descriptor:
        personInfo = yaml.load(file_descriptor)
    return personInfo

def createYaml(filepath,username):
    with open(filepath, 'w') as outfile:
        newAcc = outfile.write(yaml.dump(personDict[username],default_flow_style=False) )
    return newAcc

def clearConsole():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
clearConsole()
startMenu()