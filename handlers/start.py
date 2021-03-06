from database.db import Database
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import *
from pyrogram.errors import *
from pyrogram.types import *
from config import *
import logging
from database.db import Database
from asyncio import sleep
import traceback
from helper.fsub import forcesub

DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "ALPHA_PM")     

@Client.on_message(filters.command("start"))
async def start(client, message):
    if await forcesub(client, message):
       return
    #return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    info = await bot.get_users(user_ids=OWNER_ID)
    file_id = START_STICKER
    await client.send_sticker(message.chat.id, file_id, reply_markup=start_menu)
    text = START_STRING.format(message.from_user.mention, info.first_name)
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
  

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await bot.send_sticker(message.chat.id, S_STICKER)
  await message.reply_text(text=HELP_STRING,reply_markup=HELP_BTN)

    
    
@Client.on_callback_query(filters.regex("stback"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(START_STRING,reply_markup=START_BUTTON)

@Client.on_callback_query(filters.regex("hlp"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(HELP_STRING,reply_markup=HELP_BTN)
