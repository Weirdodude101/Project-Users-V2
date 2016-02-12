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
         - Finish Login account
         - Add admin console
         - FINALLY (After all is done):
             - Clean up code to the best of my ability
"""

if sys.platform == "win32":
	os.system("title Project Users")
	os.system("cls")
else:
	sys.stdout.write("\x1b]2;Project User\x07")
	os.system("clear")

def startMenu():
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
        topText("Invalid option, heading back to start")
        startMenu()

def createAccount():
    topText("Welcome to create an account! Enter some information")
    username = raw_input("Enter a username: ")
    password = raw_input("Enter a password: ")
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")
    age = raw_input("Enter your age: ")
    gender = raw_input("Enter your gender: ")
    hobby = raw_input("Enter your hobby: ")
    desc = raw_input("Enter your description: ")
    newUser = Person(username, password, fname, lname, age, gender, hobby, desc)
    personDict[username] = newUser.getInfo()
    createYaml("people/person_" + username + ".yaml",username)
    topText("Successfully created an account")
    startMenu()

def findAccount():
    topText("Find a Person")
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
    if option == "3":
        clearConsole()
        startMenu()
    if option != "1" or option != "2" or option != "3":
        topText("Invalid option, heading back to start")
        startMenu()

def loginAccount():
    topText("Login with your credentials")
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    setPeople(username)
    person = personDict[username]
    if username == person["Username"] and password == person["Password"]:
        person["loggedIn"] = True
        loggedIn(person)
    else:
        topText("Invalid account, heading back to start")
        startMenu()

def loggedIn(person):
    if person["loggedIn"] == False:
        topText("This account is not logged in")
        startMenu()

    topText("Successfully Logged in")
    print "1: Edit your account"
    print "2: Logout"
    option = raw_input("Enter here: ")
    if option == "1": editAccount(person)
    if option == "2": logout(person)
    if option != "1" or option != "2":
        topText("Invalid option, heading back to account page")
        loggedIn(person)

def editAccount(person):
    topText("Choose an option")
    print "1: Change password"
    print "2: Change description"
    option = raw_input("Enter here: ")
    if option == "1": changeInfo(person,"Password",True)
    if option == "2": changeInfo(person,"Description",True)
    if option == "3": loggedIn(person)
    if option != "1" or option != "2" or option != "3":
        topText("Invalid option, heading back to account page")
        loggedIn(person)

def changeInfo(person, attrb, fromLoginPage):
    topText("Enter a new " + attrb.lower())
    newInfo = raw_input("Enter here: ")
    person[attrb] = newInfo
    dumpYaml("people/person_" + person["Username"] + ".yaml",personDict[person["Username"]])
    topText("Successfully changed your " + attrb.lower() + ", Heading back to previous page")
    if fromLoginPage == True:
        loggedIn(person)
    else:
        pass


def logout(person):
    person["loggedIn"] = False
    topText("Successfully signed out, heading back to start")
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
    print "Desc: " + person["Description"]
    print "############################"

def setPeople(name):
    path = os.path.isfile(peopleData + name + ".yaml")
    if not path:
        topText("Invalid account, heading back to start")
        startMenu()
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
                "Hobby": person["Hobby"],
                "Description": person["Description"],
                "loggedIn": False
            }

def topText(msg):
    clearConsole()
    print (msg)
    print "----------------------------"

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