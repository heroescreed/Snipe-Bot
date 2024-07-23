import os
from bot import Bot

os.chdir("./") # Change directory to base directory

client = Bot() 
client.initialize() # Runs the bot