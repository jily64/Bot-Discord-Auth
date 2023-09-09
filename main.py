import discord
from discord.ext import commands
import asyncio
from websockets.server import serve
import com

intents = discord.Intents.default()


bot = commands.Bot(command_prefix='>', intents=intents)


async def echo(websocket):
    async for message in websocket:
        mes = message.split('<!>')
        if mes[0] == 'test':
            a = await com.com.test(mes[1])
        elif mes[0] == 'getUserName':
            a = await com.com.getUserName(mes[1], bot)
        elif mes[0] == 'getUserAvatarURL':
            a = await com.com.getUserAvatarURL(mes[1], bot)
        elif mes[0] == 'sendMessage':
            a = await com.com.showMessageInChannel(bot, mes[1])
        elif mes[0] == 'log':
            a = await com.com.logInMessage(mes[1], bot)
        elif mes[0] == 'logSucs':
            a = await com.com.logInMessageSuccess(mes[1], bot)
        elif mes[0] == 'logFail':
            a = await com.com.logInMessageFail(mes[1], bot)
        else:
            a = 'error'
        await websocket.send(str(a))


@bot.event
async def on_ready():
    print("bot is ready")
    async with serve(echo, "", 1000):
        while True:
            await asyncio.sleep(1)



bot.run("MTA5ODk4NjcxMDk5MTM4NDU5Nw.GH9hQw.na7HNpIGCPrYKTIjRoF9Xc01Ryu6YbUhTMheGk")

bot.run("MTA5ODk4NjcxMDk5MTM4NDU5Nw.G7xrZT.EknuMPmZRKBNKlRD9ID6Rj2p3lF74AOH_0caog")