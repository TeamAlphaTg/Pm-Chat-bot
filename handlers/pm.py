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



@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == OWNER_ID:
        await reply_text(bot, message)
        return
    if await forcesub(bot, message):
       return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=OWNER_ID,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    
@Client.on_message(filters.private & filters.sticker)
async def pm_sticker(bot, message):
    if message.from_user.id == OWNER_ID:
        await replay_media(bot, message)
        return
    if await forcesub(bot, message):
       return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=OWNER_ID,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(OWNER_ID, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    
@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == OWNER_ID:
        await replay_media(bot, message)
        return
    if await forcesub(bot, message):
       return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    msg=message.caption
    await bot.copy_message(
        chat_id=OWNER_ID,       
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=PM_MED_ATT.format(reference_id, message.from_user.mention, msg)
    )

@Client.on_message(filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=f"**Msg From**:{message.from_user.mention}\n\n{message.text}",
            chat_id=int(reference_id)
        )


@Client.on_message(filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.id
        )

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