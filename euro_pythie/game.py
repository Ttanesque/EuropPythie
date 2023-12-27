from interactions import (
    Extension,
    slash_command,
    SlashCommand,
    SlashCommandOption,
    OptionType,
    SlashContext,
    Embed,
    Member,
)
from interactions.ext.paginators import Paginator
from datetime import date
from log import command as log
from rapidfuzz import process, fuzz, utils
from config import game
import interactions
import database
import sqlite3


class Game(Extension):
    game = SlashCommand(
        name="game",
        description="Game management command",
    )

    @game.subcommand(
        sub_cmd_name="create",
        options=[
            SlashCommandOption(
                name="g_name",
                description="Name of the game",
                type=OptionType.STRING,
                required=True,
            ),
            SlashCommandOption(
                name="player1",
                description="Player 1",
                type=OptionType.USER,
                required=True,
            ),
            SlashCommandOption(
                name="player2",
                description="Player 2",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player3",
                description="Player 3",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player4",
                description="Player 4",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player5",
                description="Player 5",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player6",
                description="Player 6",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player7",
                description="Player 7",
                type=OptionType.USER,
                required=False,
            ),
            SlashCommandOption(
                name="player8",
                description="Player 8",
                type=OptionType.USER,
                required=False,
            ),
        ],
    )
    async def create_game(
        self,
        ctx: SlashContext,
        g_name: str,
        player1: Member,
        player2=None,
        player3=None,
        player4=None,
        player5=None,
        player6=None,
        player7=None,
        player8=None,
    ):
        raw_players = [
            player1,
            player2,
            player3,
            player4,
            player5,
            player6,
            player7,
            player8,
        ]
        players = [s.mention for s in raw_players if s != None]

        log.debug("%s", players)
        try:
            database.saveGames(
                g_name, date.today().strftime("%d-%m-%Y"), ",".join(players)
            )
        except sqlite3.Error as er:
            log.error("Issue when save data {}", err)
            await ctx.send("Database error the game has not been saved")
            return

        await ctx.send(str.format("Game {} saved", g_name))

    @game.subcommand(
        sub_cmd_name="ls", sub_cmd_description="Liste les parties en cours"
    )
    async def ls(self, ctx: SlashContext):
        games: list = database.getGames()
        log.debug("%s game(s) found", len(games))
        title: str = str.format("{} Game Found", str(len(games)))
        games_str: list = map(str, games)

        from __main__ import bot

        paginated_games = Paginator.create_from_list(bot, prefix="Date Name Players", content=games_str, page_size=500)
        paginated_games.default_title = title
        await paginated_games.send(ctx=ctx)

        # embed = Embed(title=title, description=games_str)

        # await ctx.send(embed=embed)

    @game.subcommand(
        sub_cmd_name="search",
        sub_cmd_description="Take some of our word and with some magic think for you",
        options=[SlashCommandOption(name="research", type=OptionType.STRING)],
    )
    async def search(self, ctx: SlashContext, research: str):
        games = database.getGames()

        game_str = [str(g) for g in games]
        res = process.extract(
            query=research,
            choices=game_str,
            scorer=fuzz.QRatio,
            limit=game["search_limit"],
            processor=utils.default_process,
        )

        # get the str of games sort
        game_match = [s[0] for s in res]
        title = str.format("{} Result for {}", str(len(game_match)), research)


        from __main__ import bot

        paginated_games = Paginator.create_from_list(bot, prefix="Date Name Players", content=game_match, page_size=500)
        paginated_games.default_title = title
        await paginated_games.send(ctx=ctx)
