import Localizer

class Person:
    def __init__(self,username,password,fname,lname,age,gender,hobby,desc):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.hobby = hobby
        self.desc = desc

    def getInfo(self):
        infoDict = {
            "Username": self.username,
            "Password": self.password,
            "FirstName": self.fname,
            "LastName": self.lname,
            "Age": self.age,
            "Gender": self.gender,
            "Hobby": self.hobby,
            "Description": self.desc
        }
        return infoDict