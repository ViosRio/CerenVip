
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
import os
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import requests
import yt_dlp
import aiohttp
from pyrogram import filters
from youtube_search import YoutubeSearch
import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging
import json

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

HEY SENDE MARKETİMİZDEKİ VİP SERVİSLERDEN FAYDALANABİLİRSİN
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ,
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="sᴀʜɪᴘ", url=f"https://t.me/{OWNER_USERNAME}")
    ],
    [
        InlineKeyboardButton(
            text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʏᴀʀᴅıᴍ & ᴋᴏᴍᴜᴛʟᴀʀ ", callback_data="HELP"),
    ],
]
X = [
    [
        InlineKeyboardButton(text=" ᴅᴇsᴛᴇᴋ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="ᴅᴇsᴛᴇᴋ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"{SOURCE}")]])
HELP_READ = "➻ MÜZİK KAZIYICI :\n\n • /bul = Youtube Mp3 İndirme Özelliği\n\n➻ SAĞLIK ÖLÇER :\n\n • /ping = Botun Sağlık Sorunları Test Et\n\n➻ SOSYAL KAZIYICI :\n\n • /hashtag = Tiktok Trend Madencisi\n • /pintag = Pinterest İlgi Alanları Keşfet\n • /sms = Tek Kullanımlık Şakalar\n • /plaka = Plaka Checker Aracı\n\n➻ DELİL KARARTMA :\n\n • /hash = METİNLERİ ŞİFRELE\n ʙᴏᴛ ᴠᴇʀsɪᴏɴ ᴠ2.1"
HELP_BACK = [
     [
           InlineKeyboardButton(text="ᴋᴀʏɴᴀᴋ ", url=f"https://github.com/zeedslowy/CerenVip"),
           
     ],
    [
           InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "Bekleyiniz.."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("✦ Yᴜ̈ᴋʟᴇɴɪʏᴏʀ..")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪ̇ʟᴇᴛɪşɪᴍ ᴠᴇ öɴᴇʀɪ \n➥ `{ms}` ms\n\n**🌹 || [sᴀʜɪᴘ](https://t.me/{OWNER_USERNAME})||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

# Pinterest

@Mukesh.on_message(filters.command(["pintag"]))
async def hashtag_handler(client, message: Message):
    tag = message.text.replace("/pintag", "").strip()
    if not tag:
        await message.reply_text("✅ KULLANIM :\n\n /pintag [ 3400 ]")
        return
    
    try:
        url = f"https://cerenyaep.serv00.net/client/app/pintag/data.php?explore={tag}"
        r = requests.get(url)
        if r.status_code == 200 and r.text.strip():
            blocks = r.text.strip().split('<hr>')
            result = "\n\n———\n\n".join(["\n".join(b.split("•")).strip() for b in blocks])
            await message.reply_text(f"**#{tag}** hakkında:\n\n{result}", parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text("📛 HATA : \n\n Sonuç Bulunamadı.")
    except Exception as e:
        await message.reply_text(f"Hata: {e}")

# plaka

@Mukesh.on_message(filters.command(["plaka"]))
async def hashtag_handler(client, message: Message):
    tag = message.text.replace("/plaka", "").strip()
    if not tag:
        await message.reply_text("✅ KULLANIM :\n\n /plaka [ 3400 ]")
        return
    
    try:
        url = f"https://cerenyaep.serv00.net/client/app/plaka/data.php?explore={tag}"
        r = requests.get(url)
        if r.status_code == 200 and r.text.strip():
            blocks = r.text.strip().split('<hr>')
            result = "\n\n———\n\n".join(["\n".join(b.split("•")).strip() for b in blocks])
            await message.reply_text(f"**#{tag}** hakkında:\n\n{result}", parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text("📛 HATA : \n\n Sonuç Bulunamadı.")
    except Exception as e:
        await message.reply_text(f"Hata: {e}")


    
# instagram hashtag

@Mukesh.on_message(filters.command(["hashtag"]))
async def hashtag_handler(client, message: Message):
    tag = message.text.replace("/hashtag", "").strip()
    if not tag:
        await message.reply_text("✅ KULLANIM :\n\n /hashtag [ ceren ]")
        return
    
    try:
        url = f"https://cerenyaep.serv00.net/client/app/tokplus/data.php?explore={tag}"
        r = requests.get(url)
        if r.status_code == 200 and r.text.strip():
            blocks = r.text.strip().split('<hr>')
            result = "\n\n———\n\n".join(["\n".join(b.split("<br>")).strip() for b in blocks])
            await message.reply_text(f"**#{tag}** hakkında:\n\n{result}", parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text("📛 HATA : \n\n Sonuç Bulunamadı.")
    except Exception as e:
        await message.reply_text(f"Hata: {e}")

# song 

@Mukesh.on_message(filters.command(["song", "bul"]))
def song(client, message):

    message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("**» Bekleyiniz...**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "✅ KULLANIM\n\n /song [ YOUTUBE MÜZİK İSİM ]"
        )
        print(str(e))
        return
    m.edit("» İndiriliyor...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**Başlık :** {title[:25]}\n**İzlenme :** `{duration}`\n**Süre :** `{views}`\n**Talep »** {chutiya}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit(
            f"» Başarısız,"
        )
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
