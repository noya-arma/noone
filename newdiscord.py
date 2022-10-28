import os
import re

import hikari

bot = hikari.GatewayBot(token='MTAzNTQzNjU2Mzc2NjcwNjIwNg.GKpAjQ.-QCATffY9rfo71po72LKkEDzS5Ds-RD1FQfyiM')

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