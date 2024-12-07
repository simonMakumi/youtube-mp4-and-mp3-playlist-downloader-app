Here is the usage information for the script:

### Usage

1. **Download a single YouTube video and convert it to MP3:**
   ```sh
   python download.py video <YouTube_video_URL> --output <output_path>
   ```
   - Replace `<YouTube_video_URL>` with the actual URL of the YouTube video.
   - Replace `<output_path>` with the desired output directory (optional, default is 

mp3

).

2. **Download a YouTube playlist and convert each video to MP3:**
   ```sh
   python download.py playlist <YouTube_playlist_URL> --output <output_path>
   ```
   - Replace `<YouTube_playlist_URL>` with the actual URL of the YouTube playlist.
   - Replace `<output_path>` with the desired output directory (optional, default is 

mp3

).

### Examples

- **Download a single video:**
  ```sh
  python download.py video https://www.youtube.com/watch?v=exampleVideoID --output my_music
  ```

- **Download a playlist:**
  ```sh
  python download.py playlist https://www.youtube.com/playlist?list=examplePlaylistID --output my_music
  ```

If you do not specify the `--output` argument, the MP3 files will be saved in the default directory 

mp3

.

### Script Explanation

- The script uses `yt_dlp` to download YouTube videos or playlists.
- It converts the downloaded audio to MP3 format using `FFmpeg`.
- Logging is set up to log messages to both the console and a file named 

download.log

.
- The `nocheckcertificate` option is used to disable SSL certificate verification.
