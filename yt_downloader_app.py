import streamlit as st
import yt_dlp as youtube_dl
from pathlib import Path

# Default output directory
DEFAULT_DOWNLOAD_PATH = Path.home() / "Downloads"

# Function to fetch video title and thumbnail
def get_video_info(url):
    try:
        with youtube_dl.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "Unknown Title")
            thumbnail = info.get("thumbnail", None)
            return title, thumbnail
    except Exception as e:
        st.error(f"Error fetching video info: {e}")
        return None, None

# Function to download video
def download_video(url, format_type, resolution=None, output_path=DEFAULT_DOWNLOAD_PATH):
    try:
        if format_type == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': str(output_path / '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif format_type == 'mp4':
            ydl_opts = {
                'format': f'bestvideo[height<={resolution}]+bestaudio/best',
                'outtmpl': str(output_path / '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return True

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit UI
def main():
    st.set_page_config(page_title="YouTube Downloader", page_icon="🔗", layout="centered")

    # Apply custom theme using CSS
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #FF0000;
            font-family: Arial, sans-serif;
        }
        .stButton > button {
            background-color: #FF0000;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #CC0000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("YouTube Downloader")
    st.write("Download YouTube videos as MP4 (video) or MP3 (audio).")

    url = st.text_input("Enter the YouTube URL:")

    if url:
        video_title, video_thumbnail = get_video_info(url)
        if video_title:
            st.write(f"**Video Title:** {video_title}")
            if video_thumbnail:
                st.image(video_thumbnail, width=400)

    format_type = st.selectbox("Select the format:", ["mp3", "mp4"])

    resolution = None
    if format_type == "mp4":
        resolution = st.selectbox("Select the video resolution:", ["144", "240", "360", "480", "720", "1080"])

    # Always default to Downloads folder for both formats
    output_path = DEFAULT_DOWNLOAD_PATH

    if st.button("Download"):
        if not url:
            st.error("Please provide a valid YouTube URL.")
        else:
            with st.spinner("Downloading..."):
                # Download video without tracking time
                success = download_video(url, format_type, resolution, output_path)

            if success:
                st.success("Download completed successfully!")

if __name__ == "__main__":
    main()
