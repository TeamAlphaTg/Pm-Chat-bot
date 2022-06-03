import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
BOT_TOKEN = os.getenv("BOT_TOKEN", "5011377446:AAHavxAS4fO42B41mNVcKVoQL8z6D6_LUdU")  # from @botfather
API_ID = int(os.getenv("API_ID", "8838171"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "0587408d4f7d9301f5295840b0f3b494")  # from https://my.telegram.org/apps
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ultroid10:9vQtrB1LxJbVXc5a@cluster0.4ssb3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
force_subchannel = os.getenv("FSUB", "gishankrishka1_cloud")
OWNER_ID = int(os.environ.get("OWNER_ID", "1884885842"))
START_STRING = os.getenv("START_STRING", "Hi {}, Welcome to  {}'s Pm Bot.")
START_STICKER = os.getenv("START_STICKER", "CAADBQADZQQAAlHy2FQE5VU4XGjXrwI")
#Strings 
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\nMemehub eke nathuva Mokatada yako Botva Start Kare kkk😒😒\n♻️Join and Try Again.♻️"
HELP_STRING = "Meme Tiye nam dapam Mekata😒😂. Adminlata Msg Daanna One Nam ekat Mekata dapam 😒😂"



#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', user_id=f"{OWNER_ID}")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id=f"{OWNER_ID}")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot") 
                 ]]
                  )

DEV_BTN = InlineKeyboardMarkup([[              
            InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
            ],
            [
            InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
            ],
            [
            InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
            ],
            [
            InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™', user_id="SL_BOTS_TM")
            ],
            [
            InlineKeyboardButton('𝘿𝙚𝙣𝙪𝙬𝙖𝙣 🇱🇰', user_id="ImDenuwan")
            ],
            [
            InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot") 
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
