import os
import re

import hikari
access_token= os.environ["ACCESS_TOKEN"]

bot = hikari.GatewayBot(token=access_token)

@bot.listen()
async def on_message(event: hikari.GuildMessageCreateEvent) -> None:

    if not event.is_human:
        return

    if event.message.attachments:
        await event.message.respond("", attachment=event.message.attachments[0])
    else:
        await event.message.respond(event.message.content)

    await event.message.delete()


bot.run()