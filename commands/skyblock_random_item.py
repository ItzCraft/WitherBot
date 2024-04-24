from discord import Interaction, Embed
from discord.app_commands import allowed_contexts, allowed_installs
from util.functions import log, logUser
from requests import get as requestGet
from random import randint

def commandFunction(tree, client):
    @tree.command(name="skyblock_random_item",description="Choose a random SkyBlock item")
    @allowed_installs(guilds=True, users=True)
    @allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skyblockRandomItemCommand(interaction:Interaction):
        logUser(interaction.user.id)
        items = requestGet(
            url="https://api.hypixel.net/resources/skyblock/items"
        ).json()
        ind = randint(1,4103)
        item = str(items["items"][ind]["name"])
        try:
            lore = str(items["items"][ind]["description"])+"\n"
        except:
            lore = ""
        try:
            rarity = str(items["items"][ind]["tier"])
        except:
            rarity = "None"
        embed = Embed(title=" ",description=f"``{item}``\n{lore}**{rarity}**")
        await interaction.response.send_message(" ",embed=embed)

        log(f"(SUCCESS) {interaction.user} used /skyblock_random_item")


        #for i in range(len(items["items"])):
        #    if(items["items"][i]["name"] == "Very Scientific Paper"):
        #        print(i)
        #        print(items["items"][i])
