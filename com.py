import random
import discord
class com:
  async def test(params):
    return params

  async def getUserName(id, bot):
    guild = bot.get_guild(1059119644490874910)
    for i in guild.members:
      if i.name == id:
        return i.display_name

  async def getUserAvatarURL(id, bot):
    guild = bot.get_guild(1067365236983738368)
    for i in guild.members:
      if i.name == id:
        return i.avatar

  async def showMessageInChannel(bot, mes):
    guild = bot.get_guild(1067365236983738368)
    channel = guild.get_channel(1093419853907509289)
    embed = discord.Embed(title='Message from server')
    embed.add_field(name='Message', value=mes)
    await channel.send(embed=embed)
    return True
    
  async def logInMessage(id, bot):
    guild = bot.get_guild(1067365236983738368)
    for i in guild.members:
      if i.name == id:
        a = random.randint(1000, 9999)
        embed = discord.Embed(title='Your Auth Code')
        embed.add_field(name='Right Here!', value=str(a))
        await i.send(embed=embed)
        return str(a)
  async def logInMessageSuccess(id, bot):
    guild = bot.get_guild(1067365236983738368)
    for i in guild.members:
      if i.id == int(id):
        embed = discord.Embed(title='Successfuly Authorised!')
        await i.send(embed=embed)
        return True

  async def logInMessageFail(id, bot):
    guild = bot.get_guild(1067365236983738368)
    for i in guild.members:
      if i.id == int(id):
        embed = discord.Embed(title='Auth Failed')
        await i.send(embed=embed)
        return True
        