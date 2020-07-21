import discord
from discord.ext import commands
import requests
import asyncio
import r6sapi as api
import math
import random
import datetime

up_user = ("email")
up_pword = ("password")
cli_token = ("token")

client = commands.Bot(command_prefix = ';')

async def stats_embed(ctx, ign, iconurl, kills, deaths, kd, wins, losses, winloss, mmr, max_mmr, rank_name):
    embed = discord.Embed(colour=discord.Colour(0xf400ff))

    embed.set_thumbnail(url=(iconurl))
    embed.set_author(name=""+(ign)+"\'s Stats on PC")
    embed.set_footer(text="Combat Stats by @combat#7871")

    embed.add_field(name="Total Kills", value=(kills), inline=True)
    embed.add_field(name="Total Deaths", value=(deaths), inline=True)
    embed.add_field(name="Total Kill / Death", value=(kd), inline=True)
    embed.add_field(name="Ranked Wins", value=(wins), inline=True)
    embed.add_field(name="Ranked Losses", value=(losses), inline=True)
    embed.add_field(name="Ranked Win / Loss", value=(winloss), inline=True)
    embed.add_field(name="Current MMR", value=(mmr), inline=True)
    embed.add_field(name="Max MMR", value=(max_mmr), inline=True)
    embed.add_field(name="Current Rank", value=(rank_name), inline=True)

    await ctx.send(embed=embed)

async def stats_oper(ctx, ign, operator_badge, opname, wins, losses, winloss, kills, deaths, killdeath, time_days):
    embed = discord.Embed(colour=discord.Colour(0xf400ff))

    embed.set_thumbnail(url=(operator_badge))
    embed.set_author(name=""+(ign)+"\'s "+(opname)+" Stats on PC")
    embed.set_footer(text="Combat Stats by @combat#7871")

    embed.add_field(name="Wins", value=(wins), inline=True)
    embed.add_field(name="Losses", value=(losses), inline=True)
    embed.add_field(name="Win / Loss", value=(winloss), inline=True)
    embed.add_field(name="Kills", value=(kills), inline=True)
    embed.add_field(name="Deaths", value=(deaths), inline=True)
    embed.add_field(name="Kill / Death", value=(killdeath), inline=True)
    embed.add_field(name="Time Played (hh:mm:ss)", value=(time_days))

    await ctx.send(embed=embed)


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
    embed=discord.Embed(title="Add me to your server!", url="http://stats.cm-bt.com", color=0xf400ff)
    embed.set_author(name="Commands for Combat Stats")
    embed.add_field(name="My prefix is `;`", value="Use it to call me in the following commands.", inline=False)
    embed.add_field(name="To show PC stats, type:", value="`;pc <UPlay Name>`", inline=False)
    embed.add_field(name="To show Xbox stats, type:", value="`;xb <Xbox Gamertag>`", inline=False)
    embed.add_field(name="To show Playstation stats, type:", value="`;ps <PSN Name>`", inline=False)
    embed.add_field(name="Add an operator to show operator stats!", value="For example: `;pc siege_player sledge`", inline=False)
    embed.set_footer(text="Combat Stats by @combat#7871")
    await ctx.send(embed=embed)

@client.command()
async def pc(ctx, username, op="default"):
    async def run_general(player_batch):
        await player_batch.load_general()
        
        if op == "default":
            for player in player_batch:
                ranks = await player_batch.get_rank(api.RankedRegions.EU)
                rank = ranks[player.id]

                ign = (player.name)
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
                
                
                await stats_embed(ctx, ign, iconurl, kills, deaths, kd, wins, losses, winloss, mmr, max_mmr, rank_name)
                
        else:
            await player_batch.load_all_operators()
            for player in player_batch:
                oper = await player.get_operator(op)

                ign = (player.name)
                opname = (oper.name).title()
                wins = (oper.wins)
                losses = (oper.losses)
                if losses == 0:
                    winlossfull = wins / 1

                else:
                    winlossfull = wins / losses

                winloss = round(winlossfull, 3)

                kills = (oper.kills)
                deaths = (oper.deaths)
                if deaths == 0:
                    killdeathfull = kills / 1

                else:
                    killdeathfull = kills / deaths

                killdeath = round(killdeathfull, 3)
                
                time = float(oper.time_played)
                day = time // (24 * 3600)
                time = time % (24 * 3600)
                hour = time // 3600
                time %= 3600
                minutes = time // 60
                time %= 60
                seconds = time
                time_days = str("%d:%d:%d:%d" % (day, hour, minutes, seconds))

                
                operator_badge = await auth.get_operator_badge(op)

                await stats_oper(ctx, ign, operator_badge, opname, wins, losses, winloss, kills, deaths, killdeath, time_days)
                

        
        
        
    async def run():
        global auth
        auth = api.Auth(up_user, up_pword)

        player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.UPLAY)

        await run_general(player_batch)

        await auth.close()

    
        
    asyncio.get_event_loop().run_until_complete(run())


    
@client.command()
async def xb(ctx, username, op="default"):
    async def run_general(player_batch):
        await player_batch.load_general()
        
        if op == "default":
            for player in player_batch:
                ranks = await player_batch.get_rank(api.RankedRegions.EU)
                rank = ranks[player.id]

                ign = (player.name)
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
                
                
                await stats_embed(ctx, ign, iconurl, kills, deaths, kd, wins, losses, winloss, mmr, max_mmr, rank_name)

        else:
            await player_batch.load_all_operators()
            for player in player_batch:
                oper = await player.get_operator(op)

                ign = (player.name)
                opname = (oper.name).title()
                wins = (oper.wins)
                losses = (oper.losses)
                
                if losses == 0:
                    winlossfull = wins / 1
                else:
                    winlossfull = wins / losses
                    
                winloss = round(winlossfull, 3)
                kills = (oper.kills)
                deaths = (oper.deaths)
                
                if deaths == 0:
                    killdeathfull = kills / 1
                else:
                    killdeathfull = kills / deaths
                    
                killdeath = round(killdeathfull, 3)
                time = str(datetime.timedelta(seconds=(oper.time_played)))
                operator_badge = await auth.get_operator_badge(op)
                await stats_oper(ctx, ign, operator_badge, opname, wins, losses, winloss, kills, deaths, killdeath, time_days)
    
    async def run():
        global auth
        auth = api.Auth(up_user, up_pword)

        player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.XBOX)

        await run_general(player_batch)

        await auth.close()

    
        
    asyncio.get_event_loop().run_until_complete(run())


    
@client.command()
async def ps(ctx, username, op="default"):
    async def run_general(player_batch):
        await player_batch.load_general()
        
        if op == "default":
            for player in player_batch:
                ranks = await player_batch.get_rank(api.RankedRegions.EU)
                rank = ranks[player.id]

                ign = (player.name)
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
                
                
                await stats_embed(ctx, ign, iconurl, kills, deaths, kd, wins, losses, winloss, mmr, max_mmr, rank_name)

        else:
            await player_batch.load_all_operators()
            for player in player_batch:
                oper = await player.get_operator(op)

                ign = (player.name)
                opname = (oper.name).title()
                wins = (oper.wins)
                losses = (oper.losses)
                if losses == 0:
                    winlossfull = wins / 1

                else:
                    winlossfull = wins / losses

                winloss = round(winlossfull, 3)

                kills = (oper.kills)
                deaths = (oper.deaths)
                if deaths == 0:
                    killdeathfull = kills / 1

                else:
                    killdeathfull = kills / deaths

                killdeath = round(killdeathfull, 3)
                
                time = str(datetime.timedelta(seconds=(oper.time_played)))
                operator_badge = await auth.get_operator_badge(op)

                await stats_oper(ctx, ign, operator_badge, opname, wins, losses, winloss, kills, deaths, killdeath, time_days)
                

        
        
        
    async def run():
        global auth
        auth = api.Auth(up_user, up_pword)

        player_batch = await auth.get_player_batch(names=[(username)], platform=api.Platforms.PLAYSTATION)

        await run_general(player_batch)

        await auth.close()

    
        
    asyncio.get_event_loop().run_until_complete(run())


    

    
client.run(cli_token)
