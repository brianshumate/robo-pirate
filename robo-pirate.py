#!/usr/bin/env python2
"""
This is @robo_pirate.

Yarrr, matey.
"""
# -*- coding: utf-8 -*- #

import json
from random import randint
# from os.path import expanduser

from twitterbot import TwitterBot


class RoboPirate(TwitterBot):
    """Bot class."""

    def bot_init(self):
        """Initialize and configure bot."""
        with open("etc/access.json", 'r') as access:
            authdb = json.load(access)

        self.config['api_key'] = authdb["API_Key"]
        self.config['api_secret'] = authdb["API_Secret"]
        self.config['access_key'] = authdb["Access_Token"]
        self.config['access_secret'] = authdb["Access_Token_Secret"]

        # Baseline tweet frequency, in seconds
        self.config['tweet_interval'] = 42 * 60  # 42 minutes

        # Tweet range: every 42 to 90 minutes
        self.config['tweet_interval_range'] = (42 * 60, 90 * 60)

        # Reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # Include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = False

        # Like any tweets that mention this bot?
        self.config['autofav_mentions'] = True

        # Like any tweets containing these keywords?
        self.config['autofav_keywords'] = ['matey',
                                           'pirate',
                                           'robot pirate',
                                           'yarrr',
                                           'treasue']

        # follow back all followers?
        self.config['autofollow'] = False

        # Log path
        # home = expanduser("~")
        self.config['log_path'] ='/home/brian/var/bot_logs/'

        # What's up with reply interval?
        # self.config['reply_interval'] = 7 * 60

    def get_insult(self):
        """Generate insult."""
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
        starter0 = starters[randint(0, len(starters) - 1)]
        adj0 = adjectives[randint(0, len(adjectives) - 1)]
        adj1 = adjectives[randint(0, len(adjectives) - 1)]
        noun0 = nouns[randint(0, len(nouns) - 1)]
        amount0 = amounts[randint(0, len(amounts) - 1)]
        if adj1 == adj0:
            adj1 = adjectives[randint(0, len(adjectives) - 1)]
        if not adj0[0] in 'aeiou':
            an0 = 'a'
        else:
            an0 = 'an'
        twutt = "{starter0} {an0} {adj0} {amount0} 'o {adj1} {noun0}."
        return twutt.format(starter0=starter0,
                            an0=an0,
                            adj0=adj0,
                            amount0=amount0,
                            adj1=adj1,
                            noun0=noun0)

    def on_scheduled_tweet(self):
        """Scheduled public tweet."""
        text = self.get_insult()
        self.post_tweet(text)

    def on_mention(self, tweet, prefix):
        """Reply to @ mention."""
        text = self.get_insult()
        # prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)

    def on_timeline(self, tweet, prefix):
        """
        Randomly reply to timeline items.

        Make this walk the plank if it causes too much API usage
        """
        """
        if randint(0, 100) < 2:
            text = self.get_insult()
            self.post_tweet(text, reply_to=tweet)
        else:
            self.favorite_tweet(tweet)
        """

if __name__ == '__main__':
    bot = RoboPirate()
    bot.run()
