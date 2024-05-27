from PyQt5.uic import*
from PyQt5.QtWidgets import*
from random import *

def generatepass(n,c1,c2,c3,c4):
    num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sc=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    choi=["1","2","3","4"]
    choi1=["1","2","3"]
    choi2=["1","2"]
    
    if c1 and c2 and c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(sc)
            if ch=="3":
                password=password+choice(upper)
            if ch=="4":
                password=password+choice(lower)
        return password
        
        
    elif c1 and c2 and c3 and not c4:
        password=""
        for i in range (n):
            ch=choice(choi1)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(sc)
            if ch=="3":
                password=password+choice(upper)
        return password
    elif c1 and c2 and not c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi1)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(sc)
            if ch=="3":
                password=password+choice(lower)
        return password
    elif c1 and c2 and not c3 and not c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(sc)
        return password
    elif c1 and not c2 and c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi1)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(lower)
            if ch=="3":
                password=password+choice(upper)
        return password
    elif c1 and not c2 and c3 and not c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(upper)
        return password
    elif c1 and not c2 and not c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(num)
            if ch=="2":
                password=password+choice(lower)
        return password
    elif c1 and not c2 and not c3 and not c4:
        password=""
        for i in range (n):
            password=password+choice(num)
        return password

    elif not c1 and c2 and c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi1)
            if ch=="1":
                password=password+choice(lower)
            if ch=="2":
                password=password+choice(sc)
            if ch=="3":
                password=password+choice(upper)
        return passowrd
    elif not c1 and c2 and c3 and not c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(sc)
            if ch=="2":
                password=password+choice(upper)
        return password
    elif not c1 and c2 and not c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(lower)
            if ch=="2":
                password=password+choice(sc)
        return password
    elif not c1 and c2 and not c3 and not c4:
        password=""
        for i in range (n):
            password=password+choice(sc)
        return password
    elif not c1 and not c2 and c3 and c4:
        password=""
        for i in range (n):
            ch=choice(choi2)
            if ch=="1":
                password=password+choice(lower)
            if ch=="2":
                password=password+choice(upper)
        return password
    elif not c1 and not c2 and c3 and not c4:
        password=""
        for i in range (n):
            password=password+choice(upper)
        return password
    elif not c1 and not c2 and not c3 and c4:
        password=""
        for i in range (n):
            password=password+choice(lower)
        return password
    else:
        password="check something brother"
        return password





def generate():
    w.T1.clear()
    if w.r1.isChecked() == True:
        n=12
    elif w.r2.isChecked() == True:
        n=14
    elif w.r3.isChecked() == True:
        n=16
    else:
        n=18
    c1=w.c1.isChecked()
    c2=w.c2.isChecked()
    c3=w.c3.isChecked()
    c4=w.c4.isChecked()
    password = generatepass(n,c1,c2,c3,c4)
    w.T1.setText(password)




















































app = QApplication([])
w=loadUi("win.ui") 
w.setWindowTitle("Password Generator By MAH")
w.gbtn.clicked.connect(generate)
w.show()
app.exec_()
