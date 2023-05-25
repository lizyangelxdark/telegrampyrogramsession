import os

os.system("apt-get update && apt-get upgrade -y && pkg upgrade -y && pip3 uninstall -r requirements.txt && pip3 install -r requirements.txt")

# https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")


CASPER = r"""
    ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
    ║╔══╝║╔═╗║║╔══╝║╔═╗║║╔══╝║╔═╗║
    ║║───║╚═╝║║╚══╗║╚═╝║║╚═╗─║╚═╝║
    ║║───║╔═╗║╚══╗║║╔══╝║╔═╝─║╔╗╔╝
    ║╚══╗║║─║║╔══╝║║║───║╚══╗║║╚╬╗
    ╚═══╝╚╝─╚╝╚═══╝╚╝───╚═══╝╚╝─╚╝
"""

print(
    f"""
    {CASPER}
    
    👻 Welcome to Session String Generator
    
    Enter p: Pyrogram Session String
    Enter t: Telethon Session String
    """
)

choice = ""
while (choice != "p" or choice != "t"):
    choice = input("Enter p or t: ")

    if choice == "p":
        print("\nPackage installation in progress...")
        import pyrogram
        print("One moment, please.")
        from pyrogram import enums
        print("\nSuccessfully switched to Pyrogram.\n")
        API_ID = int(input("Enter API ID: "))
        API_HASH = input("Enter API HASH: ")
        print("")
        with pyrogram.Client("my_account", api_id = API_ID, api_hash = API_HASH, in_memory = True) as ssg_casper:
            ssg_casper.send_message("me", f"Here is your session string: \n\n<code>{ssg_casper.export_session_string()}</code> \n\nSession String Generator", parse_mode=enums.ParseMode.HTML)
            print("\nYour session string has been successfully generated!")
            print("Please check your Telegram saved messages.")
        break

    elif choice == "t":
        print("\nPackage installation in progress...")
        from telethon.sync import TelegramClient
        print("One moment, please.")
        from telethon.sessions import StringSession 
        print("\nSuccessfully switched to Telethon.\n")
        API_ID = int(input("Enter API ID: "))
        API_HASH = input("Enter API HASH: ") 
        print("")
        with TelegramClient(StringSession(), API_ID, API_HASH) as ssg_casper:
            ssg_casper.send_message("me", f"Here is your session string: \n\n<code>{ssg_casper.session.save()}</code> \n\nSession String Generator", parse_mode="html")
            print("\nYour session string has been successfully generated!")
            print("Please check your Telegram saved messages.")
        break

    else:
        print("\nInvalid input!\n")   