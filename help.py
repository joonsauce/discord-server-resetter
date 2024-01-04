from settings import *

@bot.command()
async def help(ctx, *, msg=""):
    embed = discord.Embed(color=None)
    embed.set_author(name="Discord Server Resetter Help")
    if not msg:
        embed.add_field(name="help", value="Displays the help menu, or information on a specific command. "
                                           "Usage: dsr!help <command>*", inline=False)
        embed.add_field(name="reset", value="Resets the server. Kicks all non-admin members if roles aren't specified. "
                                            "Usage: dsr!reset <roles>*", inline=False)
    elif msg == "help":
        embed.add_field(name="help", value="Displays the help menu, or information on a specific command. "
                                           "Usage: dsr!help <command>*", inline=False)
    elif msg == "reset":
        embed.add_field(name="reset", value="Resets the server. Kicks all non-admin members if roles aren't specified. "
                                            "Usage: dsr!reset <roles>*", inline=False)
    else:
        embed.add_field(name=msg, value="Command `"+msg+"` does not exist", inline=False)
    embed.add_field(name="NOTE", value="Asterisks (*) indicate optionality of the element.", inline=False)
    await ctx.send(embed=embed)

