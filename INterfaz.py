#!/usr/bin/env python
import socket
import os
import sys
import subprocess
import getpass
import json

pass_auth = "CLARASAKURA-224"
auth_code = ""
username = os.environ['USERNAME']
auth_code = os.environ['AUTH_CODE']
session_user = os.environ['ADMIN']
session_pass = os.environ['ADMIN_PASS']
password_auth = os.environ['PASSWORD_AUTH']





def start(): 
    #print("        ############     ####              ##############    ######             ####   ##########   ##################    ##############    ##############          ")
    #print("     #################   ####             ################   ########           ####  ############# ##################   ################   #################        ")  
    #print("   ####################  ####            ##################  ####  ####         ####  ####    ##### ##################  ##################  ###################     ")
    #print("  ####                   ####           ####            #### ####   ####        ####  ####    #####        ####        ####            #### ####          ######   ")
    #print(" ####                    ####           ####            #### ####    ####       ####  ####    #####        ####        ####            #### ####          ######   ")
    #print("####                     ####           ####            #### ####     ####      ####  ####    #####        ####        ####            #### ####          #####    ")
    #print("####        ############ ####           ####            #### ####      ####     ####  #############        ####        ####            #### ##################     ")
    #print("####        ############ ####           ####            #### ####       ####    ####  #############        ####        ####            #### ###############        ")
    #print("####               ####  ####           ####            #### ####        ####   ####  ####     ####        ####        ####            #### ###############        ")
    #print(" ####             ####   ####           ####            #### ####         ####  ####  ####     ####        ####        ####            #### ####       #####       ")
    #print("   ####          ####    ####           #################### ####          #### ####  ####     ####        ####        #################### ####       #####       ")
    #print("    ################     ############    ##################  ####           ########  ####     ####        ####         ##################  ####       #####       ")
    #print("     ##############      ############     ################   ####            #######  ####     ####        ####          ################   ####       #####       ")

    print("\n\n\n######################################################################################################")
    print("######################################################################################################\n\n\n")
    
    print("####       ## ######### ##########   ######### ##     ## #########   ######### ######### #########             ")
    print("## ##      ## ######### ##########   ######### ##     ## ##########  ######### ######### ###########             ")
    print("##  ##     ## ##            ##       ##        ##     ## ##      ### ##        ##        ##       ###      ")
    print("##   ##    ## #########     ##       ######### ##     ## ##########  ######### ######### ###########             ")
    print("##    ##   ## #########     ##       ######### ##     ## #########   ######### ######### #########             ")
    print("##     ##  ## ##            ##              ## ##     ## ##     ###  ##        ##        ##     ###        ")
    print("##      ## ## #########     ##       ######### ######### ##     ###  ##        ######### ##     ###         ")
    print("##       #### #########     ##       ######### ######### ##     ###  ##        ######### ##     ###        ")
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t BY: N3TGH0ST")
    print("######################################################################################################")
    print("######################################################################################################\n\n\n")
    print("LOGIN TO CONTINUE...")
    user = input("User>_ ")
    password = getpass.getpass("Password>_ ")

    if(user == session_user and password == session_pass):
        print("\t\t\t\t\t########################################")
        print("\t\t\t\t\t##                                    ##")
        print("\t\t\t\t\t##       ACCESS GRANTED!! :)          ##")
        print("\t\t\t\t\t##       WELCOME BACK GH0ST!!!        ##")
        print("\t\t\t\t\t##                                    ##")
        print("\t\t\t\t\t########################################")

        input()
        os.system("clear")
        menu()
    else:
        print("\t\t\t\t\t########################################")
        print("\t\t\t\t\t##                                    ##")
        print("\t\t\t\t\t##       ACCESS DENIED!! :(           ##")
        print("\t\t\t\t\t##       PLEASE TRY AGAIN             ##")
        print("\t\t\t\t\t##                                    ##")
        print("\t\t\t\t\t########################################")
        
        input("\n\n Press enter to Continue")
        os.system("clear")
        start()

    print("\n\n\n##############################################################################################")


def getJSON(json_file):
    os.system("clear")
    with open(json_file, 'r') as fp:
        data = json.load(fp)
    print(data)
    print("\n\n\n\n#################################################################################\n\n\n")
    input("Type enter to continue")
    menu()

def menu():
    print("\n\n\n\n#########################################################")
    print("Enter an option for scanning or infection: \n 1.- Scan HOST\n 2.- Get all infected Hosts \n 3.- Scan Traffic \n 4.- Persistent on Host \n 5.- Network scan \n 0.- Return to Menu")
    print("\n###############################################################\n\n\n")
    option = int(input("Enter an option!!: "))
    choice(option)

def exploit_list():
    os.system("clear")
    print("##################################################")
    print("\nSelect an attack \n 1.- Kernel attack \n 2.- OS detection")
    

def omega_protocol():
    os.system("clear")
    print("Omega protocol activated!!!!!! \n Please enter the username and password to continue: ")
    username = input("Username: ")
    password = input("Password: ")
    print("SYSTEM DESTRUCTION INITIATED")

def access_denied():
    os.system("clear")
    print("#################################################################################################################################################################")
    print("#################################################################################################################################################################\n\n")
    print("       ****          ***********    **********  *********  ********* *********     ***********     ********* *****        *** ********* ********* ************    ")
    print("      ******        ************   ***********  *********  ********* *********     ************    ********* *** ***      *** ********* ********* *************   ")
    print("     ***  ***      ***            ***           ***        ***       ***           ***      ****   ***       ***  ***     ***    ***    ***       ***       ****  ")
    print("     ***   ***    ***            ***            *********  ********* **********    ***       ****  ********* ***   ***    ***    ***    ********* ***         *** ")
    print("    ***********   ***            ***            *********  ********* **********    ***        **** ********* ***    ***   ***    ***    ********* ***        **** ")
    print("   ***       ***   ***            ***           ***              ***        ***    ***       ****  ***       ***     ***  ***    ***    ***       ***       ****  ")
    print("  ***         ***   ************   ***********  *********  ********* **********    *************   ********* ***      *** *** ********* ********* *************   ")
    print(" ***           ***    **********    **********  *********  ********* **********    ************    ********* ***        ***** ********* ********* ************    ")
    print("\n\n#################################################################################################################################################################")
    print("#################################################################################################################################################################\n\n")
    
    input("Type enter to continue")
    os.system("clear")
    menu()

def choice(option):
    #option =int(input("Enter an option!!: "))
    if(option == 1):
        ip_host = input("Enter Host IP address: ")
        print("[*] Scanning " + ip_host)
    elif(option == 2):
        myObj = getJSON('MOCK_DATA.json')
    elif(option==3):
        print("[*] Initializing network scanning... \n")
    elif(option==4):
        ip_host = input("Enter host IP address to infect: ")
        if(ip_host== ""):
            os.system('clear')
            start()
            print("The host doesn't exists")
            menu()
        else:
            print(type(ip_host))
            print("starting attack to:", ip_host)
    elif(option ==5):
        #ip_host =raw_input("Enter network segment to scan: ")
        print("Beginning Network scan")
        os.system("clear")
        os.system("sudo tcpdump")
        os.system("clear")
        ##if(ip_host== ""):
        ##    os.system('clear')
        ##    start()
        ##    print("Wrong network segment")
        ##    menu()
        ##else:
        ##    print(type(ip_host))
        ##    print("starting Scanning:", ip_host)
    elif(option == 6):
        menu()
    elif(option == 292):
        ##os.system("clear")
        auth_code = getpass.getpass('Enter Authtorization code!!!!: ')
        if(auth_code == pass_auth):
            omega_protocol()
        else:
            access_denied()
    else:
        print("The option doesn't exists")
        menu()

os.system("clear")
start()
#menu()







