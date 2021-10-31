from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To PROUD-INDIAN-BOT String Session\nGenerator By @agora_swamy\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API-KEY-ID, API-HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your Proud Indian Bot String Session\n(Tap to copy it) \n\n `{SESSION}` \n\n And Visit @INDIANBOTSUPPORT For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing PROUD-INDIAN-BOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : If you are indian (+91)(your ph number) Kindly Retry"
        )
        print("")
        continue
    break
