import smtplib
import random
import bcrypt
import re

def check(s):
    if not re.search('[A-Z]', s):
       print("Please mention atleast one Upper Case")
       return False
    elif not re.search('[a-z]', s):
       print("Please mention atleast one Lower Case")
       return False
    elif not re.search('[0-9]', s):
       print("Please mention atleast one digit")
       return False
    elif not re.search('[!@#$%^&*]', s):
       print("Please mention atleast one special character")
       return False
    elif  len(s) < 8:
       print("Password should be atleast 8 characters") 
    else: return True


def check_email(s):
    return re.match('[a-z.0-9]{3,}@[a-z]{2,}\.(com|in)', s)


def otpgen():
    s = ""
    for i in range(0, 7):
        s+= str(random.randint(0, 9))
    return s


def otpgen():
    s = ""
    for i in range(0, 7):
        s+= str(random.randint(0, 9))
    s = int(s)
    return s


def send(rec, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    pas = open(r'E:\pre-intern-training\python_trn\pwd.txt', 'r').read()
    s.login('yacobtalla@gmail.com', pas)
    s.sendmail('yacobtalla@gmail.com', rec, msg)
    s.quit()