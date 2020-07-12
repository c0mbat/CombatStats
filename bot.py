import discord
from discord.ext import commands
import requests
import asyncio
import r6sapi as api
import math
import random

client = commands.Bot(command_prefix = ';')


@client.event
async def on_ready():
    print("Bot user ready")
    game = discord.Game(";commands for help.")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
@client.command()
async def commands(ctx):
    embed=discord.Embed(title="Add me to your server!", url="https://stats.cm-bt.com", description="Click the link above.", color=0xff85e4)
    embed.set_author(name="Commands for Combat Stats")
    embed.add_field(name="Use my prefix `;` to call me", value="This prefix cannot yet be changed.", inline=False)
    embed.add_field(name="To show PC stats, type:", value="`;pc <UPlay Name>`", inline=False)
    embed.add_field(name="To show Xbox stats, type:", value="`;xb <Xbox Gamertag>`", inline=False)
    embed.add_field(name="To show Playstation stats, type:", value="`;ps <PSN Name>`", inline=False)
    embed.set_footer(text="Combat Stats by @combat#7871")
    await ctx.send(embed=embed)

@client.command()
async def pc(ctx, username):
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
            embed.set_footer(text="Combat Stats Bot - @combat#7871")

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

    
@client.command()
async def xb(ctx, username):
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
            embed.set_author(name="EU Xbox Stats for "+(username))
            embed.set_footer(text="Combat Stats Bot - @combat#7871")

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

        player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.XBOX)

        await run_general(player_batch)

        await auth.close()

    
        
    asyncio.get_event_loop().run_until_complete(run())

@client.command()
async def ps(ctx, username):
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
            embed.set_author(name="EU Playstation Stats for "+(username))
            embed.set_footer(text="Combat Stats Bot - @combat#7871")

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

        player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.PLAYSTATION)

        await run_general(player_batch)

        await auth.close()

    
        
    asyncio.get_event_loop().run_until_complete(run())

    
client.run('token')
