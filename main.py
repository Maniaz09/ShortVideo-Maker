from moviepy.editor import VideoFileClip, clips_array
import random
import string
import yt_dlp
import os


def merge_and_resize_videos(video1_path, video2_path, output_path, return_video_file=False):
    # Load video clips
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path).set_audio(None)
    # Resize videos to have the same width while maintaining aspect ratio
    final_width = min(clip1.size[0], clip2.size[0])
    duration = min(clip1.duration, clip2.duration)
    clip1 = clip1.resize(width=final_width)
    clip2 = clip2.resize(width=final_width)

    # Stack the videos vertically
    final_clip = clips_array([[clip1], [clip2]]).set_duration(duration)
    if return_video_file:
        # Write the result to the output path
        final_clip.write_videofile(output_path)
        # return output_path
        return output_path
    else:
        # return VideoClip
        return final_clip


def cut_into_clips(input_video, output_dir, extension, clip_duration=30):
    # Calculate the number of clips
    num_clips = int(input_video.duration / clip_duration)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate and save individual clips
    for i in range(num_clips):
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, input_video.duration)
        clip = input_video.subclip(start_time, end_time)
        cpath = f"clip_{i + 1}.{extension}"
        clip_output_path = os.path.join(output_dir, cpath)
        clip.write_videofile(clip_output_path)
        print(f"DONE! {cpath}")
        clip.close()

    return output_dir


def generate_random_filename(length=10, extension=".txt"):
    """
    Generate a random file name.

    Parameters:
    - length (int): Length of the random string (default is 10).
    - extension (str): File extension (default is ".txt").

    Returns:
    - str: Random file name with the specified length and extension.
    """
    # Define characters to use in the random string
    characters = string.ascii_letters + string.digits

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))

    # Combine the random string with the file extension
    filename = random_string + extension

    return filename


def download_youtube_video(youtube_url, output_folder="youtube_videos"):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',  # change it based on your needs
                }
    ydl = yt_dlp.YoutubeDL(options)

    with ydl:
        # Download the video
        info_dict = ydl.extract_info(youtube_url, download=True)
        # Get the local path of the downloaded video
        video_path = ydl.prepare_filename(info_dict)

    return video_path


video1_path = "video-on-top"  # video path or youtube video download_youtube_video("https://youtu.be/BmC1CmJb82k")
video2_path = "video-on-bottom"  # video path or youtube video download_youtube_video("https://youtu.be/He-jKBESg9I")

ext = video2_path.split(".")[-1]
output_merged_path = generate_random_filename(extension=f".{ext}")
output_clips_dir = "output_clips"  # short videos output folder

merged_video_path = merge_and_resize_videos(video1_path, video2_path, output_merged_path)
cut_into_clips(merged_video_path, output_clips_dir, ext, clip_duration=30)  # change clip duration based on your needs
