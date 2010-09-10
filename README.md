Robo Pirate
===========

Robo pirate is a Twitter bot that is based on the @insult_bird
Twitter bot code by [Brent Woodruff](http://www.brentwoodruff.com/).

The aim of Robo Pirate is to insult tweeps in the following ways:

* All replies made to @robo_pirate will be met w/ a retort
* A random person he is following will get insult if no @ replies
* Continuously insults tweeps that follow him, but who he cannot follow
* BONUS: If tweep is particularly harsh in their reply, and it contains ~'Fuck you', @robo_pirate replies "No, fuck YOU!" (for optional great justice).

Running Robo Pirate in Virtualenv
---------------------------------

1. Get virtualenv
2. Create a virtualenv
3. Install pip
4. Install Python Twitter
5. Configure and edit the script (see details below)
6. Run the script
7. Celebrate good times... C'MON!

Configure the script
--------------------

Edit robo_pirate.py and change the following variable values:

 * `username`: Replace `TWITTER_NICK` with your bot's Twitter user name.
 * `password`: Replace `CHANGEME with` your bot's Twitter password.
 * `store_filename`: (optional) Specify pickle storage file name.
 
> Please edit the different dictionaries which make up the bot's lexicon to create a unique personality for your bot, and don't just make a clone of robo_pirate itself.

Thanks - share and enjoy! :)