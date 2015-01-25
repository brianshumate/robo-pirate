
```
				 ____       _             ____  _           _
				|  _ \ ___ | |__   ___   |  _ \(_)_ __ __ _| |_ ___
				| |_) / _ \| '_ \ / _ \  | |_) | | '__/ _` | __/ _ \
				|  _ < (_) | |_) | (_) | |  __/| | | | (_| | ||  __/
				|_| \_\___/|_.__/ \___/  |_|   |_|_|  \__,_|\__\___|

                       .ed"""" """$$$$be.
                     -"           ^""**$$$e.
                   ."                   '$$$c
                  /                      "4$$b
                 d  3                     $$$$
                 $  *                   .$$$$$$
                .$  ^c           $$$$$e$$$$$$$$.
                d$L  4.         4$$$$$$$$$$$$$$b
                $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
    e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
   z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
  4$$$$L   \     $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
  ^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
    "**$$$ec   "\   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
          "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
            ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
               "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
                 "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                    "$   "%*ebJLzb$e$$$$$b $P"
                      %..      4$$$$$$$$$$ "
                       $$$e   z$$$$$$$$$$%
                        "*$c  "$$$$$$$P"
                         ."""*$$$$$$$$bc
                      .-"    .$***$$$"""*e.
                   .-"    .e$"     "*$c  ^*b.
            .=*""""    .e$*"          "*bc  "*$e..
          .$"        .z*"               ^*$e.   "*****e.
          $$ee$c   .d"                     "*$.        3.
          ^*$E")$..$"                         *   .ee==d%
             $.d$$$*                           *  J$$$e*
              """""                             "$$$"   Gilo95'


```

This is the source for [@robo-pirate](https://twitter.com/robo-pirate/with_replies), a Twitter
bot whose one sole purpose is to insult Twitter users in a particularly
pirate-y manner.

## Setup

### Note

Replace all instances of *robo-pirate* in this project with the name of
your own bot to begin making use of this code for yourself.

Use `virtualenv` and `virtualenvwrapper` because Python is more fun with them.

Clone this repository, the change into its top level directory:

```
git clone https://github.com/brianshumate/robo-pirate.git
cd robo-pirate
```

Then, to quote the venerable @densoneold,

> commands

```
mkvirtualenv robo-pirate
pip install -r requirements.txt
cp robo-pirate/etc/access.json-dist robo-pirate/etc/access.json
```

Finally, edit `etc/access.json` and plug in your Twitter API keys, tokens,
and secrets.

## Usage

Run it like this:

```
./robo-pirate.py
```

## Thank You

- [Brent Woodruff](https://twitter.com/fprimex): Long time friend, Twitter bot collaborator and influence
- [@thricedotted](https://twitter.com/thricedotted): For their cool [twitterbot](https://github.com/thricedotted/twitterbot) framework that Robo Pirate uses! <3
- [Darius Kazemi](https://twitter.com/tinysubversions): Twitter bot artiste extraordinaire and constant inspiration
