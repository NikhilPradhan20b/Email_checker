## This project is made to check whether the format of the email is correct or not.

import string

email = input("Enter your email: ")
def checkmail(email):
    index = email.find("@")
    if(index < 0):
        print("Wrong Email. There is no @")
        return
    index2 = email.find(".")
    if(index2 < index):
        print("Wrong Email. . Before @")
        return
    if(index + 1 == index2):
        print("Wrong Email. There is no domain name")
        return
    if not '.com' in email:
        print("Wrong Email. There is no domain")
        return
    if ' ' in email:
        print("Wrong Email. There is an empty space")
        return
    if not email.islower():
        print("Wrong Email. There is an Uppercase Letter")
        return
    print("Correct email")


checkmail(email)


    