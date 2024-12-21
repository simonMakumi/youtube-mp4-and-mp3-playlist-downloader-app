# YouTube Downloader App

A simple Streamlit app to download YouTube videos or audio (MP3/MP4). This app allows you to download YouTube videos in both MP3 and MP4 formats, with an option to choose the resolution for MP4 downloads.

## Features

- **Download YouTube videos as MP3 (audio)** with a preferred quality of 192 kbps.
- **Download YouTube videos as MP4 (video)** with selectable resolution options.
- **Fetch and display video title and thumbnail** before download.
- **Customizable output folder** (default is your system's Downloads folder).
- **User-friendly Streamlit interface** for easy interaction.

## Requirements

To run the app locally, ensure you have the following installed:

- Python 3.x
- Streamlit
- yt-dlp
- FFmpeg (for audio conversion)

You can install the required dependencies with:

```bash
pip install streamlit yt-dlp
```

You also need to have FFmpeg installed. On Ubuntu, you can install it using:

```bash
sudo apt install ffmpeg
```

## Usage

### Running the App Locally
 1. Clone the repository:

```bash
git clone <https://github.com/simonMakumi/youtube-mp4-and-mp3-playlist-downloader-app>
cd <repository_directory>
```

 2. Install the dependencies:

```bash
pip install streamlit yt-dlp
```

 3. Run the app:

```bash
streamlit run yt_downloader_app.py
```

Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).

### How to Use the App

- **Enter the YouTube URL:** Paste the URL of the YouTube video or playlist you want to download.
- **Choose the format:** Select either MP3 (for audio only) or MP4 (for video). If you choose MP4, you will also be prompted to select the video resolution (e.g., 144p, 360p, 720p).
- **Click the Download button:** After selecting the format and providing the URL, click the Download button to start the process.
- **Download location:** By default, the files will be saved in your Downloads folder, but you can modify the download path as needed.

### Example Usage

* To download a video as MP3:

Enter a YouTube video URL (e.g., https://www.youtube.com/watch?v=example).
Choose MP3 as the format.
Click Download.

* To download a video as MP4:

Enter a YouTube video URL.
Choose MP4 as the format and select a resolution (e.g., 720p).
Click Download.

## Customization

- **Output directory**: By default, downloads are saved to the Downloads folder. To change the download path, you can modify the `DEFAULT_DOWNLOAD_PATH` variable in the script.

- **Custom styling**: The app has custom CSS styling to enhance the UI. You can modify the styles within the `st.markdown` section to fit your design preferences.

## Troubleshooting

- **Error fetching video info:** This may occur if the provided YouTube URL is incorrect or if yt-dlp encounters a temporary issue. Ensure the URL is correct and try again later.

- **FFmpeg not installed:** Make sure you have FFmpeg installed and accessible in your system's PATH.

## License

This project is open source and available under the MIT License.
