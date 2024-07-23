import nextcord
from nextcord.ext import commands
from nextcord.abc import GuildChannel
from config import get_channels, remove_channel
from bot import Bot

class Channel_Delete(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: GuildChannel) -> None: # Runs when a channel is deleted
        if channel.id in get_channels(channel.guild): # If channel is in database remove it, preventing future errors
            remove_channel(channel.guild, channel.id)

def setup(client: Bot):
    client.add_cog(Channel_Delete(client))