from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "skyblock_true_damage_reduction", description= "Calculate your True Damage Reduction percentage in SkyBlock")
    async def skyblockTrueDamageReductionCommand(interaction: Interaction, true_defense: int):
        true_damage_reduction = round(true_defense/(true_defense+100)*100,2)
        embed = Embed(title=" ",description=f"**Your True Damage Reduction percentage is {true_damage_reduction}%** ({true_defense} ❂ True Defense)", colour=16777215)
        await interaction.response.send_message(" ",embed=embed)
        
        log(f"(SUCCESS) {interaction.user} used /skyblock_true_damage_reduction")