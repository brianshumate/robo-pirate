#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

import json
import sys
import re
import random
from twitterbot import TwitterBot


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
        self.config['tweet_interval'] = 120 * 60     # 120 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes

        # Tweet range: every 120 to 420 minutes
        self.config['tweet_interval_range'] = (120*60, 420*60)

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = True

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = False

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = False

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = ['pirate', 'robot pirate', 'yarrr']

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

    def get_insult(self):
        with open("etc/nouns.json", 'r') as noun:
            nounlist = json.load(noun)
            nouns = nounlist["nounwords"]
        with open("etc/adjectives.json", 'r') as adjectivejson:
            adjectivelist = json.load(adjectivejson)
            adjectives = adjectivelist["adjectivewords"]
        with open("etc/amounts.json", 'r') as amountjson:
            amountlist = json.load(amountjson)
            amounts = amountlist["amountwords"]
        with open("etc/starters.json", 'r') as starterjson:
            starterlist = json.load(starterjson)
            starters = starterlist["starterterms"]
        starter = starters[random.randint(0, len(starters) - 1)]
        adj1 = adjectives[random.randint(0, len(adjectives) - 1)]
        adj2 = adjectives[random.randint(0, len(adjectives) - 1)]
        noun = nouns[random.randint(0, len(nouns) - 1)]
        amount = amounts[random.randint(0, len(amounts) - 1)]
        if adj1 == adj2:
            adj2 = adjectives[random.randint(0, len(adjectives) - 1)]
        if not adj1[0] in 'aeiou':
            an = 'a'
        else:
            an = 'an'

        return "%s %s %s %s 'o %s %s." % (starter, an, adj1, amount, adj2, noun)

    def on_scheduled_tweet(self):
        """
        Make a public tweet to the bot's own timeline.

        It's up to you to ensure that it's less than 140 characters.

        Set tweet frequency in seconds with TWEET_INTERVAL in config.py.
        """
        text = self.get_insult()
        self.post_tweet(text)

    def on_mention(self, tweet, prefix):
        """
        Defines actions to take when a mention is received.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)

    def on_timeline(self, tweet, prefix):
        """
        Defines actions to take on a timeline tweet.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """

        """
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text

        # let's only reply 70% of the time, otherwise fave the twutt
        def lucky(percent=70):
            return random.randrange(100) < percent

        if lucky():
            self.post_tweet(prefix + ' ' + text, reply_to=tweet)
        else:
            self.favorite_tweet(tweet)
        """
        pass

if __name__ == '__main__':
    bot = RoboPirate()
    bot.run()
