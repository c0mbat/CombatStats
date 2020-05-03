import discord
from discord.ext import commands
import logging
from threading import Thread
import requests
import json
import asyncio
import r6sapi as api
from contextlib import suppress
import math
import random

#logging
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot user ready")

@client.command()
async def ping(ctx):
    await ctx.send("Pong")
    


@client.command()
async def stats(ctx, username, region="EU"):
    with suppress(Exception):
        if region == "EU" or region == "eu":
            async def run_general(player_batch):
                await player_batch.load_general()
                

                for player in player_batch:
                    ranks = await player_batch.get_rank(api.RankedRegions.EU)
                    rank = ranks[player.id]

                    wins = (rank.wins)
                    losses = (rank.losses)
                    mmr = math.trunc(rank.mmr)
                    max_mmr = math.trunc(rank.max_mmr)
                    rank_name = (rank.rank)
                    iconurl = (rank.get_icon_url())
                    if losses == 0:
                        winlossfull = wins / 1

                    else:
                        winlossfull = wins / losses
                    winloss = round(winlossfull, 3)
                    
                    deaths = (player.deaths)
                    kills = (player.kills)
                    kd_full = kills / deaths
                    kd = round(kd_full, 3)
                    

                    embed = discord.Embed(colour=discord.Colour(0xf400ff))

                    embed.set_thumbnail(url=(iconurl))
                    embed.set_author(name="EU Stats for "+(username))
                    embed.set_footer(text="Rob's Discord Stats Bot - @combat#7871")

                    embed.add_field(name="Total Kills", value=(kills), inline=True)
                    embed.add_field(name="Total Deaths", value=(deaths), inline=True)
                    embed.add_field(name="Total KD Ratio", value=(kd), inline=False)
                    embed.add_field(name="Ranked Wins", value=(wins), inline=True)
                    embed.add_field(name="Ranked Losses", value=(losses), inline=True)
                    embed.add_field(name="Ranked Win / Loss", value=(winloss), inline=True)
                    embed.add_field(name="Current MMR", value=(mmr), inline=True)
                    embed.add_field(name="Max MMR", value=(max_mmr), inline=True)
                    embed.add_field(name="Current Rank", value=(rank_name), inline=True)

                    await ctx.send(embed=embed)

            async def run():
                auth = api.Auth("robin_hugill@hotmail.com", "Prince_2007")

                player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.UPLAY)

                await run_general(player_batch)

                await auth.close()

            
                
            asyncio.get_event_loop().run_until_complete(run())

        if region == "NA" or region == "na":
            async def run_general(player_batch):
                await player_batch.load_general()
                

                for player in player_batch:
                    ranks = await player_batch.get_rank(api.RankedRegions.NA)
                    rank = ranks[player.id]
                    
                    wins = (rank.wins)
                    losses = (rank.losses)
                    mmr = math.trunc(rank.mmr)
                    max_mmr = math.trunc(rank.max_mmr)
                    rank_name = (rank.rank)
                    iconurl = (rank.get_icon_url())
                    if losses == 0:
                        winlossfull = wins / 1

                    else:
                        winlossfull = wins / losses
                    winloss = round(winlossfull, 3)
                    
                    deaths = (player.deaths)
                    kills = (player.kills)
                    kd_full = kills / deaths
                    kd = round(kd_full, 3)
                    

                    embed = discord.Embed(colour=discord.Colour(0xf400ff))

                    embed.set_thumbnail(url=(iconurl))
                    embed.set_author(name="NA Stats for "+(username))
                    embed.set_footer(text="Rob's Discord Stats Bot - @combat#7871")

                    embed.add_field(name="Total Kills", value=(kills), inline=True)
                    embed.add_field(name="Total Deaths", value=(deaths), inline=True)
                    embed.add_field(name="Total KD Ratio", value=(kd), inline=False)
                    embed.add_field(name="Ranked Wins", value=(wins), inline=True)
                    embed.add_field(name="Ranked Losses", value=(losses), inline=True)
                    embed.add_field(name="Ranked Win / Loss", value=(winloss), inline=True)
                    embed.add_field(name="Current MMR", value=(mmr), inline=True)
                    embed.add_field(name="Max MMR", value=(max_mmr), inline=True)
                    embed.add_field(name="Current Rank", value=(rank_name), inline=True)

                    await ctx.send(embed=embed)

            async def run():
                auth = api.Auth("email", "password")

                player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.UPLAY)

                await run_general(player_batch)

                await auth.close()

            
                
            asyncio.get_event_loop().run_until_complete(run())
        
       
            
    
    
client.run('token')
