import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "𝙷𝙴𝙻𝙾 𝙱𝚁𝙾...",
    "𝙷𝙾𝚆 𝚁 𝚈𝙾𝚄??",
    "𝙳𝙾𝙽𝚃 𝙲𝙷𝙴𝙲𝙺, 𝙸'𝙼 𝚂𝚃𝙸𝙻𝙻 𝙰𝙻𝙸𝚅𝙴...😅😂", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
