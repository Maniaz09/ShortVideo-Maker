# Video Editing Toolkit

This Python script utilizes the MoviePy library to perform various video editing tasks, including merging and resizing videos, cutting videos into clips, and downloading YouTube videos.

You may have seen YouTube Shorts which a main video is playing on top and another video like a gameplay is playing in the background....
This Python scripts is designed to make such videos automatically.
## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install moviepy yt-dlp`)

## Usage

### Merging and Resizing Videos

```python
from moviepy.editor import VideoFileClip
from video_toolkit import merge_and_resize_videos

video1_path = "path/to/video1.mp4"
video2_path = "path/to/video2.mp4"
output_merged_path = "path/to/output/merged_video.mp4"

merge_and_resize_videos(video1_path, video2_path, output_merged_path)
```

- `video1_path`: Path to the first video file.
- `video2_path`: Path to the second video file.
- `output_merged_path`: Path to the output merged video file.

### Cutting Videos into Clips

```python
from moviepy.editor import VideoFileClip
from video_toolkit import cut_into_clips

input_video_path = "path/to/input/video.mp4"
output_clips_dir = "path/to/output/clips"
extension = "mp4"
clip_duration = 30  # Duration of each clip in seconds

input_video = VideoFileClip(input_video_path)
cut_into_clips(input_video, output_clips_dir, extension, clip_duration)
```

- `input_video_path`: Path to the input video file.
- `output_clips_dir`: Directory to save the output clips.
- `extension`: File extension for the output clips.
- `clip_duration`: Duration of each clip in seconds.

### Downloading YouTube Videos

```python
from video_toolkit import download_youtube_video

youtube_url = "https://youtu.be/example"
output_folder = "path/to/output/folder"

download_youtube_video(youtube_url, output_folder)
```

- `youtube_url`: YouTube video URL.
- `output_folder`: Folder to save the downloaded video.

## Additional Notes

- The script supports downloading the best video and audio quality from YouTube. You can customize the download options in the `download_youtube_video` function.

- Ensure that the required libraries are installed before running the script (`pip install moviepy yt-dlp`).

Feel free to modify the script based on your specific needs and integrate it into your projects. If you encounter any issues or have suggestions, please open an issue in the repository. Happy video editing!


This section now includes a specific credit to ChatGPT for its role in the development of the project.
