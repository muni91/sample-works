from botbuilder.core import ActivityHandler, TurnContext

class TeamsBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Echo incoming text
        await turn_context.send_activity(f"You said: {turn_context.activity.text}")
