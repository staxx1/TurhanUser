from telethon import events
import asyncio
from userbot.events import register
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

@register(outgoing=True, pattern="^.banall")
async def banall(event):
    await event.edit("`Tüm kullanıcılar banlanıyor...`")
    ben = await event.client.get_me()
    all_participants = await event.client.get_participants(event.chat_id)
    for user in all_participants:
        if user.id == ben.id:
            pass
        try:
            await event.client(EditBannedRequest(
                event.chat_id, int(user.id), ChatBannedRights(
                    until_date=None,
                    view_messages=True
                )
            ))
        except Exception as e:
            await event.reply(str(e))
        await asyncio.sleep(0.3)
    await event.edit("`İşlem tamam!`")
