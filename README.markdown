Robo Pirate (@robo_pirate)
==========================

Robo pirate is a Twitter bot that is a harmony of code being primarily
written by [Brent Woodruff](http://www.brentwoodruff.com/) and vocabulary
plus bits of code written by [Brian Shumate](http://brianshumate.com/).

The aim of Robo Pirate is to tweet insult in the following ways:

* All replies made to @robo_pirate will be met w/ a reply.
* If `@robo_pirate` receives no @ replies, it picks a random tweep that `@robo_pirate` is following, and insults them.
* Upon execution, insults all tweeps that follow, but who cannot be followed. (`@robo_pirate` don't need your protected tweet havin' ass!)
* BONUS: If tweep is particularly harsh in their reply, and the reply contains a string resembling *fuck you*, `@robo_pirate` replies with "No, fuck YOU!" (for optional great justice).

## Running Robo Pirate in a Virtualenv

0. Get [virtualenv](http://pypi.python.org/pypi/virtualenv)
1. Create a virtualenv
2. Install a recent [Python Twitter](http://code.google.com/p/python-twitter/) with OAuth2 support
3. Configure and edit the script (see details below)
4. Run the script
5. Celebrate good times... C'MON!

## Configure the script

Edit robo_pirate.py and change the following variable values:

 * `consumer_key`: Replace with your Twitter account's oAuth key
 * `consumer_secret`: Replace with your Twitter account's oAuth secret
 * `access_token`: Replace with your Twitter account's oAuth access token
 * `access_token_secret`: Replace with your Twitter account's oAuth access token secret
 * `store_filename`: (optional) Specify pickle storage file name.
 * `username`: The Twitter account username

See [this resource](http://jmillerinc.com/2010/05/31/twitter-from-the-command-line-in-python-using-oauth/) for information on setting up oAuth with Python.

> Please edit the different dictionaries which make up the bot's lexicon to create a unique personality for your bot, and don't just make a clone of robo_pirate itself.

**Feel free follow the actual [@insult_bird](http://twitter.com/insult_bird) and [@robo_pirate](http://twitter.com/robo_pirate) bots on Twitter or block
them if they're harassing you too much already.**

Thanks - share and enjoy! :)
