import os
import sys

from pyrogram import Client
from pyrogram.types import Message

from utils import filters


@Client.on_message(filters.command(["restart"]) & filters.sudo & ~filters.forwarded)
async def restart(_: Client, message: Message):
    await message.reply_text("<code>Restarting...</code>")
    os.execvp(sys.executable, [sys.executable, *sys.argv])
