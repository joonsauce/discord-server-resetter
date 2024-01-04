from help import *
from settings import *

@bot.command()
async def reset(ctx):
    await ctx.send("Are you sure you want to remove ALL non-admin users from this server?\n"
                   "This action CANNOT be undone.\n"
                   "If you are sure, please respond with the name of this server.\n"
                   "Note that name capitalization matters.")

    def checkMessage(msg):
        return msg.author == ctx.author

    try:
        msg = await bot.wait_for("message", check=checkMessage, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("Timed out. Please try again.")
        return

    if msg.content == ctx.message.guild.name:
        for m in ctx.message.guild.members:
            if not m.guild_permissions.administrator:
                await m.kick()
    else:
        await ctx.send("The server name is incorrect. Please try again.")

bot.run(bot_token)