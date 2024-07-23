import random, nextcord
from nextcord.ext import commands
from bot import Bot
from constants import COLOUR_MAIN, KO_FI
from config import get_channel_mode, get_channels, get_role_mode, get_roles
from utils import create_warning_embed

snipe_message_author = {}
snipe_message_content = {}
snipe_message_link = {}

class Snipe(commands.Cog):
    def __init__(self, client: Bot) -> None:
        self.client = client

    @nextcord.slash_command(name="snipe", description="Snipe the last deleted message in this channel")
    async def snipe(self, interaction: nextcord.Interaction) -> None:
        if (get_channel_mode(interaction.guild.id) == "blacklist") and (interaction.channel.id in get_channels(interaction.guild.id)): # Checks if the channel is blacklisted
            await interaction.send(embed=create_warning_embed(title="Channel Blacklisted", description="This channel has the `/snipe` command disabled"), ephemeral=True)
            return
        elif (get_channel_mode(interaction.guild.id) == "whitelist") and (not interaction.channel.id in get_channels(interaction.guild.id)): # Checks if the channel isnt whitelisted
            await interaction.send(embed=create_warning_embed(title="Channel Not Whitelisted", description="This channel hasn't got the `/snipe` command enabled"), ephemeral=True)
            return
        elif (get_role_mode(interaction.guild.id) == "blacklist"): # Checks if role is on blacklist mode
            for roleid in get_roles(interaction.guild.id): # Iterates through each role in the list
                try:
                    role = interaction.guild.get_role(roleid) # Attempts to fetch the role
                    if role in interaction.user.roles: # If user has the role prevent them from running the command
                        await interaction.send(embed=create_warning_embed(title="Role Blacklisted", description="You have a role which prevents you from using `/snipe`"), ephemeral=True)
                        return
                except: # Catches all errors
                    pass
        elif (get_role_mode(interaction.guild.id) == "whitelist"): # Checks if role is on whitelist mode
            p = False
            for roleid in get_roles(interaction.guild.id): # Iterates through each role in the list
                try:
                    role = interaction.guild.get_role(roleid) # Attempts to fetch the role
                    if role in interaction.user.roles:  # If user has the role allow them to run the command
                        p = True
                        break
                except: # Catches all errors
                    pass
            if not p: # If user has no whitelisted roles, prevent them from running the command
                await interaction.send(embed=create_warning_embed(title="No Whitelisted Roles", description="You dont have a role which allows you to use `/snipe`"), ephemeral=True)
                return
        try: # If there is nothing matching my request in the dict this will error
            embed = nextcord.Embed(title=f"{str(snipe_message_content[interaction.channel.id])[:256]}", description=f"[Go to conversation]({snipe_message_link[interaction.channel.id]})", colour=COLOUR_MAIN) # Adds the first 256 characters of the message content as the embed title and the link as the description.
            embed.set_footer(text=f"Sniped by {interaction.user} | Coded by @heroescreed") # Add who used the snipe command to the footer
            member = interaction.guild.get_member(int(snipe_message_author[interaction.channel.id])) # Get the member of the orininal message as a member item
            embed.set_author(name=member, icon_url=member.display_avatar.url) # Set the embed author to be the author of the original message 
            await interaction.send(embed=embed)
            del snipe_message_author[interaction.channel.id] # Reset deleted message content
            del snipe_message_content[interaction.channel.id] # Reset deleted message content
            del snipe_message_link[interaction.channel.id] # Reset deleted message content
            chance = random.randint(1, 3)
            if chance == 1:
                await interaction.edit_original_message(content=f"Support the creator on [Ko-fi]({KO_FI})")
        except KeyError: # The error is caught and sends a reasonable message.
            await interaction.send("No recently deleted message was found in this channel", ephemeral=True)    

    @commands.Cog.listener()
    async def on_message_delete(self, message: nextcord.Message) -> None: # Runs when a message is deleted
        if (not message.author.bot) and (not message.content is None): # Prevets the bot from logging bot messages or messages containing no text
            if (get_channel_mode(message.guild.id) == "blacklist") and (message.channel.id in get_channels(message.guild.id)): # Checks if the channel is blacklisted
                return
            elif (get_channel_mode(message.guild.id) == "whitelist") and (not message.channel.id in get_channels(message.guild.id)): # Checks if the channel isnt whitelisted
                return
            snipe_message_author[message.channel.id] = message.author.id # Adds the message author ID as the most recently deleted message in the channel
            snipe_message_content[message.channel.id] = message.content# Adds the message content as the most recently deleted message in the channel
            snipe_message_link[message.channel.id] =  message.jump_url # Adds the link to the last message as the most recently deleted message in the channel

def setup(client: Bot) -> None:
    client.add_cog(Snipe(client))