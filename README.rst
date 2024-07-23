.. image:: https://ko-fi.com/img/githubbutton_sm.svg
   :target: https://ko-fi.com/Q5Q710SOTM
   :alt: Kofi Link

.. image:: https://img.shields.io/discord/1265317002960961556?color=blue&label=discord
   :target: https://discord.gg/tT3WX2uZBC
   :alt: Discord

Snipe Bot
--------

An open-source, easy-to-use Python bot.

Features
-------------

- /snipe command to send the last deleted message in a channel
- /settings command to customize the channels that /snipe can be used in and the roles that can use it
- Both SQL and JSON support for small-scale and larger-scale applications

How To Use
----------

First, download all files from this repository into a folder.

Next, open PowerShell and run the following command

.. code:: sh

    pip install -r requirements.txt

This will install all the required packages.

In the same folder level as ''constants.py'', create a new file called ``.env``.

Inside the ``.env`` file put the following

.. code:: env

    TOKEN = ""
    DBENDPOINT = ""
    DBUSER = ""
    DBPASS = ""
    DBNAME = ""
    DBPORT = ""

Put your Discord bot token in the token variable, and if you are going to be using SQL, fill out the database information; otherwise, you can leave them as is.

Inside ''constants.py'', select the database mode you wish to use. (Defaults to JSON)

.. code:: py

    DATABASE_MODE = "JSON" # USE EITHER "SQL" or "JSON" ONLY.

In a PowerShell window, run the following command

.. code:: sh

    py main.py

This should run the bot.

**NOTE:** If you get a ``CommandNotFoundException`` try running

.. code:: sh

    python main.py

Which one you use will depend on your PATH variables

Where to host the bot
----------

There are many services that provide bot hosting, but personally, I recommend `PebbleHost <https://pebblehost.com/bot-hosting>`_ for your hosting needs. Alternatively, I can host the bot for you if you subscribe to my `Ko-fi <https://ko-fi.com/Q5Q710SOTM>`_

Support
----------

- `LightCreed Commissions Server <https://discord.gg/tT3WX2uZBC>`_
- `Discord Developers Server <https://discord.gg/discord-developers>`_
- Add me on Discord: ``@heroescreed``