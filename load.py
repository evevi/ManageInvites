from discord.ext import commands
from settings import folder_list
import os


class CoreLoad(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, types=None, extension=None):
        if ctx.author.id == 643072638075273248:
            if types is not None and extension is not None:
                if types.lower() in folder_list:
                    if extension == "*":
                        for filenames in os.listdir(f'./{types}'):
                            if filenames.endswith('.py'):
                                print(f"Load {extension}, by {ctx.author}")
                                self.client.load_extension(f'{types}.{filenames[:-3]}')
                        await ctx.send(f"Loaded all extensions in {types}, succes!")
                    else:
                        self.client.load_extension(f'{types}.{extension}')
                        print(f"Load {extension}, by {ctx.author} in {types}")
                        await ctx.send(f"Load {extension}, succes!")


def setup(client):
    client.add_cog(CoreLoad(client))
