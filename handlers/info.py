from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import *
from pyrogram.errors import *
from pyrogram.types import *
from config import *
import logging
from database.db import Database
from asyncio import sleep
from helper.fsub import forcesub

@Client.on_message(filter.user(OWNER_ID) & filters.command("info"))
async def replay_media(bot, message):
    file = message.reply_to_message
    reference_id = file.text.split()[2]
    info = await bot.get_users(user_ids=reference_id)
    await bot.send_message(OWNER_ID,text=f"""
    **User Info**
    
    **••User id:** [`{info.id}`]
    **••First Name:** {info.first_name}
    **••UserName:** @{info.username}
    
    """)
    

@Client.on_callback_query()  
async def tgm(bot, update):     
    if update.data == "ref": 
        await update.answer("♻️Reloading.....♻️",) 
        await update.message.delete()
        if await forcesub(bot, update):
            return
        info = await bot.get_users(user_ids=OWNER_ID)
        file_id = START_STICKER
        await bot.send_sticker(update.from_user.id, file_id)
        TEXT = START_STRING.format(update.from_user.mention, info.first_name)
        RMB = START_BUTTON  
        await bot.send_message(update.from_user.id, TEXT, reply_markup=RMB)  