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
        self.config['tweet_interval'] = 42 * 60     # default: 30 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
        self.config['tweet_interval_range'] = None

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = True

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = False

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = []

        # follow back all followers?
        self.config['autofollow'] = False


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

    def get_insult(wat):
        # print wat
        starters = ['Ahoy! Ye be', 'Arrr! Thar be', 'Avast! Ye be', 'Avast! Ye be more foul \'an', 'Avast! Thar be', 'Avast! Ye be resemblin\'', 'Aye! No doubt ye be', 'By my reckonin\' ye be', 'Blimey! Ye \'ppear t\' be', 'Come now, fer ye be', 'D\'ye see?! Ye must be', 'Sail ho! Yer filthier \'an', 'Scupper that \'an begone! Ye be', 'Holloa! Ye be', 'How are \'ee?! Ye be', 'Shiver me timbers! Ye be', 'Show a leg! Fer ye surely be', 'Sink me! Ye be', 'Stay yer tears! Ye be', 'Stint yer clack! Ye be', 'Stop yer clapper! Ye be', 'Yo ho! Ye be', 'Yo ho! Thar be', 'Yarrr! Ye be filthier \'an', 'Blimey! Ye be filthier \'an', 'Avast! Ye be filthier \'an', 'Yo ho! Ye be filthier \'an', 'Avast! Ye be nastier \'an', 'Yarrr! Ye be nastier \'an', 'Yo ho! Ye be nastier \'an', 'Blimey! Ye be nastier \'an', 'Yo ho ho! Ye be', 'Aye! Ye be!', 'Ye be remindin\' me of',]
        nouns = ['backsides', 'barkadeers', 'bilge waters', 'ballast pigs', 'barnacles', 'bowsprits', 'belayin\' pins', 'bilge drinkers', 'bilge rats', 'black spots', 'blaggards',  'blowfishes',  'boatswains', 'boat hooks', 'bones', 'buccaneers', 'butts', 'buttles', 'buttcabbages', 'buttnapkinsmythes', 'buttankards', 'buttossacks', 'buttards', 'cabin boys', 'carousers', 'castaways', 'cat o\' nine tails', 'chandlers', 'cogs', 'curs', 'cusses', 'dandies',  'deadlights', 'doxies', 'fish gizzards' 'freebooters', 'Frenchmen',  'futtocks', 'gangplanks', 'gibbits', 'gibbit cages', 'gizzards', 'grog blossoms', 'hawseholes', 'hempen jigs', 'hempen halters', 'hogsheads', 'holystones', 'horn swoggler', 'hulks', 'humdingers', 'interlopers', 'Jack Ketches', 'knaves', 'killicks', 'lads', 'luggers', 'lynch baits', 'poop decks', 'jim lads', 'krakens', 'landlubbers', 'lasses', 'lassies', 'lassie-lenders', 'lubbers', 'marroons', 'parrots', 'petards', 'picaroons', 'powder chests', 'peglegs', 'powder monkeys', 'pressganngs', 'privateers', 'private parts', 'privy parts',  'rapscallions', 'rope burns', 'sandcrabs', 'sassielassies', 'saw bones', 'scallywags', 'scoundrels', 'scurvy dogs', 'sea lice', 'six pounders', 'smythes', 'smythesackers', 'smythesluggers', 'smytheslorpers', 'spankers', 'strike colors', 'sea bass', 'sea dogs', 'sea witches', 'scuttle hounds', 'sluggards', 'sunken skulls', 'strumpets', 'swabbies',  'stumps', 'swashers', 'swine', 'tar stains', 'tarts', 'tarty mermaids', 'twitterfools', 'tweeples', 'tweeps', 'twenches', 'twittles', 'twittlesmiths', 'twittlesmythes', 'twits', 'wenches', 'wherries',
            ]
        amounts = ['barrel', 'cask', 'chest', 'draught', 'fathom', 'full hold', 'hull full',  'keg', 'keg full', 'league', 'motherload', 'tankard', 'stein', 'sea chest',]
        adjectives = ['addle brained', 'barnacle bottomed', 'becalmed', 'bedraggled', 'b\'tween decks', 'black eyed', 'black toothed', 'blood thirsty', 'barnacled', 'barrel belly\'d', 'black hearted', 'blubberin\'', 'bow legged', 'brine crusted', 'chicken hearted', 'confounded', 'crows footed', 'drunken', 'flea bitten', 'floggish', 'fog bound', 'furlish', 'gibbitly', 'gibbitish', 'goutish', 'gout-toed', 'green gilled', 'green limbed', 'groggy', 'grog brained', 'grog headed', 'groggish', 'grog swiggin\'', 'grog snarfin\'', 'handsomely', 'hoggish', 'hornswagglish', 'horn swogglin\'', 'hulkish', 'knock kneed', 'lead slingin\'',  'lice infested', 'lily livered', 'lily sniffin\'', 'luggish', 'marroonish', 'mast huggin\'', 'one armed', 'one legged', 'one toed', 'peglegged', 'pigeon toed', 'parrot lubbin\'', 'plunderin\'', 'plunderish', 'powder wettin\'', 'pox faced', 'pox infested', 'rot mouth\'d', 'scrappy', 'scrappish', 'keelhaulish', 'motherload-ish', 'mutinous', 'rum swiggin\'', 'salt crusted', 'scutt\'ly', 'scuttlish', 'scurvish', 'scurvy', 'skirt wearin\'', 'square-rigged', 'squiffy', 'stinkin\'', 'swabbish', 'swaggardly', 'swiney', 'tar stain\'d', 'thunderin\'', 'tweetish', 'twittish', 'wind blown', 'worm infested', 'worm riddled', 'yellow', 'yellow-bell\'yd',]
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
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)


if __name__ == '__main__':
    bot = RoboPirate()
    bot.run()
