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

import config
from strings import get_command
from BallasMusic import app
from BallasMusic.misc import SUDOERS
from BallasMusic.utils.database import add_off, add_on
from BallasMusic.utils.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@app.on_message(filters.command(VIDEOMODE_COMMAND) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
