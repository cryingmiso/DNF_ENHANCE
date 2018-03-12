#-*- coding: utf8 -*-

import random
import os

enhan_cost = [314280, 314280, 314280, 314280, 628560, 691416, 754272, 817128, 879984, 942840, 942840, 1571400, 2547000,
              4129000, 8568000]
enhan_per = [100, 100, 100, 100, 80, 70, 60, 50, 40, 30, 25.9, 18, 9.2, 5.4, 2.1]
enhan_name = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

usr_enhan = enhan_name[0]
total_cost = 0

def enhan_tem(usr_enhan, total_cost):
    print("--"*10)
    now_cost = enhan_cost[usr_enhan]
    now_per = enhan_per[usr_enhan]
    usr_rand = random.randrange(0,101)
    total_cost += now_cost
    if usr_rand <= now_per:
        print("Enhance Success!!")
        usr_enhan += 1
    else:
        print("Enhance Fail...")
        if usr_enhan >= 12:
            print("Broken Item")
            total_cost += 80000000
            usr_enhan = 0
        elif usr_enhan >= 10:
            print("Lower Enhance -3")
            usr_enhan -= 3
        else:
            usr_enhan += 0
    print("--" * 10)
    return usr_enhan, total_cost


os.system("clear")
print("1. Auto Enhance")
print("2. Enhance")
print("Select Number")
usr_input = input(">>")
os.system("clear")
if int(usr_input) == 1:
    while 1:
        usr_auto = input("Set Enhance Number [0 ~ 15] >>")
        if int(usr_auto) in enhan_name:
            while 1:
                usr_enhan, total_cost = enhan_tem(usr_enhan, total_cost)
                os.system("clear")
                if usr_enhan == int(usr_auto):
                    print("User Set Enhance = +" + str(usr_auto))
                    print("Final Enhance = +" + str(usr_enhan))
                    print("Total Cost [Gold] = " + str(total_cost))
                    usr_cash = round(total_cost / 8000000, 4)
                    print("[Gold] -> [Cash] = " + str(usr_cash))
                    break
            break
else:
    while 1:
        print("Now Item Enhance Stat = +" + str(usr_enhan))
        print("Now Item Enhance Probability = " + str(enhan_per[usr_enhan]) + "%")
        print("Now Item Enhance Cost [Gold] = " + str(enhan_cost[usr_enhan]))
        print("Total Enhance Cost [Gold] = " + str(total_cost))
        usr_cash = round(total_cost / 8000000, 4)
        print("[Gold] -> [Cash] = " + str(usr_cash))
        if usr_enhan >= 10:
            print("\n")
            print("*"*20)
            print("Warning!! \nFailure to enhance will break or lower.")
            print("*" * 20)
        input("\nPlease Enter Button to Enhance +"+str(usr_enhan)+ " -> +" + str(usr_enhan+1))
        os.system("clear")
        usr_enhan, total_cost = enhan_tem(usr_enhan, total_cost)
