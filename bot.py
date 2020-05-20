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
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour(0xa2599d))

    embed.set_author(name="Commands for Combat Stats Bot", url="https://www.cm-bt.com")
    embed.set_footer(text="Combat Stats Bot - @combat#7871")

    embed.add_field(name="Use the prefix `;` to call me.", value="This cannot yet be changed.\n\n")
    embed.add_field(name="`;pc`", value="Shows stats from the PC version of R6S.")
    embed.add_field(name="`;xb`", value="Shows stats from the Xbox version of R6S.")
    embed.add_field(name="`;ps`", value="Shows stats from the Playstation version of R6S.")
    embed.add_field(name="After typing platform, type your username and your region:", value="`;pc combat_stats na`")
    embed.add_field(name="If you specify no region, it will default to EU.", value="\n*Thank you for using my bot!*")

    await ctx.send(embed=embed)

@client.command()
async def pc(ctx, username, region="EU"):
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
async def xb(ctx, username, region="EU"):
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
                embed.set_author(name="NA Xbox Stats for "+(username))
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
async def ps(ctx, username, region="EU"):
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
                embed.set_author(name="NA Playstation Stats for "+(username))
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
