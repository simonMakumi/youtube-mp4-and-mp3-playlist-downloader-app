import ssl
import certifi
import argparse
import yt_dlp as youtube_dl
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

# Default output directory
DEFAULT_DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

def download_youtube_video(url, format_type, output_path=DEFAULT_DOWNLOAD_PATH):
    try:
        logging.info(f"Starting download for video: {url} in format {format_type}")
        
        # Configure options for MP3 or MP4 download
        if format_type == 'mp3':
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
        elif format_type == 'mp4':
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'nocheckcertificate': True,  # Disable SSL certificate verification
            }
        else:
            raise ValueError("Unsupported format type. Use 'mp3' or 'mp4'.")

        # Download the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            ydl.download([url])
        
        logging.info(f"Downloaded and converted: {url} to {format_type}")
    except Exception as e:
        logging.error(f"An error occurred while downloading video: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos and convert them to MP3 or MP4.")
    parser.add_argument('url', help="The YouTube URL of the video to download.")
    parser.add_argument('--format', choices=['mp3', 'mp4'], default='mp3', help="The format to download: 'mp3' for audio or 'mp4' for video (default is 'mp3').")
    parser.add_argument('--output', default=DEFAULT_DOWNLOAD_PATH, help=f"The output path for the downloaded files (default is '{DEFAULT_DOWNLOAD_PATH}').")

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)
        logging.info(f"Created output directory: {args.output}")

    download_youtube_video(args.url, args.format, args.output)

