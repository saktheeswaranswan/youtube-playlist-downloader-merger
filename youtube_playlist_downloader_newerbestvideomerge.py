# -*- coding: utf-8 -*-
"""youtube-playlist-downloader-newerbestvideomerge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IFnOhjgK9_ScdHJaPVlKom4Ob0191Xcs
"""

!pip install -U yt-dlp

import os
from yt_dlp import YoutubeDL

# === CONFIG ===
playlist_url = 'https://www.youtube.com/playlist?list=PLHCNPOIaj2WeZiT5LE7MDF4NwYdMNA_1P'
base_folder = 'Downloaded_Playlist'

# === yt-dlp Options ===
def download_youtube_playlist(url):
    ydl_opts = {
        'outtmpl': f'{base_folder}/%(playlist_index)s - %(title)s/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# === Run ===
if __name__ == '__main__':
    os.makedirs(base_folder, exist_ok=True)
    download_youtube_playlist(playlist_url)

import os
from yt_dlp import YoutubeDL

# === CONFIG ===
playlist_url = 'https://www.youtube.com/playlist?list=PLHCNPOIaj2WdgMwGGKyvwWCE1WVSwfFZu'
base_folder = 'Downloggaded_Playlist'

# === yt-dlp Options ===
def download_youtube_playlist(url):
    ydl_opts = {
        'outtmpl': f'{base_folder}/%(playlist_index)s - %(title)s/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# === Run ===
if __name__ == '__main__':
    os.makedirs(base_folder, exist_ok=True)
    download_youtube_playlist(playlist_url)

import os
from yt_dlp import YoutubeDL

# === CONFIG ===
playlist_url = 'https://www.youtube.com/watch?v=ojQ_ia2PBYU&list=PLHCNPOIaj2Wc8P5xAWq9g2DUrrbixoTOK'
base_folder = 'Doffwnloggaded_Pdlaylist'

# === yt-dlp Options ===
def download_youtube_playlist(url):
    ydl_opts = {
        'outtmpl': f'{base_folder}/%(playlist_index)s - %(title)s/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# === Run ===
if __name__ == '__main__':
    os.makedirs(base_folder, exist_ok=True)
    download_youtube_playlist(playlist_url)

!find /content/Doffwnloggaded_Pdlaylist -type f -name "*.mp4" | sort > /content/all_videos_raw.txt
!sed "s/^/file '/;s/$/'/" /content/all_videos_raw.txt > /content/filelist.txt
!ffmpeg -f concat -safe 0 -i /content/filelist.txt -vf "scale=-2:720" -c:v libx264 -crf 23 -preset fast -c:a aac -b:a 192k -y /content/topp.mp4

!find /content/Downloaded_Playlist -type f -name "*.mp4" | sort > /content/vids_raw.txt
!sed "s/^/file '/;s/$/'/" /content/vids_raw.txt > /content/playlist_files.txt
!ffmpeg -f concat -safe 0 -i /content/playlist_files.txt -vf "scale=-2:720" -c:v libx264 -crf 23 -preset fast -c:a aac -b:a 192k -y /content/trey.mp4

!find /content/Downloggaded_Playlist -type f -name "*.mp4" | sort > /content/downlog_list_raw.txt
!sed "s/^/file '/;s/$/'/" /content/downlog_list_raw.txt > /content/downlog_filelist.txt
!ffmpeg -f concat -safe 0 -i /content/downlog_filelist.txt -vf "scale=-2:720" -c:v libx264 -crf 23 -preset fast -c:a aac -b:a 192k -y /content/trey.mp4

!zip -r  /content/Doffwnloggaded_Pdlaylist.zip  /content/Doffwnloggaded_Pdlaylist

ULTIMATE KUMITE TECHNIQUES 🥋⛩️
https://www.youtube.com/playlist?list=PLHCNPOIaj2WeZiT5LE7MDF4NwYdMNA_1P
Shotokan Karate Kata
https://www.youtube.com/playlist?list=PLHCNPOIaj2WdgMwGGKyvwWCE1WVSwfFZu

ULTIMATE KARATE  by JASON LEUNG 🥋⛩️

https://www.youtube.com/playlist?list=PLHCNPOIaj2Wc8P5xAWq9g2DUrrbixoTOK

https://www.youtube.com/watch?v=N3KSQQ--LB0

https://www.youtube.com/watch?v=8PtYD_6W7BY

https://www.youtube.com/watch?v=hXdS1awov3c

senir master karatae training

https://www.youtube.com/playlist?list=PLKnkn8Bg8AfD43rBtOEfrZmpNn56YCROe

https://www.youtube.com/playlist?list=PLEDBEBl2RnQxNBd_k09jo_3BhQk7tVJjX