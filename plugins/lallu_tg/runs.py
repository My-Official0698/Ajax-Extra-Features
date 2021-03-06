import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "π·π΄π»πΎ π±ππΎ...",
    "π·πΎπ π ππΎπ??",
    "π³πΎπ½π π²π·π΄π²πΊ, πΈ'πΌ πππΈπ»π» π°π»πΈππ΄...ππ", 
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
