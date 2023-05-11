from os import system 

try:

    from colorama import Fore as f

    import time

    from time import strftime

    import string

    from random import choice

    from random import randint

except ModuleNotFoundError:

    print("pip install colorama")

    system("pip install colorama")

    system("clear")

    

print(f"""{f.YELLOW}

 ____  _            _       ____ _____ _

| __ )| | __ _  ___| | __  / ___|___ /| |__   ___ _ __

|  _ \| |/ _` |/ __| |/ / | |     |_ \| '_ \ / _ \ '__|

| |_) | | (_| | (__|   <  | |___ ___) | |_) |  __/ |

|____/|_|\__,_|\___|_|\_\  \____|____/|_.__/ \___|_|

               {f.BLUE}This Tool For{f.RED} Hacking{f.BLUE} Platforms !

""")

print(f"""

{f.GREEN}[{f.YELLOW}1{f.GREEN}]{f.YELLOW} WhatsApp

{f.GREEN}[{f.YELLOW}2{f.GREEN}]{f.YELLOW} Telegram

{f.GREEN}[{f.YELLOW}3{f.GREEN}]{f.YELLOW} Instagram

{f.GREEN}[{f.YELLOW}4{f.GREEN}] {f.YELLOW}Rubika

{f.GREEN}[{f.YELLOW}5{f.GREEN}] {f.YELLOW}Soroosh

{f.RED}[{f.YELLOW}6{f.RED}] Bale

{f.RED}[{f.YELLOW}7{f.RED}] Eitaa

""")

print(f"{f.RED}╭───[ {f.YELLOW}/termux/home{f.RED}] ")

client = str(input(f"╰───>{f.CYAN}  "))

print("\n")

if client == "1" or client == "WhatsApp" or client == "Whatsapp" or client == "whatsapp":

    print(f"{f.RED}╭───[ {f.YELLOW}/termux/home/WhatsApp{f.RED}] ")

    hack = str(input(f"╰─{f.GREEN}Number{f.RED}──>{f.CYAN}  "))

    print(f"\n{f.RED}Start Hacking and Cracking ...")

    char = string.digits

    password = "".join(choice(char) for x in range(randint(3,6)))

    time.sleep(3)

    print(f"""{f.YELLOW}

Hacked in {f.RED}{strftime("%H:%M:%S")}

{f.CYAN}Verify Code is {f.BLUE}{password}

{f.RED}B{f.WHITE}Y{f.GREEN}E""")

    

elif client == "4" or client == "Rubika" or client == "rubika" or client == "rub":

    print(f"{f.RED}╭───[ {f.YELLOW}/termux/home/Rubika{f.RED}] ")

    hack = str(input(f"╰─{f.GREEN}ID{f.RED}──>{f.CYAN}  @"))

    print(f"\n{f.RED}Start Hacking and Cracking ...")

    char = string.digits

    password = "".join(choice(char) for x in range(randint(5,6)))

    time.sleep(3)

    print(f"""{f.YELLOW}

Hacked in {f.RED}{strftime("%H:%M:%S")}

{f.CYAN}Verify Code is {f.BLUE}{password}

{f.RED}B{f.WHITE}Y{f.GREEN}E""")

elif client == "2" or client == "Telegram" or client == "telegram" or client == "tel":

    print(f"{f.RED}╭───[ {f.YELLOW}/termux/home/Telegram{f.RED}] ")

    hack = str(input(f"╰─{f.GREEN}ID{f.RED}──>{f.CYAN}  @"))

    print(f"\n{f.RED}Start Hacking and Cracking ...")

    char = string.digits

    password = "".join(choice(char) for x in range(randint(5,6)))

    time.sleep(3)

    print(f"""{f.YELLOW}

Hacked in {f.RED}{strftime("%H:%M:%S")}

{f.CYAN}Verify Code is {f.BLUE}{password}

{f.RED}B{f.WHITE}Y{f.GREEN}E""")

elif client == "3" or client == "Instagram" or client == "insta" or client == "instagram":

    print(f"{f.RED}╭───[ {f.YELLOW}/termux/home/Instagram{f.RED}] ")

    hack = str(input(f"╰─{f.GREEN}Page ID{f.RED}──>{f.CYAN}  @"))

    print(f"\n{f.RED}Start Hacking and Cracking ...")

    char = string.digits

    password = "".join(choice(char) for x in range(randint(5,6)))

    time.sleep(3)

    print(f"""{f.YELLOW}

Hacked in {f.RED}{strftime("%H:%M:%S")}

{f.CYAN}Verify Code is {f.BLUE}{password}

{f.RED}B{f.WHITE}Y{f.GREEN}E""")

elif client == "5" or client == "soroosh" or client == "Soroosh" or client == "sor":

    print(f"{f.RED}╭───[ {f.YELLOW}/termux/home/Soroosh{f.RED}] ")

    hack = str(input(f"╰─{f.GREEN}ID{f.RED}──>{f.CYAN}  @"))

    print(f"\n{f.RED}Start Hacking and Cracking ...")

    char = string.digits

    password = "".join(choice(char) for x in range(randint(5,6)))

    time.sleep(3)

    print(f"""{f.YELLOW}

Hacked in {f.RED}{strftime("%H:%M:%S")}

{f.CYAN}Verify Code is {f.BLUE}{password}

{f.RED}B{f.WHITE}Y{f.GREEN}E""")

    
