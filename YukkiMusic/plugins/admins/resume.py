#
# Copyright (C) 2021-2022 by ramoben200@Github, < https://github.com/ramoben200 >.
#
# This file is part of < https://github.com/ramoben200/BallasMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ramoben200/BallasMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from BallasMusic import app
from BallasMusic.core.call import Ballas
from BallasMusic.utils.database import is_music_playing, music_on
from BallasMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Yukki.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
