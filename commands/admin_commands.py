import discord
from discord.ext import commands
import random
from messages import *

class admin(commands.Cog):
  def __init__(self, client):
    self.client = client


  ##### Servername
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_guild=True)
  async def servername(self, ctx, *, name=None):
    if name == None:
      await ctx.reply(random.choice(no_server_name_messages), mention_author=True)
    else:
      await ctx.guild.edit(name=name)
      server_name_messages = [f"{ctx.message.author} changed server name to {name}", "Done!", f"Done! Now the server is called {name}."]
      await ctx.reply(random.choice(server_name_messages), mention_author=False)
      return


  ##### Rolecreate
  @commands.command(no_pm=True)
  @commands.has_permissions(manage_roles=True, manage_guild=True)
  async def rolecreate(self, ctx, perm:int=521942715968, *, name = None):
    if name == None:
      await ctx.reply(random.choice(rolecreate_no_name_messages), mention_author = True)
    else:
      try:
        guild = ctx.guild
        await guild.create_role(name=name, permissions=perms)
        rolecreate_created_messages = [f"The {name} role has been created!", "Done!", f"Created {name} role"]
        await ctx.reply(random.choice(rolecreate_created_messages), mention_author=False)
      except:
        await ctx.reply("Thats not a perm id. If you don't have one, you can generate one here\nhttps://discordapi.com/permissions.html")


  ##### Roledel
  @commands.command(pass_context=True, no_pm=True)
  @commands.has_permissions(manage_roles=True, manage_guild=True)
  async def roledel(self, ctx, *, role_name=None):
    roledel_deleted_messages = [f"Deleted the {role_name} role.", "Done!", f"The {role_name} role has been deleted!"]
    if role_name == None:
      await ctx.reply(random.choice(roledel_no_role_messages), mention_author=True)
    role = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role.delete()
    await ctx.reply(random.choice(roledel_deleted_messages), mention_author=False)


  ##### Channelcreate
  @commands.command(pass_context=True, no_pm=True)
  @commands.has_permissions(manage_channels=True, manage_guild=True)
  async def channelcreate(self, ctx, channel_type=None, *, channel=None):
    guild = ctx.message.guild
    channelcreate_created_messages = [f"the {channel} channel has been created", "done!", f"Created {channel} channel"]
    if channel == None:
      await ctx.reply(random.choice(channelcreate_no_name_messages), mention_author=True)
    elif channel_type == None:
      await ctx.reply(random.choice(channelcreate_no_type_messages), mention_author=True)

    elif channel_type == "text":
      await guild.create_text_channel(channel)
      await ctx.reply(random.choice(channelcreate_created_messages), mention_author=False)
    elif channel_type == "voice":
      await guild.create_voice_channel(channel)
      await ctx.reply(random.choice(channelcreate_created_messages), mention_author=False)


  ##### Channeldel
  @commands.command(pass_context=True, no_pm=True)
  @commands.has_permissions(manage_channels=True, manage_guild=True)
  async def channeldel(self, ctx, *, channel_name=None):
    channeldel_no_channel_messages = [f"No channel named, '{channel_name}' was found", "i can't find that channel", f"There's no channel named {channel_name}"]
    channeldel_deleted_messages = [f"Deleted the {channel_name} channel", "Done!", f"The {channel_name} channel has been deleted"]
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel is not None:
      await existing_channel.delete()
      await ctx.reply(random.choice(channeldel_deleted_messages), mention_author=False)
    else:
      await ctx.send(random.choice(channeldel_no_channel_messages), mention_author=True)


def setup(client):
  client.add_cog(admin(client))