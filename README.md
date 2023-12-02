# Video Editing Toolkit

This Python script utilizes the MoviePy library to perform various video editing tasks, including merging and resizing videos, cutting videos into clips, and downloading YouTube videos.

You may have seen YouTube Shorts which a main video is playing on top and another video like a gameplay is playing in the background....
This Python scripts is designed to make such videos automatically.
## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install moviepy yt-dlp`)

## Usage

- `video1_path`: Path to the main video file. you can use YouTube url too.
- `video2_path`: Path to the second video file. you can use YouTube url too.
- `output_merged_path`: Path to the output merged video file.
- `output_clips_dir`: Path to short videos after merging.
## Additional Notes

- The script supports downloading the best video and audio quality from YouTube. You can customize the download options in the `download_youtube_video` function.

- Ensure that the required libraries are installed before running the script (`pip install moviepy yt-dlp`).

Feel free to modify the script based on your specific needs and integrate it into your projects. If you encounter any issues or have suggestions, please open an issue in the repository. Happy video editing!


This section now includes a specific credit to ChatGPT for its role in the development of the project.
