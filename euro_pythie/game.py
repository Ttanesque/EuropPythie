from interactions import (
    Extension,
    slash_command,
    SlashCommand,
    SlashCommandOption,
    OptionType,
    SlashContext,
    Embed,
    Member
)
from datetime import date
import logging
import interactions
import database

log = logging.getLogger("Euro_pythie")


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
        raw_players = [player1, player2, player3, player4, player5, player6, player7, player8]
        players = [s.mention for s in raw_players if s != None]

        log.debug("%s", players)
        database.saveGames(g_name, date.today().strftime("%d-%m-%Y"), ",".join(players))

        await ctx.send("Game saved")

    @game.subcommand(
        sub_cmd_name="ls", sub_cmd_description="Liste les parties en cours"
    )
    async def ls(self, ctx: SlashContext):
        games = database.getGames()
        log.debug("%s game(s) found", len(games))

        embed = Embed(title=("Result " + str(len(games))), description="\n".join(map(str, games)))

        await ctx.send(embed=embed)
