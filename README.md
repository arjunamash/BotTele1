
# 🎵 MasharmBot - Telegram Bot Musik Otomatis

Bot Telegram yang memungkinkan pengguna mengunduh lagu cukup dengan perintah:
```
/musik namalagu
```

## 🛠️ Kebutuhan Sistem

- OS: Linux (Armbian, Debian, Ubuntu, dsb.)
- Python: v3.7 atau lebih baru
- Platform sudah dites di STB HG680P dengan Armbian

---

## 📦 Tools & Dependencies
Masuk ke Super User (Root)
Berikut adalah tools dan library Python yang wajib diinstal agar bot berjalan sempurna: (Pastikan kamu berada di path root "cd /")

### 1. Python Package

Instal semua dependensi Python berikut:

```bash
sudo apt update
sudo apt install git -y
sudo apt install python3
sudo apt install python3-pip
pip install pyrogram tgcrypto yt-dlp --break-system-package
```

Jika ada error saat install `tgcrypto`, pastikan kamu sudah menginstal header dev Python:
```bash
# Cek versi python3 "python3 --version"
sudo apt install python3-dev build-essential
# Atau jika pakai Python 3.11:
sudo apt install python3.11-dev
# Lalu ulangi:
pip install pyrogram tgcrypto yt-dlp --break-system-package
```

### 2. FFmpeg

`yt-dlp` menggunakan `ffmpeg` untuk mengonversi audio (ke `.mp3`), jadi **wajib** diinstal:

```bash
sudo apt install ffmpeg
```

---

## 🔐 Konfigurasi Akun Telegram

Kamu harus punya:

- `API_ID` dan `API_HASH` dari: [https://my.telegram.org]

Langkah-langkah:

1. Login ke [https://my.telegram.org]
2. Klik **API Development Tools**
3. Isi:
   - App Title: bebas (misalnya: MasharmBot)
   - Short Name: masharmbot
   - Platform: Desktop
   - URL: https://t.me/nama_bot_anda (Dapatkan melalui https://t.me/BotFather)
4. Salin `API_ID` dan `API_HASH` dan simpan
---

## 📄 Struktur File

```
Di path root: (Pindahkan masharmbot.py ke root / "mv /BotTele1/masharmbot.py /
")
├── masharmbot.py         # Script utama bot (git clone https://github.com/arjunamash/BotTele1)
├── masharmbot.session    # File session Pyrogram (otomatis dibuat)

`API_ID` dan `API_HASH` yang dicopy tadi dipakai untuk mengubah kode di masharmbot.py (nano masharmbot.py)
```



---

## 🚀 Menjalankan Bot

Jalankan bot secara manual: 

```bash
chmod 744 masharmbot.py
python3 masharmbot.py
```

JIKA ADA ERROR `sqlite3.OperationalError: database is locked`:

```bash
ps aux | grep masharmbot.py # Copy kode PID python3 masharmbot.py
kill -9 <NOMOR_PID>
```

---

## ⚙️ Opsional: Systemd Service (Autostart)

Untuk menjalankan bot otomatis saat boot, buat file `nano /etc/systemd/system/masharmbot.service`, isi:

```ini
[Unit]
Description=Bot Telegram Musik - masharmbot
After=network.target

[Service]
User=root
WorkingDirectory=/
ExecStart=/usr/bin/python3 masharmbot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Lalu aktifkan:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable masharmbot
sudo systemctl start masharmbot
```

---

## ✅ Catatan

- Pastikan bot kamu sudah diaktifkan melalui (https://t.me/BotFather)
- File musik dikirim dalam format `.mp3`
- Tidak ada iklan/link YouTube yang dikirim ke pengguna

---

## 📬 Kontak

Dibuat oleh: [Arjunamash](https://arjunamash.eu.org) dengan AI ChatGPT