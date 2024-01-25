#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 26311402
API_HASH = "012450e57d2bc98d0693c6982d01a2d7"
BOT_TOKEN = "6726180531:AAGqQMUmjVs4IrpZbvuz79DT-YluOle-3y8"
SESSION = "1BQANOTEuMTA4LjU2LjE5MAG7YVEDXuzeoth/bNqHJA/pJkd2Gc29pm7OpoKypkDRHAwNkY7vVUMCGcbLK2zQAQwSm1VYdc1GAHqT8k4gvvUPtaLl76XPJkJb9E4xfpRD/z6im+7g8d/2DQpESYd/okTe8NTb8TVC2b0gXX/lTPuitUmv2CMbOawxT6+Gx/1jTmfzX9qtSx//v+5v/T0KrX9fkXOVvlMyTF+3Njbcichi2xSFk5dzliAOz485AQUpiBQscTd5xGVWnU26aYPi9qOBIEDPfjHeOGWE3WPUlOD1mlyqr3f8fr8siBQ7vAgRvpG4u/UJhE4PkZRRfj49MEXt3lCfy5EKu9ze2AJIvt6K8g=="
FORCESUB = "DroneBots"
AUTH = 5832887847

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
