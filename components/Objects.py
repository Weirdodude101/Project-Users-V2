import Localizer

class Person:
    def __init__(self,username,password,fname,lname,age,gender,hobby):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.hobby = hobby

    def getInfo(self):
        infoDict = {
            "Username": self.username,
            "Password": self.password,
            "FirstName": self.fname,
            "LastName": self.lname,
            "Age": self.age,
            "Gender": self.gender,
            "Hobby": self.hobby
        }
        return infoDict