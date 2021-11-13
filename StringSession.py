from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style, Back



logo = """
"""
ganja_fooko_bolte = """
#STONEDLEGENDAGORA        
Made With Love By STONEDLEGENDAGORA
"""
                                                                                                            
print("")
print(Style.BRIGHT + Fore.MAGENTA + Legend)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.BLUE + logo)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + Back.BLUE + bhai_bolte)
print(Style.RESET_ALL)
print("""Welcome To PROUD-INDIAN-BOT String Generator By @STONEDLEGENDAGORA""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @INDIANBOTSUPPORT For Any Help !",
            )

            print(
                "Thanks for Choosing PROUDINDIANBOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +919811099999 ! Kindly Retry"
        )
        print("")
        continue
    break
