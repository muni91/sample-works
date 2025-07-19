import os
from aiohttp import web
from dotenv import load_dotenv
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from bot_app.bot import TeamsBot

load_dotenv()

APP_ID = os.getenv("APP_ID", "")            # empty for emulator
APP_PASSWORD = os.getenv("APP_PASSWORD", "")

# Adapter and Bot
settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter  = BotFrameworkAdapter(settings)
bot      = TeamsBot()

async def messages(req):
    body = await req.json()
    activity = req.app["adapter"].activity_factory().create_activity(body)
    auth_header = req.headers.get("Authorization", "")
    response = await adapter.process_activity(activity, auth_header, bot.on_turn)
    return web.Response(status=response.status)

app = web.Application()
app["adapter"] = adapter
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3978)
