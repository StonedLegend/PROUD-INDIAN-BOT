from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To 𝗣𝗥𝗢𝗨𝗗-𝗜𝗡𝗗𝗜𝗔𝗡-𝗕𝗢𝗧 String Session\nGenerator By @𝗦𝗧𝗢𝗡𝗘𝗗-𝗟𝗘𝗚𝗘𝗡𝗗-𝗔𝗚𝗢𝗥𝗔\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), 𝗔𝗣𝗜_𝗜𝗗, 𝗔𝗣𝗜_𝗛𝗔𝗦𝗛) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your 𝗣𝗥𝗢𝗨𝗗-𝗜𝗡𝗗𝗜𝗔𝗡-𝗕𝗢𝗧 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡\n(Tap to copy it) \n\n `{𝗦𝗘𝗦𝗦𝗜𝗢𝗡}` \n\n And Visit @INDIANBOTSUPPORT For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing 𝗣𝗥𝗢𝗨𝗗-𝗜𝗡𝗗𝗜𝗔𝗡-𝗕𝗢𝗧 Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : 𝗜𝗙 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗜𝗡𝗗𝗜𝗔𝗡 (+𝟵𝟭)(𝗬𝗢𝗨𝗥 𝗡𝗨𝗠𝗕𝗘𝗥) Kindly Retry"
        )
        print("")
        continue
    break
