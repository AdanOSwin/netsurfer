import sys
import socket
import os

def clear():
    os.system("clear")

def menu_scan():
    print("\t\t\t\t\t\t\t\t ##############################################    ")
    print("\t\t\t\t\t\t\t\t ##                                          ##    ")
    print("\t\t\t\t\t\t\t\t ##                                          ##    ")
    print("\t\t\t\t\t\t\t\t ##                 MENU                     ##    ")
    print("\t\t\t\t\t\t\t\t ##     1.- Check if hosts is up             ##    ")
    print("\t\t\t\t\t\t\t\t ##     2.- Check open ports and services    ##    ")
    print("\t\t\t\t\t\t\t\t ##     3.- Check routes                     ##    ")
    print("\t\t\t\t\t\t\t\t ##     4.- Brute force DNS                  ##    ")
    print("\t\t\t\t\t\t\t\t ##     5.- Enable OS detection              ##    ")
    print("\t\t\t\t\t\t\t\t ##     6.- Exit                             ##    ")
    print("\t\t\t\t\t\t\t\t ##                                          ##    ")
    print("\t\t\t\t\t\t\t\t ##                                          ##    ")
    print("\t\t\t\t\t\t\t\t ##############################################    ")

    option = int(input("\n\nEnter an option: "))
    scan_option(option)

def scan_option(option):
    if(option==1):
        host = input("Enter host to scan (IP address or URL): ")
        os.system("sudo nmap -sn " + host)
        print("\n###################################\n")
        print("Scan complete!!!")
        input()
        clear()
        menu_scan()
    elif(option==2):
        host = input("Enter host IP address or URL: ")
        os.system("sudo nmap -v -A " + host)
        print("#################################################3")
        print("\n Scan complete!!!!!")
        input()
        clear()
        menu_scan()
    elif(option==3):
        host = input("Enter IP address or URL to scan: ")
        os.system("sudo nmap -sn --traceroute " + host)
        print("\n###################################\n")
        print("Scan complete!!!")
        input()
        clear()
        menu_scan()
    elif(option==4):
        host = input("Enter IP address or URL to scan: ")
        os.system("sudo nmap -sn --script dns-brute " + host)
        print("\n###################################\n")
        print("Scan complete!!!")
        input()
        clear()
        menu_scan()
    elif(option==5):
        host = input("Enter IP address or URL to scan: ")
        os.system("sudo nmap -sS -sV -O " + host)
        print("\n###################################\n")
        print("Scan complete!!!")
        input()
        clear()
        menu_scan()
    elif(option==6):
        print("Menu principal")
    else:
        print("Invalid option")
        input()
        clear()
        menu_scan()


print("\t\t\t\t\t\t\t\t ##############################################    ")
print("\t\t\t\t\t\t\t\t ##                                          ##    ")
print("\t\t\t\t\t\t\t\t ##                                          ##    ")
print("\t\t\t\t\t\t\t\t ##        HOST SYSTEM AND PORT SCAN         ##    ")
print("\t\t\t\t\t\t\t\t ##                                          ##    ")
print("\t\t\t\t\t\t\t\t ##                                          ##    ")
print("\t\t\t\t\t\t\t\t ##                                          ##    ")
print("\t\t\t\t\t\t\t\t ##############################################    ")

input()
clear()

#print("\n\nMENU\n1.-Check if host is up \n2.-Check open ports and Services\n3.- Check Routes\n4.-Enable OS detection")

menu_scan()



