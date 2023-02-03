#!/usr/bin/python
"""
This file acts as a quick wrapper for stopping the bot script within the virtual
environment.
"""
from subprocess import Popen



print("Killing our bot process...")
Popen(['pkill', '-9', '-f', 'bot.py']).communicate()
