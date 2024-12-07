import ssl
import certifi
import argparse
import yt_dlp as youtube_dl
from pydub import AudioSegment
import os
import logging

# Set up SSL context to use certifi's certificate bundle
ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = lambda: ssl_context

# Set up logging to log to both file and console
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('download.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

def download_youtube_video(url, output_path='mp3'):
    try:
        logging.info(f"Starting download for video: {url}")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'nocheckcertificate': True,  # Disable SSL certificate verification
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            ydl.download([url])
        logging.info(f"Downloaded and converted: {url}")
    except Exception as e:
        logging.error(f"An error occurred while downloading video: {e}")

def download_youtube_playlist(url, output_path='mp3'):
    try:
        logging.info(f"Starting download for playlist: {url}")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'nocheckcertificate': True,  # Disable SSL certificate verification
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            ydl.download([url])
        logging.info(f"Downloaded and converted playlist: {url}")
    except Exception as e:
        logging.error(f"An error occurred while downloading playlist: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos or playlists and convert them to MP3.")
    parser.add_argument('type', choices=['video', 'playlist'], help="Specify whether to download a single video or a playlist.")
    parser.add_argument('url', help="The YouTube URL of the video or playlist.")
    parser.add_argument('--output', default='mp3', help="The output path for the downloaded files (default is 'mp3').")

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)
        logging.info(f"Created output directory: {args.output}")

    if args.type == 'video':
        download_youtube_video(args.url, args.output)
    elif args.type == 'playlist':
        download_youtube_playlist(args.url, args.output)