#!/usr/bin/env python
"""
robo_pirate.py
"""
import sys
import re
import random
import urllib2
import cPickle as pickle
import twitter
from sets import Set  

random.seed()
  
username = 'twitter_nick'
password = CHANGEME'
store_filename = '/path/to/pickle_store.file'
re_fu = re.compile("^.*fuck[\s|!|.]*you.*$", flags=re.I)

def get_insult():
    starters = ['Ahoy! Ye be', 'Arrr! Thar be', 'Avast! Ye be', 'Avast! Ye be more foul \'an', 'Avast! Thar be', 'Avast! Ye be resemblin\'', 'Aye! No doubt ye be', 'By my reckonin\' ye be', 'Blimey! Ye \'ppear t\' be', 'Come now, fer ye be', 'D\'ye see?! Ye be', 'Sail ho! Yer filthier \'an', 'Scupper that \'an begone! Ye be', 'Holloa! Ye be', 'How are \'ee?! Ye be', 'Shiver me timbers! Ye be', 'Show a leg! Fer ye be', 'Sink me! Be it', 'Stay yer tears! Ye be', 'Stint yer clack! Ye be', 'Stop yer clapper! Ye be', 'Yo ho! Ye be', 'Yo ho! Thar be', 'Yarrr! Ye be filthier \'an', 'Blimey! Ye be filthier \'an', 'Avast! Ye be filthier \'an',  'Yo ho! Ye be filthier \'an', 'Avast! Ye be nastier \'an', 'Yarrr! Ye be nastier \'an', 'Yo ho! Ye be nastier \'an', 'Blimey! Ye be nastier \'an',]
    nouns = ['backsides', 'barkadeers', 'bilge waters', 'ballast pigs', 'barnacles', 'bowsprits', 'belayin\' pins', 'bilge drinkers', 'bilge rats', 'black spots', 'blaggards',  'blowfishes',  'boatswains', 'boat hooks', 'bones', 'buccaneers', 'butts', 'cabin boys', 'carousers', 'castaways', 'cat o\' nine tails', 'chandlers', 'cogs', 'curs', 'cusses', 'dandies',  'deadlights', 'doxies', 'fish gizzards' 'freebooters', 'Frenchmen',  'futtocks', 'gangplanks', 'gibbits', 'gibbit cages', 'gizzards', 'grog blossoms', 'hawseholes', 'hempen jigs', 'hempen halters', 'hogsheads', 'holystones', 'horn swoggler', 'hulks', 'interlopers', 'Jack Ketches', 'knaves', 'killicks', 'lads', 'luggers', 'lynch baits', 'poop decks', 'jim lads', 'krakens', 'landlubbers', 'lasses', 'lassies', 'lubbers', 'marroons', 'parrots', 'petards', 'picaroons', 'powder chests', 'peglegs', 'powder monkeys', 'pressganngs', 'privateers', 'privy parts',  'rapscallions', 'rope burns', 'sandcrabs', 'saw bones', 'scallywags', 'scoundrel', 'scurvy dogs', 'sea lice', 'six pounders', 'spankers', 'strike colors', 'sea bass', 'sea dogs', 'sea witches', 'scuttle hounds', 'sluggards', 'sunken skulls', 'strumpets', 'swabbies',  'stumps', 'swashers', 'swine', 'tar stains', 'tarts', 'tarty mermaids', 'twitterfools', 'twits', 'wenches', 'wherries',
        ]
    amounts = ['barrel', 'cask', 'chest', 'draught', 'fathom', 'full hold', 'hull full',  'keg', 'keg full', 'league', 'motherload', 'tankard', 'stein', 'sea chest',]
    adjectives = ['addle brained', 'barnacle bottomed', 'becalmed', 'bedraggled', 'b\'tween decks', 'black eyed', 'black toothed', 'blood thirsty', 'barancled', 'barrel belly\'d', 'black hearted', 'blubberin\'', 'bow legged', 'brine crusted', 'chicken hearted', 'confounded', 'crows footed', 'drunken', 'flea bitten', 'floggish', 'fog bound', 'furlish', 'gibbitly', 'gibbitish', 'goutish', 'gout-toed', 'green gilled', 'green limbed', 'groggy', 'grog brained', 'grog headed', 'groggish', 'grog swiggin\'', 'grog snarfin\'', 'handsomely', 'hoggish', 'hornswagglish', 'horn swogglin\'', 'hulkish', 'knock kneed', 'lead slingin\'',  'lice infested', 'lily livered', 'lily sniffin\'', 'luggish', 'marroonish', 'mast huggin\'', 'one armed', 'one legged', 'one toed', 'peglegged', 'pigeon toed', 'parrot lovin\'', 'plunderin\'', 'plunderish', 'powder wettin\'', 'pox faced', 'pox infested', 'rot mouth\'d', 'scrappy', 'scrappish', 'keelhaulish', 'motherload-ish', 'mutinous', 'rum swiggin\'', 'salt crusted', 'scutt\'ly', 'scuttlish', 'scurvish', 'scurvy', 'skirt wearin\'', 'square-rigged', 'squiffy', 'stinkin\'', 'swabbish', 'swaggardly', 'swiney', 'tar stain\'d', 'thunderin\'', 'tweetish', 'twittish', 'wind blown', 'worm infested', 'worm riddled', 'yellow', 'yellow-bell\'yd',]
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

    return '%s %s %s %s o %s %s.' % (starter, an, adj1, amount, adj2, noun)

try:
    store_file = open(store_filename, 'rb')
    store = pickle.load(store_file)
except IOError:
    # we're at the point now that it would be disasterous to
    # reply to everything since the beginning
    store = { 'last_reply_id':None, 'last_dm_id':None, }
except pickle.PickleError:
    sys.exit(1)

api = twitter.Api(username=username, password=password)  
  
following = api.GetFriends()
friend_names = Set()
for friend in following:
    friend_names.add(friend.screen_name)
  
followers = api.GetFollowers()
for follower in followers:
    if (not follower.screen_name in friend_names):
        try:
            api.CreateFriendship(follower.screen_name)
            print "Created friendship with " + follower.screen_name
        except urllib2.HTTPError:
            msg = "@" + follower.screen_name + " "
            msg += get_insult()
            #api.PostUpdate(msg)
            print "Unable to follow " + follower.screen_name + ": " + msg

for friend in friend_names:
    print friend

print "Getting replies since: " + repr(store['last_reply_id'])
replies = api.GetReplies(since_id=store['last_reply_id'])
for reply in replies:
    if not reply.user.screen_name == username:
        if reply.id > store['last_reply_id']:
            store['last_reply_id'] = reply.id
        reply_msg = "@" + reply.user.screen_name + " "
        if re_fu.match(reply.text):
            reply_msg += "no, FUCK YOU!"
        else:
            reply_msg += get_insult()
        api.PostUpdate(reply_msg, in_reply_to_status_id=reply.id)
        print "Posted reply to " + repr(reply.id) + ":" + reply_msg

print "Getting direct messages since: " + repr(store['last_dm_id'])
dms = api.GetDirectMessages(since_id=store['last_dm_id'])
for dm in dms:
    if not dm.sender_screen_name == username:
        if dm.id > store['last_dm_id']:
            store['last_dm_id'] = dm.id
        msg = " "
        if re_fu.match(dm.text):
            msg += "no, FUCK YOU!"
        else:
            msg += get_insult()
	try:
        	api.PostDirectMessage(dm.sender_screen_name, msg)
	except:
		print "it blowed up at me!"
        print "Posted direct message to " + dm.sender_screen_name + ":" + msg

# Get a random friend and insult them
if len(friend_names) != 0:
    msg = "@" + random.sample(tuple(friend_names), 1)[0] + " " + get_insult()
    api.PostUpdate(msg)
    print "Posted update:" + msg

# Insult all friends
#for friend in friend_names:
#    msg = "@" + friend + " " + get_insult()
#    api.PostUpdate(msg)
#    print "Posting update:" + msg

print store

store_file = open(store_filename, 'wb')
try:
    pickle.dump(store, store_file)
finally:
    store_file.close()

