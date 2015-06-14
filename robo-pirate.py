#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

import json
import sys
import re
import random
from twitterbot import TwitterBot
from os.path import expanduser


class RoboPirate(TwitterBot):
    def bot_init(self):
        """
        Initialize and configure your bot!

        Use this function to set options and initialize your own custom bot
        state (if any).
        """

        ############################
        # REQUIRED: LOGIN DETAILS! #
        ############################

        with open("etc/access.json", 'r') as access:
            authdb = json.load(access)

        self.config['api_key'] = authdb["API_Key"]
        self.config['api_secret'] = authdb["API_Secret"]
        self.config['access_key'] = authdb["Access_Token"]
        self.config['access_secret'] = authdb["Access_Token_Secret"]

        access.close()

        ######################################
        # SEMI-OPTIONAL: OTHER CONFIG STUFF! #
        ######################################

        # how often to tweet, in seconds
        self.config['tweet_interval'] = 60 * 60  # 60 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes

        # Tweet range: every 120 to 420 minutes
        self.config['tweet_interval_range'] = (60 * 60, 420 * 60)

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = False

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = True

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = ['pirate', 'robot pirate', 'yarrr', 'treasue']

        # follow back all followers?
        self.config['autofollow'] = True


        ###########################################
        # CUSTOM: your bot's own state variables! #
        ###########################################

        # If you'd like to save variables with the bot's state, use the
        # self.state dictionary. These will only be initialized if the bot is
        # not loading a previous saved state.

        # self.state['butt_counter'] = 0

        # You can also add custom functions that run at regular intervals
        # using self.register_custom_handler(function, interval).
        #
        # For instance, if your normal timeline tweet interval is every 30
        # minutes, but you'd also like to post something different every 24
        # hours, you would implement self.my_function and add the following
        # line here:

        # self.register_custom_handler(self.my_function, 60 * 60 * 24)

        # log path
        home = expanduser("~")
        self.config['log_path'] = home + '/var/bot_logs/'

        # what's up with reply interval?
        self.config['reply_interval'] = 7 * 60

    def get_insult(self):
        with open("share/nouns.json", 'r') as noun:
            nounlist = json.load(noun)
            nouns = nounlist["nounwords"]
        with open("share/adjectives.json", 'r') as adjectivejson:
            adjectivelist = json.load(adjectivejson)
            adjectives = adjectivelist["adjectivewords"]
        with open("share/amounts.json", 'r') as amountjson:
            amountlist = json.load(amountjson)
            amounts = amountlist["amountwords"]
        with open("share/starters.json", 'r') as starterjson:
            starterlist = json.load(starterjson)
            starters = starterlist["starterterms"]
        starter0 = starters[random.randint(0, len(starters) - 1)]
        adjective0 = adjectives[random.randint(0, len(adjectives) - 1)]
        adjective1 = adjectives[random.randint(0, len(adjectives) - 1)]
        noun0 = nouns[random.randint(0, len(nouns) - 1)]
        amount0 = amounts[random.randint(0, len(amounts) - 1)]
        if adjective1 == adjective0:
            adjective1 = adjectives[random.randint(0, len(adjectives) - 1)]
        if not adjective0[0] in 'aeiou':
            an0 = 'a'
        else:
            an0 = 'an'
        return "{starter0} {an0} {adjective0} {amount0} 'o {adjective1} {noun0}.".format(starter0=starter0, an0=an0,
                                                                                        adjective0=adjective0,
                                                                                        amount0=amount0,
                                                                                        adjective1=adjective1,
                                                                                        noun0=noun0)

    def on_scheduled_tweet(self):
        text = self.get_insult()
        self.post_tweet(text)

    def on_mention(self, tweet, prefix):
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)

    def on_timeline(self, tweet, prefix):
        pass
        """
        if random.randrange(100) < 2:
            text = self.get_insult()
            self.post_tweet(text, reply_to=tweet)
        else:
            self.favorite_tweet(tweet)
        """

if __name__ == '__main__':
    bot = RoboPirate()
    bot.run()
