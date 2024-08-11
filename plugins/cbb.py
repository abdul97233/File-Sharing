
from pyrogram import __version__
from levi import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Dᴇᴠ : <a href='https://t.me/abdul97233'>Abdul</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/ntmchat'>NTM CHAT</a>\n○ DEV Cʜᴀɴɴᴇʟ : <a href='https://t.me/ntmpro'>NTM PRO Cʜᴀɴɴᴇʟ</a>\n○ NTM AI : <a href='https://t.me/NTMAI'>NTM AI</a>\n○ Support group : <a href='https://t.me/NTMCHAT'>ᴄʜᴀᴛ Group</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('MAIN Cʜᴀɴɴᴇʟ', url='https://t.me/ntmpro')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
