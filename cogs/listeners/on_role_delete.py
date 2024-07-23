import nextcord
from nextcord.ext import commands
from bot import Bot
from config import remove_role, get_roles


class Role_Delete(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: nextcord.Role) -> None: # Runs when a role is deleted
        if role.id in get_roles(role.guild.id): # If role is in database remove it, preventing future errors
            remove_role(role.guild.id, role.id)

def setup(client: Bot):
    client.add_cog(Role_Delete(client))