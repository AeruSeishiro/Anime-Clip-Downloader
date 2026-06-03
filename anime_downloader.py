import os
import sys
import subprocess

def auto_download_anime_clips(anime_name, num_clips):
    # 1. Back to your exact preferred target folder!
    target_folder = r"C:\Users\c.wijaya\yt-dlp\clip"
    os.makedirs(target_folder, exist_ok=True)
    
    # 2. Keep the history archive file inside the main yt-dlp folder
    history_file = r"C:\Users\c.wijaya\yt-dlp\downloaded_history.txt"
    
    # 3. Output structure for the video files
    output_dir = os.path.join(target_folder, "%(title)s.%(ext)s")
    
    # 4. Ask YouTube for a pool of top 10 results to check against your history
    search_query = f"ytsearch10:{anime_name} 4k twixtor clip log"
    
    print(f"\n🔍 Searching YouTube for new 4K clips of: '{anime_name}'...")
    print(f"📁 Target location: {target_folder}")
    print("⏳ Downloading unique video layers (skipping duplicates in history)...")
    
    # 5. Build the smart command
    command = [
        sys.executable, "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]", 
        "--merge-output-format", "mp4",
        "--download-archive", history_file,
        "--max-downloads", str(num_clips),  # Stops exactly when you get your desired number of NEW clips
        search_query,
        "-o", output_dir
    ]
    
    # Execute the command
    subprocess.run(command)
    print(f"\n✅ Finished! Any new videos are saved in your 'yt-dlp/clip' folder.\n")

if __name__ == "__main__":
    user_choice = input("What anime character or scene do you need 4K clips for? ")
    clips_input = input("How many *NEW* clips do you want? (e.g., 1, 2, 3): ")
    
    try:
        num_clips = int(clips_input)
    except ValueError:
        num_clips = 1
        
    auto_download_anime_clips(user_choice, num_clips)