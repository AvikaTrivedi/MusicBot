from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import queue
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("DJ DOMIN8or=▶️ Paused.")


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("DJ DOMIN8or ⏸ Resumed.")


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        queue.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("DJ DOMIN8or =⏹ Stopped streaming.")


@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    queue.task_done(chat_id)

    if queue.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, queue.get(chat_id)["file_path"]
        )

    await message.reply_text("DJ DOMIN8or=⏩ Skipped the current song.")


@Client.on_message(
    filters.command("admincache")
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("DJ DOMIN8or=❇️ Admin cache refreshed!")
