import os
import time

def alarm():
    a = int(input("Init the hours : "))
    b = int(input("the minutes : "))
    c = int(input("and the seconds : "))
    return(a,b,c)

def clock(a, b, c):
    a_hours,b_min,c_sec = alarm()
    i = 0
    os.system('clear')
    while i < 9223372036854775807:
        if c == 59:
            b+=1
            c = 00
        if b == 60:
            a+=1
            b = 00
        if a == 24:
            a = 00
        else:
            c +=1

        print('')

        if a >= a_hours and a >= a_hours and b == b_min and c == c_sec:
            print("0{}:0{}:0{}".format(a, b, c))
            print("\nDRING DRING DRING")
        elif c < 10 and b < 10 and a < 10:
            print("0{}:0{}:0{}".format(a, b, c))
        elif c < 10 and b < 10:
            print("{}:0{}:0{}".format(a, b, c))
        elif c < 10 and a < 10:
            print("0{}:{}:0{}".format(a, b, c))
        elif b < 10 and a < 10:
            print("0{}:0{}:{}".format(a, b, c))
        elif a < 10:
            print("0{}:{}:{}".format(a, b, c))
        elif b < 10:
            print("{}:0{}:{}".format(a, b, c))
        elif c < 10:
            print("{}:{}:0{}".format(a, b, c))
        else:
            print("{}:{}:{}".format(a, b, c))
        
        print('')
        time.sleep(1)
        os.system('clear')
        i+=1

def choose_hour():
    i = 0
    print("set up the clock first : ")
    a = int(input("set the hours up : "))
    if a > 24 and a < 0:
        a = int(input("i dont understand, please retry"))
    b = int(input("set the minutes up : "))
    if b > 60 and b < 0:
        b = int(input("i dont understand, please retry"))
    c = int(input("set the seconds up : "))
    if c > 60 and c < 0:
        c = int(input("i dont understand, please retry"))
    print("and now the alarm : ")
    a_hours,b_min,c_sec = alarm()
    os.system('clear')
    
    while i < 9223372036854775807:
        if c == 59:
            b+=1
            c = 00
        if b == 60:
            a+=1
            b = 00
        if a == 24:
            a = 00
        else:
            c +=1

        print('')
        if a >= a_hours and a >= a_hours and b == b_min and c == c_sec:
            print("0{}:0{}:0{}".format(a, b, c))
            print("\nDRING DRING DRING")
        if c < 10 and b < 10 and a < 10:
            print("0{}:0{}:0{}".format(a, b, c))
        elif c < 10 and b < 10:
            print("{}:0{}:0{}".format(a, b, c))
        elif c < 10 and a < 10:
            print("0{}:{}:0{}".format(a, b, c))
        elif b < 10 and a < 10:
            print("0{}:0{}:{}".format(a, b, c))
        elif a < 10:
            print("0{}:{}:{}".format(a, b, c))
        elif b < 10:
            print("{}:0{}:{}".format(a, b, c))
        elif c < 10:
            print("{}:{}:0{}".format(a, b, c))
        else:
            print("{}:{}:{}".format(a, b, c))
        print('')
        time.sleep(1)
        os.system('clear')
        i+=1


def main():
    timeset = input("Do you want to choose the time ?\n 1) Yes \n 2) No \n")
    if timeset == "1":
        value = input("Do you want to add an alarm ?\n 1) Yes \n 2) No \n")
        if value == "1":
            choose_hour()
        if value == "2":
            choose_hour()
    if timeset == "2":
        value = input("Do you want to add an alarm ?\n 1) Yes \n 2) No \n")
        if value == "1":
            clock(16,30,00)
        if value == "2":
            clock(16,30,00)

main()