#-*- coding: utf8 -*-

import random
import os

enhan_cost = [314280, 314280, 314280, 314280, 628560, 691416, 754272, 817128, 879984, 942840, 942840, 1571400, 2547000,
              4129000, 8568000]
enhan_per = [100, 100, 100, 100, 80, 70, 60, 50, 40, 30, 25.9, 18, 9.2, 5.4, 2.1]
enhan_name = [a for a in range(0,16)]


def enhan_tem(usr_enhan, total_cost):
    print("--"*10)
    now_cost = enhan_cost[usr_enhan]
    now_per = enhan_per[usr_enhan]
    usr_rand = random.randrange(0,101.00)
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

def check_digit(usr_input):
    try:
        int(usr_input)
        return True
    except ValueError:
        return False


while 1:
    usr_enhan = enhan_name[0]
    total_cost = 0
    total_count = 0

    os.system("clear")
    print("1. Auto Enhance")
    print("2. Enhance")
    print("3. Exit")
    print("Select Number")
    usr_input = input(">>")
    if not check_digit(usr_input) or not int(usr_input) in range(4): continue
    os.system("clear")
    if int(usr_input) == 1:
        while 1:
            usr_auto = input("Set Enhance Number [0 ~ 15] >>")
            if int(usr_auto) in enhan_name:
                while 1:
                    usr_enhan, total_cost = enhan_tem(usr_enhan, total_cost)
                    total_count += 1
                    os.system("clear")
                    if usr_enhan == int(usr_auto):
                        print("User Set Enhance = +" + str(usr_auto))
                        print("Final Enhance = +" + str(usr_enhan))
                        print("Total Enhance Count = " + str(format(total_count,',')))
                        print("Total Cost [Gold] = " + str(format(total_cost,',')))
                        usr_cash = int(round(total_cost * 0.00083, 4))
                        print("[Gold] -> [Cash] = " + str(format(usr_cash,',')))
                        input("\nPlease Enter Button to Exit..")
                        break
                break
    elif int(usr_input) == 2:
        while 1:
            print("Now Item Enhance Stat = +" + str(usr_enhan))
            print("Now Item Enhance Probability = " + str(enhan_per[usr_enhan]) + "%")
            print("Now Item Enhance Cost [Gold] = " + str(format(enhan_cost[usr_enhan],',')))
            print("Total Enhance Count = " + str(format(total_count,',')))
            print("Total Enhance Cost [Gold] = " + str(format(total_cost,',')))
            usr_cash = int(round(total_cost * 0.00083, 4))
            print("[Gold] -> [Cash] = " + str(format(usr_cash,',')))
            if usr_enhan == max(enhan_name):
                input("\nPlease Enter Button to Exit")
                break
            if usr_enhan >= 10:
                print("\n")
                print("*"*20)
                print("Warning!! \nFailure to enhance will break or lower.")
                print("*"*20)
            print("\n[Enter] Button to Enhance +"+str(usr_enhan)+ " -> +" + str(usr_enhan+1))
            print("[init] Input to Init")
            print("[exit] input to Exit")
            usr_select = input(">> ")
            os.system("clear")
            if usr_select == "init":
                usr_enhan = 0
                total_cost = 0
                total_count = 0
                continue
            elif usr_select == "exit": break
            else:
                total_count += 1
                usr_enhan, total_cost = enhan_tem(usr_enhan, total_cost)
    else:
        os.system("clear")
        break
