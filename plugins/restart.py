import os
import sys

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["restart"]) & filters.user(6815918609) & ~filters.forwarded
)
async def _restart(_: Client, message: Message):
    await message.reply_text("<code>Restarting...</code>")
    os.execvp(sys.executable, [sys.executable, *sys.argv])