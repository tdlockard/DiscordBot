# Overview
A Discord bot meant to replicate one of our friends who became too involved with 
World of Warcraft to interact with the real world. Bot reactions are artisan-crafted to mimic the delicate, yet sophisticated idiocy of our beloved friend.
It honestly fills the void surprisingly well. Raising questions about how much
of a real person they were to begin with... :thinking:


# Set up your Discord Bot "Application" and grab a Discord API key
For deeper instructions, see the following links:

https://discordpy.readthedocs.io/en/latest/discord.html

https://discord.com/developers/applications

Add your new bot "application" to your Discord Server. Ensure it has the correct messaging permissions.


# Installation

## 1. Ensure that you have "Python 3" installed on your machine.
Mac and Linux probably have it installed by default. Windows is windows...

## 2. Download or clone this github repo, and `cd` into that directory.
Simple enough.

## 3. Apply your Discord App API Key to your bot
You can add the api key to the **"api_key.yaml"** file or you can set it within the bot.py script itself, on the **API_KEY** variable at the top of the script. Either way. Since API keys should never be shared, the **"api_key.yaml"** file could offer better security, with file permissions or other wackiness. But that's ultimately up to you.

## 3. Install the required python libraries
**Option 1:** YOLO? Simply install the python libraries on your local machine.

    python3 -m pip install -r requirements.txt

**Option 2:** Set up a "virtual environment" to contain everything the bot needs, in its own sandbox. Debatably better. Particularly if you have a lot of "stuff" running on your machine, or if it's running on a server of sorts... You don't want the version of these libraries to conflict with other app requirements. Since I don't know what's running on your machine, I recommend this method.
1. [Install "virtual env" on your machine](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

2. Create a virtual environment for Python 3

        virtualenv -p python3 venv

    1. Initialize our new virtual env
        
            source env/bin/activate

    2. Install our pip requirements within this new sandbox environment

            python3 -m pip install -r requirements.txt


# Running the Bot
When you're ready, you basically just run the `bot.py` script with python3. If you set everything correctly, it should grab your API key and connect to your Discord Server(s) as the bot user you set up on the Discord Dev website.

    python3 bot.py

If you've set up a virtual env, you can run the `start.py` script instead of having to jump through the hoops of **initializing** the env and whatnot. This file acts as a quick wrapper for launching the bot. Instead of **sourcing the env**, **running the bot command**, and **backgrounding it** each and every time you want to run the bot, you can simply execute this instead. Options are available if your want to see the bot output in a foreground process. *(Use the `-fg` or `--foreground` args)*

By default it kicks the process into the background.

    ./start.py
    ./start.py -fg
    ./start.py --foreground

# Stopping the Bot
Need to stop a bot that's running in the background? For convenience there's also a quick command to kill the bot process. In the somewhat likely event of a robot apocalypse. Alternatively you can just run `top` or `htop` and kill the bot.py process.

    ./stop.py