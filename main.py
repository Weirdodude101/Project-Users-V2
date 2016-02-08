from components import yaml
from components import Localizer
from components.Objects import *
import sys
import os
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
        print "Invalid option, heading back to start"
        print "-------------------------------------"
        startMenu()

def createAccount():
    print "Welcome to create an account!"
    print "You will need to enter some information"
    username = raw_input("Enter a username: ")
    password = raw_input("Enter a password: ")
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")
    age = raw_input("Enter your age: ")
    gender = raw_input("Enter your gender: ")
    hobby = raw_input("Enter your hobby: ")
    x = loadYaml("people/personNumber.yaml")
    newUser = Person(username, password, fname, lname, age, gender, hobby)
    personDict[x["next"]] = newUser.getInfo()
    createYaml("people/person_" + str(x["next"]) + ".yaml",x["next"])
    x["next"] += 1
    xDict = dict(
        next = x["next"]
    )
    dumpYaml("people/personNumber.yaml",xDict)
    clearConsole()
    startMenu()

def dumpYaml(filepath, option):
    with open(filepath, 'w') as outfile:
        newAttb = outfile.write(yaml.dump(option,default_flow_style=False) )
    return newAttb

def loadYaml(filepath):
    with open(filepath, "r") as file_descriptor:
        personInfo = yaml.load(file_descriptor)
    return personInfo

def createYaml(filepath, number):
    with open(filepath, 'w') as outfile:
        newAcc = outfile.write(yaml.dump(personDict[number],default_flow_style=False) )
    return newAcc

def clearConsole():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
clearConsole()
startMenu()