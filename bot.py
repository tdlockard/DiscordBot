"""
Tyler Lockard
11/20/2018

A Discord bot meant to replicate one of our friends who became too involved with 
World of Warcraft to interact with the real world. Reactions are artisan
crafted to mimic the delicate, yet sophisticated idiocy of our beloved friend.
It honestly fills the void surprisingly well. Raising questions about how much
of a real person they were to begin with... :thinking:

Some resources used:
https://discordpy.readthedocs.io/en/latest/api.html
https://discord.com/developers/applications
"""

import os
import yaml
import random
import asyncio
import discord
import emoji



# You can optionally set your API key here instead of the "api_key.yaml" file
API_KEY = ''

# Modify the following numbers to affect how frequently the bot interacts
STATUS_CHANGE_FREQUENCY = 240  # (In seconds) The delay between updating activities
INTERRUPT_CHANCE = 400  # The odds that the bot will respond while you're typing
RESPONSE_CHANCE = 100  # The odds that the bot will randomly respond to a message
DOGPILE_CHANCE = 5  # The odds that the bot will attempt to react to a reaction
REACTION_CHANCE = 10  # The odds that the bot will attempt to react to a message
REACTION_LIMIT = 3  # The cap on how many reactions the bot can add to a message


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('------------------------------------')
        print("STATUS_CHANGE_FREQUENCY: %s seconds" % STATUS_CHANGE_FREQUENCY)
        print("INTERRUPT_CHANCE: 1/%s odds" % INTERRUPT_CHANCE)
        print("RESPONSE_CHANCE: 1/%s odds" % RESPONSE_CHANCE)
        print("DOGPILE_CHANCE: 1/%s odds" % DOGPILE_CHANCE)
        print("REACTION_CHANCE: 1/%s odds" % REACTION_CHANCE)
        print("REACTION_LIMIT: %s" % REACTION_LIMIT)
        print('------------------------------------')

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('------------------------------------')
        print('We have logged in as %s' % self.user)
        print('------------------------------------')
        await self.change_presence(activity=discord.Game(name="Startup"))

    async def on_typing(self, channel, user, when):
        """
        Interject someone's message with some rude garbage
        """
        print("%s's typing in %s..." % (user, channel))

        if random.randint(0, INTERRUPT_CHANCE) == 1:
            responses = [
                "We out here", "yeh.", "brooooooo", "Broh!", "I feel that",
                "no u", "wait...", "wait", "HulloooOOOOOOOOO!??",
            ]
            await channel.send(random.choice(responses))

    async def on_reaction_add(self, reaction, user):
        """
        Dogpile some extra reactions when someone else reacts to a message
        """
        print("%s reacted to a message with %s" % (user, reaction))

        # Pardon me
        if user == self.user:
            print("That's me reacting, skipping...")
            return

        # Only add reactions once
        for reaction in reaction.message.reactions:
            if reaction.me == True:
                print("I've already reacted to that message, skipping...")
                return

        # React
        if random.randint(0, DOGPILE_CHANCE) == 1:
            await self.react(reaction.message)

    async def on_message(self, message):
        """
        Respond to select messaging
        """
        print("Received a message:\n%s\n%s\n" % (message, message.content))

        # Ignore my own messages
        if message.author == self.user:
            print("That's my own message...")
            return

        # Reply to very specific messages with very specific "canned" responses
        if message.content.lower().startswith('i have a question'):
            await self.say(message, "How dare you")
            return

        elif message.content.lower().startswith('leeroy'):
            await self.say(message, "JENKINS!!!")

        elif 'git gud' in message.content.lower():
            await self.say(message, 'lul')

        elif message.content.lower().startswith('wait'):
            responses = ["wait...", "wa- wait...", "wait."]
            await self.say(message, random.choice(responses))

        elif message.content.lower().startswith('wow'):
            responses = [
                "Wow.", "Wow dude. Wow.", "Wow, dude. That's TOUGH!!!",
                "I feel attacked.", "VERY TRU!!!", "Broooooooo",
            ]
            await self.say(message, random.choice(responses))

        elif (
            '793711293415948289' in message.content or  # User: @Waffleses_Bot
            '343576869804965889' in message.content or  # User: @Michael
            '800880542487805953' in message.content or  # Role: @Waffle_Bot
            '795813462525476894' in message.content or  # Role: @FFXIV_bros
            'waffleses' in message.content.lower() or
            'waffles' in message.content.lower() or
            'warcraft' in message.content.lower() or
            'mike means' in message.content.lower() or
            'michael means' in message.content.lower()
        ):
            responses = [
                "no, u", "no u", "no, u!", "yeh. u rite.", "Broh!",
                "We out here...", "Wait...", "TRUE!", "Wow.", "Wow dude. Wow.",
                "Wow, dude. That's TOUGH!!!", "HulloooOOOOOOOOO!??",
                "I have a question...", "I feel attacked.", "VERY TRU!!!",
                "I'm raiding", "Big true", "Broooooooo", "ahahaha, IDIOT!",
                "_anime noises_", "Bye Felicia!", "you hate to see it...",
                "DON'T @ ME!!!", ":poop:",
            ]
            await self.say(message, random.choice(responses))

        elif (
            'no u' in message.content.lower() or
            'no, u' in message.content.lower() or
            'no, you' in message.content.lower() or
            'no you' in message.content.lower()
        ):
            responses = [
                "no, u", "no u", "no, u!",
                "no, u", "no u", "no, u!",
                "no, u", "no u", "no, u!",
                "yeh. u rite.", "Broh!", "We out here...", "Wait...", "TRUE!",
                "Wow.", "Wow dude. Wow.", "Wow, dude. That's TOUGH!!!",
                "HulloooOOOOOOOOO!??", "I have a question...",
                "I feel attacked.", "VERY TRU!!!", "Big true",
                "_anime noises_", "Bye Felicia!", ":poop:", "Broooooooo",
                "you hate to see it...", "DON'T @ ME!!!", "ahahaha, IDIOT!",
            ]
            await self.say(message, random.choice(responses))

        # Roll the dice, should we respond to the message with a basic message?
        elif random.randint(0, RESPONSE_CHANCE) == 1:
            responses = [
                "I feel that", "True", "u rite", "brooooooo", "Broh!",
                '"%s" dees nuts!' % message.content,
            ]
            await self.say(message, random.choice(responses))

        else:
            print("I decided to not respond to this message...")

        # Roll the dice, should we attempt to react to the message contents?
        if random.randint(0, REACTION_CHANCE) == 1:
            await self.react(message)

    async def my_background_task(self):
        """
        Periodically update the "game" that the bot is playing
        """
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(STATUS_CHANGE_FREQUENCY)
            games = [
                "Wow.", "Imgur", "Reddit", "Tic Toc", "Casually", "Nord VPN",
                "Minecraft", "COD of Duty", "Destiny Also", "Gatcha Games",
                "Raid Shadowlegends", "My Brains Out Right Now",
                "Call of Duty 2 Two 17.5 HD Remix Electric Boogaloo",
            ]
            status = random.choice(games)
            await self.change_presence(activity=discord.Game(name=status))

    async def react(self, message):
        """
        Simulate a natural emoji reaction based on the message contents
        self.emojis  # This server's current emojis
        """
        print("Applying some Emoji reactions...")

        stop_words = [
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
            "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
            'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
            'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them',
            'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
            'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
            'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
            'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
            'by', 'for', 'with', 'about', 'against', 'between', 'into',
            'through', 'during', 'before', 'after', 'above', 'below', 'to',
            'from', 'up', 'down', 'in', 'im', 'out', 'on', 'off', 'over',
            'again', 'further', 'then', 'once', 'here', 'there', 'when', 'k',
            'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'under',
            'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
            'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
            'can', 'will', 'just', 'don', "don't", 'should', "should've",
            'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
            "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',
            "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
            "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't",
            'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'people',
            'shouldn', "shouldn't", 'wasn', "wasn't", 'way', 'weren', 'hold',
            "weren't", 'won', "won't", 'wouldn', "wouldn't", 'right', 'left',
            'last', 'first',
        ]

        # Find contextually relevant emoji
        matches = []
        for character in emoji.EMOJI_ALIAS_UNICODE_ENGLISH:
            for word in message.content.lower().strip().split():
                if word not in stop_words:

                    # Store our current matches for comparison later
                    match_count = len(matches)

                    # Look for literal matches
                    if ":%s:" % word == character:
                        matches.append(emoji.emojize(character))
                        print("\tFound a literal match...")

                    # Look for partial matches
                    elif len(word) > 4:
                        if word in character:
                            matches.append(emoji.emojize(character))
                            print("\tFound a partial match...")

                    # Report any matching emoji
                    if len(matches) > match_count:
                        print("\tAdding %s %s from key word %s" % (
                                emoji.emojize(character),
                                character,
                                word,
                            )
                        )

        # Try to add our reaction (not all emoji exist in Discord)
        random.shuffle(matches)
        limit = random.randrange(1, REACTION_LIMIT)
        for count, match in enumerate(matches):
            try:
                # Simulate some thought process
                await asyncio.sleep(random.randint(1, 12))

                # Finally, react. Wow.
                await message.add_reaction(match)

                # Limit our possible reaction count
                if count > limit:
                    break
            except:
                print('Failed to apply an emoji reaction "%s"' % match)

        print("Done applying emoji reactions.")

    async def say(self, message, response):
        """
        Simulate some user typing delay based on the length of the response
        """
        print("Responding %s" % response)

        # Thinking
        await asyncio.sleep(random.randrange(1, 12))

        # Typing
        async with message.channel.typing():
            typing_delay = len(response) / 6
            await asyncio.sleep(typing_delay)
            await message.channel.send(response)


def main():
    """
    The main entry point for our bot setup
    """
    # Extract our Discord api key from the adjacent "api_key.yaml" file
    global API_KEY
    if not API_KEY:
        path_to_self = os.path.dirname(__file__)
        path_to_self = os.path.abspath(path_to_self)
        api_key_file = os.path.join(path_to_self, "api_key.yaml")
        with open(api_key_file) as f:
            env = yaml.load(f, Loader=yaml.Loader)
            API_KEY = env['api_key']

    # Exit early if we don't have what we need
    if not API_KEY:
        msg = "Hmm, we don't seem to have an API key to run this bot! Please "
        msg += "add one in the \"api_key.yaml\" file, or edit the API_KEY "
        msg += "variable in this script to continue."
        print(msg)
        return

    # Specify the ability to read message text content.
    # May not be necessary now, after the recent change to Discord bots.
    intents = discord.Intents.default()
    intents.messages = True

    # Finally, run the bot!
    client = MyClient(intents=intents)
    client.run(API_KEY)


if __name__ == "__main__":
    main()
