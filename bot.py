import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith("!find"):
        user_id = message.content[6:]
        user = await client.fetch_user(int(user_id))
        embed = discord.Embed(title="User Information", description="", color=0x00ff00)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="Account creation date", value=user.created_at.strftime("%b %d, %Y"), inline=True)
        await message.channel.send(embed=embed)

client.run("bot_token")
