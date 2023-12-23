import botpy, os
from botpy.message import Message
class MyClient(botpy.Client):
    bot_log=None
    async def on_at_message_create(self, message: Message):
        
        await self.api.post_message(channel_id=message.channel_id, content='本地文件读写测试:测试通过！')

    async def on_public_message_delete(self, message: Message):
        """
        此处为处理该事件的代码
        """


intents = botpy.Intents(public_guild_messages=True,guild_messages=True, direct_message=True, guilds=True, audio_action=True, forums=True, message_audit=True, interaction=True, guild_members=True, guild_message_reactions=True)
client = MyClient(intents=intents)
print(dir(MyClient))
client.run(appid="102059538", secret="pY6XnqgIkz1pSs42")
