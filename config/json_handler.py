import json
from typing import List

def json_get_channel_mode() -> str:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["channel_mode"].lower() # Returns the channel mode in lower case

def json_get_role_mode() -> str:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["role_mode"].lower() # Returns the role mode in lower case

def json_update_channel_mode(mode: str) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["channel_mode"] = mode # Sets channel mode to be the new value
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_update_role_mode(mode: str) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["role_mode"] = mode # Sets role mode to be the new value
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_get_channels() -> List[int]:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["channels"] # Returns the channels list

def json_get_roles() -> List[int]:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    return data["roles"]  # Returns the roles list

def json_add_channel(channel_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["channels"].append(channel_id) # Adds channel id to channels list
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_remove_channel(channel_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    index = data["channels"].index(channel_id) # Finds the index where the channel id is
    del data["channels"][index] # Deletes the channel id using the index
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_add_role(role_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    data["roles"].append(role_id) # Adds channel id to channels list
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)

def json_remove_role(role_id: int) -> None:
    with open("config/settings.json", "r") as f: # Opens config json file in read only and retrieves the data inside
        data = json.load(f)
    index = data["roles"].index(role_id) # Finds the index where the role id is
    del data["roles"][index] # Deletes the channel id using the index
    with open("config/settings.json", "w") as f: # Opens config json file in write mode and sets the new data
        json.dump(data, f)