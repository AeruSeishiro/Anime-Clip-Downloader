# 🎬 Anime Clip Downloader

Automatically downloads the highest-viewed 4K twixtor anime clips from YouTube.
No manual searching, no manual downloading — just run and it fills your clip library.

## ✨ Features

- ⚡ **Parallel downloads** — multiple clips download at the same time
- 🔁 **Deduplication** — never downloads the same clip twice, each run fetches new ones
- 📁 **Organised storage** — all clips saved to a `downloads/` folder automatically
- 🔍 **Smart search** — targets highest-viewed results first for best quality
- 🎯 **Customisable** — add your own search queries and anime titles easily

---

## 🛠️ Requirements

- Python 3.8 or higher → download at **python.org/downloads**
- yt-dlp (installed in setup below)

---

## ⚙️ Setup (First Time Only)

**Step 1 — Install Python**

Go to **python.org/downloads**, download the latest version.

> ⚠️ During install, tick **"Add Python to PATH"** before clicking Install Now.

**Step 2 — Clone or download this repo**

Option A — Clone with Git:
```
git clone https://github.com/AeruSeishiro/Anime-Clip-Downloader.git
cd Anime-Clip-Downloader
```

Option B — Download ZIP:
Click the green **Code** button above → **Download ZIP** → extract the folder

**Step 3 — Install yt-dlp**

Open Command Prompt (Windows key → type `cmd` → Enter) and run:
```
pip install yt-dlp
```

---

## ▶️ How to Run

**Option A — Double click (easiest)**

Double-click `START.bat` — installs everything and runs automatically.

**Option B — Command Prompt**
```
python downloader.py
```

Clips are saved to the `downloads/` folder automatically.

---

## ⚙️ Configuration

Open `downloader.py` in any text editor and edit the CONFIG section at the top:

```python
SEARCH_QUERIES = [
    "4k twixtor anime clips",
    "4k twixtor demon slayer",
    "4k twixtor jujutsu kaisen",
    # add your own search terms here
]

VIDEOS_PER_QUERY = 5      # how many videos per search query
MAX_PARALLEL     = 3      # how many downloads run at the same time
OUTPUT_FOLDER    = "downloads"
MIN_VIEWS        = 10000  # skip videos with fewer views than this
```

---

## 📁 File Structure

```
Anime-Clip-Downloader/
├── downloader.py       ← main script
├── requirements.txt    ← dependencies
├── START.bat           ← Windows double-click launcher
├── downloaded.json     ← auto-created, tracks download history
└── downloads/          ← auto-created, where clips are saved
```

> `downloads/` and `downloaded.json` are in `.gitignore` — they won't be uploaded
> to GitHub since clips are too large and history is personal to each machine.

---

## 🔄 How It Works

```
Run downloader.py
      ↓
Search YouTube for each query
      ↓
Filter already-downloaded clips (deduplication)
      ↓
Sort by view count — highest first
      ↓
Download top clips in parallel
      ↓
Save to downloads/ folder
      ↓
Update downloaded.json so next run fetches different clips
```

---

## 🧩 Part of the Anime Content Automation Workflow

This tool is **Step 2** of the full content creation automation:

| Step | Tool | Status |
|------|------|--------|
| 1. Research trends | TikTok Scraper | ✅ Automated |
| 2. Download clips | **This repo** | ✅ Automated |
| 3. Edit video | CapCut / Premiere Pro | Manual |
| 4. Upload to TikTok | Manual / Scheduler | Manual |

---

## ❓ Troubleshooting

| Problem | Fix |
|---------|-----|
| `python is not recognized` | Re-install Python and tick **Add to PATH** |
| `pip is not recognized` | Same as above — re-install Python with PATH ticked |
| `yt-dlp is not recognized` | Run `pip install yt-dlp` in Command Prompt |
| Download fails for a video | YouTube may have restricted it — script skips and continues |
| `START.bat` closes immediately | Right-click → **Run as administrator** |