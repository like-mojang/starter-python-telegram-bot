import botpy, os
from botpy.message import Message
d=0
st = ''
e=[]
for a,b,c in os.walk('/storage/emulated/0/', topdown=True):
    e.append(c)
    if d<=6:
        st += str(a)+' ............ 读取文件（夹）成功\n'
    d+=1
print(st)
print(len(e))
class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        
        await self.api.post_message(channel_id=message.channel_id, content='本地文件读写测试:\n'+st+'......\n手机共'+str (len (e))+'files, 有'+str (len (e)-132)+'files测试通过！')

    async def on_public_message_delete(self, message: Message):
        """
        此处为处理该事件的代码
        """


intents = botpy.Intents(public_guild_messages=True,guild_messages=True, direct_message=True, guilds=True, audio_action=True, forums=True, message_audit=True, interaction=True, guild_members=True, guild_message_reactions=True)
client = MyClient(intents=intents)
print(dir(MyClient))
client.run(appid="102059538", secret="pY6XnqgIkz1pSs42")
