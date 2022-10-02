# Steward DSI

This is Discord Bot of Data Science Indonesia. The bot have several functions to work with for Data Science Indonesia community in Discord.
We are welcoming everyone to contribute more in this repo to make the bot better. Please join our discord [here](bit.ly/discord-dsi-on) to get more action with the bot.

## Running bot

setup the `auth_config.yaml` with this format :

```
TOKEN : <discord token from>
HOST : <db host IP for $promote function>
USER : <db user for $promote function>
PASS : <db password for $promote function>
DBNAME : <db name for $promote function>
```

Then run the following script :

```
pip install virtualenv
virtualenv stew-v
source stew-v/bin/activate
pip install -r requirements.txt
python main.py
```

## Bot Functions

| Syntax      | Description |
| ----------- | ----------- |
| $welcome    | Welcoming you in DSI discord  |
| $halo       | Generating random reply from Bot |
| $promote    | Promoting an account having a `member` role |

PS: $promote is special function which connect to DSI database. You can ignore this function while testing the bot in your local.

## Contribution

[WIP]

## Reference

* Join [Our Discord](bit.ly/discord-dsi-on)
* [Discord with Python](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
* Discord [Color API](https://discordpy.readthedocs.io/en/latest/api.html#discord.User.color)

