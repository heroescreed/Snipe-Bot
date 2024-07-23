from typing import List
from .json_handler import json_add_channel, json_add_role, json_get_channel_mode, json_get_channels, json_get_role_mode, json_get_roles, json_remove_channel, json_remove_role, json_update_channel_mode, json_update_role_mode
from .sql_handler import sql_add_channel, sql_remove_channel, sql_remove_role, sql_update_channel_mode, sql_update_role_mode, sql_add_data, sql_add_role, sql_get_channel_mode, sql_get_role_mode, sql_get_channels, sql_get_guild_data, sql_get_roles
from constants import DATABASE_MODE
from utils import colour_message

errormessage = colour_message(message="Inccorect database mode, use either 'SQL' or 'JSON'", color="red") # Generates error message to be printed to console

# For each function, checks selected database mode and runs relevant function

def get_channel_mode(guild_id: int) -> str:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_channel_mode(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_channel_mode()
    else:
        print(errormessage)

def get_role_mode(guild_id: int) -> str:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_role_mode(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_role_mode()
    else:
        print(errormessage)

def update_channel_mode(guild_id: int, mode: str) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_update_channel_mode(guild_id, mode)
    elif DATABASE_MODE.lower() == "json":
        json_update_channel_mode(mode)
    else:
        print(errormessage)

def update_role_mode(guild_id: int, mode: str) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_update_role_mode(guild_id, mode)
    elif DATABASE_MODE.lower() == "json":
        json_update_role_mode(mode)
    else:
        print(errormessage)

def get_channels(guild_id: int) -> List[int]:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_channels(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_channels()
    else:
        print(errormessage)

def get_roles(guild_id: int) -> List[int]:
    if DATABASE_MODE.lower() == "sql":
        return sql_get_roles(guild_id)
    elif DATABASE_MODE.lower() == "json":
        return json_get_roles()
    else:
        print(errormessage)

def add_channel(guild_id: int, channel: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_add_channel(guild_id, channel)
    elif DATABASE_MODE.lower() == "json":
        json_add_channel(channel)
    else:
        print(errormessage)

def add_role(guild_id: int, role: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_add_role(guild_id, role)
    elif DATABASE_MODE.lower() == "json":
        json_add_role(role)
    else:
        print(errormessage)

def remove_channel(guild_id: int, channel: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_remove_channel(guild_id, channel)
    elif DATABASE_MODE.lower() == "json":
        json_remove_channel(channel)
    else:
        print(errormessage)

def remove_role(guild_id: int, role: int) -> None:
    if DATABASE_MODE.lower() == "sql":
        sql_remove_role(guild_id, role)
    elif DATABASE_MODE.lower() == "json":
        json_remove_role(role)
    else:
        print(errormessage)