import discord
from discord.utils import get
import os
from tools.parser import parse_yaml
from tools.db_setup import conn
from tools.query_generator import query_setup
import pandas as pd
from response.bot_response import get_response

## Configuration
config = parse_yaml('config.yaml')
auth_config = parse_yaml(config.get('PATH_AUTH'))
PATH_QUERY = config.get('PATH_QUERY')

TOKEN_ID = auth_config.get('TOKEN')
client = discord.Client()
member_ver_query = query_setup(PATH_QUERY+"member_verification.sql")

## Main Function
@client.event
async def on_ready():
    print('log in as {0.user}'.format(client))


@client.event
async def on_message(message):
    status_response = 0

    if message.author == client.user:
        return

    ## inspect the message
    if message.content.startswith('$'):
        reply_message, status_response = get_response(message)

    ## reply process
    if status_response == 1:
        await message.channel.send(reply_message)

    elif status_response == 2:
        connection = conn(auth_config)
        discord_id = str(message.author)
        role = get(message.author.guild.roles , name="member")
        all_roles = [i.name for i in message.author.roles]

        if 'member' not in all_roles:
            d = {'DISCORD_ID':discord_id}
            sql_input = member_ver_query.get_query(d)
            dt = pd.read_sql_query(sql_input, connection)
            if len(dt)>0:
                user_dsi = dt['username'].values[0]
                await message.author.add_roles(role)
                reply_message = "Welcome "+user_dsi+". Kamu sudah dipromosikan menjadi Member Server. Sekarang kamu bisa bergabung diberbagai channel diserver ini."
            else:
                reply_message = "Halo "+discord_id+". Kamu belum mendaftarkan discord id kamu ke datascience.or.id. "
                reply_message = reply_message + "Tolong daftarkan di isian 'telegram'. Jika sudah terlanjur terisi dengan telegram id, tolong diganti dengan discord id. "
                reply_message = reply_message + "Contoh discord id: steward_dsi#9568. "
                reply_message = reply_message + "Setelah itu ketik $promote kembali. "
                reply_message = reply_message + "Untuk lebih detilnya, bisa kunjungi : bit.ly/dsidiscord1"
        else:
            reply_message = "Halo "+discord_id+'''. Kamu sudah dipromosikan. Untuk Role yang lebih, bisa hubungi @admin.'''
        
        await message.channel.send(reply_message)

client.run(TOKEN_ID)
