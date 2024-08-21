import random
import time
import os
from colorama import Fore, init

import datetime
init()

LOGER = """
██╗   ██╗ ██████╗ ██╗  ██╗███████╗██╗     
██║   ██║██╔═══██╗╚██╗██╔╝██╔════╝██║     
██║   ██║██║   ██║ ╚███╔╝ █████╗  ██║     
╚██╗ ██╔╝██║   ██║ ██╔██╗ ██╔══╝  ██║     
 ╚████╔╝ ╚██████╔╝██╔╝ ██╗███████╗███████╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ 1.1
"""

if os.path.exists("tokens.txt"):
    e = input("Tokens.txt exists. Would you like to remove it? Y/N: ").upper()
    if e == "Y":
        os.remove("tokens.txt")

if os.path.exists("userid.txt"):
    with open("userid.txt", "r") as file:
        print(Fore.LIGHTGREEN_EX + "user id file detected")
        os.system("cls")
        id = file.read().strip()
else:
    id = input("User ID? (base64 utf8 encoded): ")
    id = id.replace("==", "")  
    id += "."  
    if input("Would you like to save the ID so it is automatically used unless the file is deleted? Y/N: ").upper() == "Y":
        print("Saving ID...")
        with open("userid.txt", "w") as file:
            file.write(id)
            print("Id saved")
            os.system("cls")  
    time.sleep(1)  
table1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
os.system("cls")
print(Fore.LIGHTRED_EX+ LOGER + Fore.RESET)
Seks = int(input("How many tokens?: "))
print(Fore.GREEN +"Generating tokens for: " + id)


choice = [".lower()", ".upper()"]

def generatetoken():
    token = ""  
    
    
    token += id 

    
    for _ in range(random.randint(3, 8)):
        x = random.choice(choice)
        randomletter = random.choice(table1)
        randomletter = randomletter.lower() if x == ".lower()" else randomletter.upper()
        token += randomletter
    
    token += "."  

    
    hmac_length = random.randint(26, 28)  
    for _ in range(hmac_length):
        x = random.choice(choice)
        randomletter = random.choice(table1)
        


        randomletter = randomletter.lower() if x == ".lower()" else randomletter.upper()
        token += randomletter

    return token

try:
    
    with open("tokens.txt", "a") as file:
        for _ in range(Seks): 
            date = datetime.datetime.now()
            x = generatetoken()
            print(Fore.LIGHTMAGENTA_EX, str(date),  "[+]" , x , Fore.RESET )  
            file.write(x + "\n")

    os.system("cls")
    print(Fore.LIGHTGREEN_EX + "Tokens have been generated and saved to tokens.txt")
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(6)  
