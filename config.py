import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # from @botfather
API_ID = int(os.getenv("API_ID", ""))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "")  # from https://my.telegram.org/apps
MONGO_URI = os.getenv("MONGO_URI", "")
force_subchannel = os.getenv("FSUB", "gishankrishka1_cloud")
OWNER_ID = int(os.environ.get("OWNER_ID", "1884885842"))
START_STRING = os.getenv("START_STRING", "Hi {}, Welcome to  {}'s Pm Bot.")
START_STICKER = os.getenv("START_STICKER", "CAADBQADZQQAAlHy2FQE5VU4XGjXrwI")
#Strings 
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
FORCESUB_TEXT = "**â Access Denied â**\n\nMemehub eke nathuva Mokatada yako Botva Start Kare kkkðð\nâ»ï¸Join and Try Again.â»ï¸"
HELP_STRING = """Hello.. â£ï¸GIsá¼á´É´ KÊIÊsá¼á´á´â£ï¸
Type your query here..
I'll respond to your query as earliest ð"""



#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('ð Êá´á´Êá´ Êá´É¢s ð', user_id=f"{OWNER_ID}")
                 ],
                 [
                 InlineKeyboardButton(text="â»ï¸ Reload â»ï¸",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("ð®ððððð", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="ð» Êá´á´á´á´ ð»",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('âð°ð»ð¿ð·ð° ä¹ â¢ Bots ãð±ð°ã', url="https://t.me/AlphaTm_Botz")
                 ],
                 [
                 InlineKeyboardButton(text="ð´ Êá´Êá´ ð´",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("ð sá´á´Êá´á´ á´á´á´á´ ð", url="https://github.com/TeamAlphaTg/Pm-Chat-bot") 
                 ]]
                  )

DEV_BTN = InlineKeyboardMarkup([[              
            InlineKeyboardButton('à¼â£ï¸â¢ï¸â£IrÃÎ®âmà¸Åâ â¢ï¸â£ï¸à¼ ', user_id="ImGishan")
            ],
            [
            InlineKeyboardButton('unknown boyâð°ð»ð¿ð·ð° ä¹ â¢', user_id="UnknownB_o_y")
            ],
            [
            InlineKeyboardButton('Å¦Ä§ÈºÉáµ¾ê ÉÉnáµ¾ÉÈº', user_id="ImTharuk")
            ],
            [
            InlineKeyboardButton('ð¯ððð ð°ððððð ð±ð°ð¸ ð± ð§ ð´ ð¹ ð¸ â¢', user_id="SL_BOTS_TM")
            ],
            [
            InlineKeyboardButton('ð¿ðð£ðªð¬ðð£ ð±ð°', user_id="ImDenuwan")
            ],
            [
            InlineKeyboardButton("ð sá´á´Êá´á´ á´á´á´á´ ð", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot") 
            ]]
            )
HELP_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('âð°ð»ð¿ð·ð° ä¹ â¢ Bots ãð±ð°ã', url="https://t.me/AlphaTm_Botz")
                 ],
                 [
                 InlineKeyboardButton("ð sá´á´Êá´á´ á´á´á´á´ ð", url="https://github.com/TeamAlphaTg/Pm-Chat-bot") 
                 ],
                 [
                 InlineKeyboardButton("Back", callback_data="stback") 
                 ]]
                  )

#Rndm Stkr



STAT_STICKER = ["CAADAQAD7gMAAv5DwUe0nbeQnSoavAI",
                "CAADAgAD8QEAAladvQohKm5i6iYv7gI"              
         ]  

         
DEV_STICKER = ["CAADAgADaRsAAsOUWUpHrmf5mZp3EgI",
                "CAADAgADbAIAAladvQoqGV6cxNDenwI",
                "CAADAgADgQEAAiteUwteCmw-bAABeLQC", 
                "CAADBQADZgMAAvIEcFVMnMXcAqRX7gI",
                "CAADAgADFwADlp-MDlZMBDUhRlElAg"                
         ] 

HELP_STICKER = ["CAADAgADYgADWbv8JXMOJcSM3-2OAg",
                "CAADAgADzwEAAhZCawpc3d8UgDDcaQI",
                "CAADAgAD9AIAAvPjvgtVDXi3hHimOQI", 
                "CAADAgADiQEAAiteUwt812TG6sLw9AI"               
         ]




print("Config Working....")
