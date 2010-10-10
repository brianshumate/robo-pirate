Robo Pirate (@robo_pirate)
==========================

Robo pirate is a Twitter bot that is based on the [@insult_bird](http://twitter.com/insult_bird) Twitter bot code by [Brent Woodruff](http://www.brentwoodruff.com/).

Now With oAuth Support!

The aim of Robo Pirate is to insult tweeps in the following ways:

* Upon execution, all replies made to @robo_pirate will be met w/ a reply.
* Upon execution, if `@robo_pirate` receives no @ replies, it picks a random tweep that `@robo_pirate` is following, and insults them.
* Upon execution, insults all tweeps that follow, but who cannot be followed. (`@robo_pirate` don't need your protected tweet havin' ass!)
* BONUS: If tweep is particularly harsh in their reply, and the reply contains as string like 'fuck you', `@robo_pirate` replies with "No, fuck YOU!" (for optional great justice).

Running Robo Pirate in Virtualenv
---------------------------------

1. Get virtualenv[1]
2. Create a virtualenv
3. Install pip[2]
4. Install a recent Python Twitter[3] with OAUTH support
5. Configure and edit the script (see details below)
6. Run the script
7. Celebrate good times... C'MON!

Configure the script
--------------------

Edit robo_pirate.py and change the following variable values:

 * `consumer_key`: Replace with your Twitter account's oAuth key
 * `consumer_secret`: Replace with your Twitter account's oAuth secret
 * `access_token`: Replace with your Twitter account's oAuth access token
 * `access_token_secret`: Replace with your Twitter account's oAuth access token secret
 * `store_filename`: (optional) Specify pickle storage file name.
 * `username`: The Twitter account username

See [4] for information on setting up oAuth.

> Please edit the different dictionaries which make up the bot's lexicon to create a unique personality for your bot, and don't just make a clone of robo_pirate itself.

**Feel free follow the actual [@insult_bird](http://twitter.com/insult_bird) and [@robo_pirate](http://twitter.com/robo_pirate) bots on Twitter!**

Thanks - share and enjoy! :)

[1] http://pypi.python.org/pypi/virtualenv
[2] http://pypi.python.org/pypi/pip
[3] http://code.google.com/p/python-twitter/
[4] http://jmillerinc.com/2010/05/31/twitter-from-the-command-line-in-python-using-oauth/