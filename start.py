#!/usr/bin/python
"""
This file acts as a quick wrapper for launching the bot script within a virtual
environment. Instead of sourcing the env, running the command, and
backgrounding it each and every time you want to run the bot, you can simply
execute this instead. Options are available if your want to surface the output
of the bot into a foreground process as well, using the -fg or --foreground
args.
"""
import os
import argparse
from subprocess import Popen, PIPE



# Set up some color variables so we can stylize our terminal output later
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def main():
    # Find our relative path
    path_to_self = os.path.dirname(__file__)
    path_to_self = os.path.abspath(path_to_self)

    # Find our virtual environment folder,
    # Find our Python interpreter which'll run our bot,
    # Find our path to the script that has to run under the virtualenv
    virtual_env = os.path.join(path_to_self, 'venv')
    python_bin = os.path.join(virtual_env, 'bin', 'python3')
    script_file = os.path.join(path_to_self, "bot.py")
    api_key_file = os.path.join(path_to_self, "api_key.yaml")

    # Communicate our files and environment
    print("Using virtual environment: %s%s%s" % (WARNING, virtual_env, ENDC))
    print("Using Python interpreter: %s%s%s" % (WARNING, python_bin, ENDC))
    print("Executing script file: %s%s%s" % (WARNING, script_file, ENDC))
    print("API key from file: %s%s%s" % (WARNING, api_key_file, ENDC))

    # Make sure our files actually exists on disk
    if not os.path.isfile(python_bin):
        print(python_bin)
        print("Error: Our python executable doesn't seem to exist")
        return
    if not os.path.isfile(script_file):
        print(script_file)
        print("Error: Our entry point doesn't seem to exist")
        return
    if not os.path.isfile(api_key_file):
        print(api_key_file)
        print("Error: Our api key file doesn't seem to exist")
        return

    # Set up our terminal arg parsing
    parser = argparse.ArgumentParser(
        description="Runs our Discord bot in a virtual environment"
    )
    parser.add_argument(
        "-fg", "--foreground",
        action="store_true",
        help="increase output verbosity",
    )
    args = parser.parse_args()

    # Run our python script in a new process, in our virtual env!
    print("")
    print("--------------------------")
    print("Initializing our bot...")
    print("--------------------------")
    print("")
    if args.foreground:
        print("Running our process in the foreground")
        print("Press %s%sCTRL+C%s to exit" % (BOLD, WARNING, ENDC))
        print("""
        To run in the background:
        Press %s%sCTRL+Z%s to stop, and restore user control of the terminal,
        type in %s%sbg%s to resume the stopped script in the background,
        then %s%sdisown%s to make that process independent of our session.
        """ % (
            BOLD, WARNING, ENDC,
            BOLD, WARNING, ENDC,
            BOLD, WARNING, ENDC,
        ))
        
        Popen([python_bin, script_file]).communicate()
    else:
        Popen([python_bin, script_file], stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    main()
