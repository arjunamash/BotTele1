from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp
import os

API_ID = 12345678  # Ganti dengan API ID dari https://my.telegram.org
API_HASH = "API_HASH"  # Ganti dengan API HASH
BOT_TOKEN = "TOKEN_BOT_ANDA"  # Dapatkan token dari @BotFather

app = Client("musikbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Pesan sambutan
@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text(
        "Selamat datang di bot Arjunamash!🎵\n\n"
        "Ini adalah bot musik, silakan ketik:\n"
        "`/musik namalagu`\n\n"
        "Untuk kami unduh dan kirim musik kepadamu 😊",
        quote=True
    )

# Fitur musik
@app.on_message(filters.command("musik") & filters.private)
async def musik(client, message: Message):
    query = message.text.split(maxsplit=1)
    if len(query) < 2:
        await message.reply_text("❗ Contoh penggunaan: `/musik Night Changes x Shayad`", quote=True)
        return

    keyword = query[1]
    await message.reply_text(f"🔍 Mencari dan mengunduh lagu: `{keyword}`...\nMohon tunggu sebentar...", quote=True)

    # Setup konfigurasi yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{keyword}", download=True)
            filename = ydl.prepare_filename(info['entries'][0])
            filename = os.path.splitext(filename)[0] + ".mp3"

        await client.send_audio(
            chat_id=message.chat.id,
            audio=filename,
            caption=f"🎶 Musik: {info['entries'][0]['title']}",
        )
        os.remove(filename)

    except Exception as e:
        await message.reply_text("❌ Gagal mengunduh lagu. Coba judul lain atau periksa koneksi.")
        print(f"Error: {e}")

app.run()
