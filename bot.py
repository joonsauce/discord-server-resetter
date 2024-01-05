from help import *
from settings import *

@bot.command()
async def reset(ctx, *, message=''):
    if not ctx.author.guild_permissions.administrator or ctx.author.bot:
        await ctx.send("You do not have the permission to perform this command.")
        return

    roles = []

    if message:
        roles = message.split(",")
        roles = [x.replace(" ", "").replace("<", "").replace(">", "").replace("&", "").replace("@", "") for x in roles]
        guild_roles = [str(r.id) for r in ctx.guild.roles]
        for i in roles:
            if i not in guild_roles:
                await ctx.send("Invalid role selected. Please try again.")
                return
        roles = [discord.utils.get(ctx.guild.roles, id=int(x)) for x in roles]

    await ctx.send("Are you sure you want to remove ALL non-admin users from this server?\n"
                   "This action CANNOT be undone.\n"
                   "If you are sure, please respond with the name of this server.\n"
                   "Please note that name capitalization matters.")

    def checkMessage(msg):
        return msg.author == ctx.author

    try:
        msg = await bot.wait_for("message", check=checkMessage, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("Timed out. Please try again.")
        return

    if not msg.content == ctx.message.guild.name:
        await ctx.send("The server name is incorrect. Please try again.")
        return

    if roles:
        for role in roles:
            for m in role.members:
                if not m.guild_permissions.administrator:
                    await m.kick()
    else:
        for m in ctx.message.guild.members:
            if not m.guild_permissions.administrator:
                await m.kick()

bot.run(bot_token)