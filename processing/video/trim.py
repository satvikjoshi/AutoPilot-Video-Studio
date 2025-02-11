from moviepy import VideoFileClip


def trim_video(input_path, output_path, start_time, end_time):
    """
    Trims a section of a video file from start_time to end_time.

    Args:
        input_path (str): Path to the original video file.
        output_path (str): Path to save the trimmed video.
        start_time (int/float): Start time of the clip in seconds.
        end_time (int/float): End time of the clip in seconds.
    
    Returns:
        None
    """
    try:
        # Load the video file
        video = mp.VideoFileClip(input_path)

        # Trim the video from start_time to end_time
        trimmed_video = video.subclip(start_time, end_time)

        # Save the trimmed video using H.264 codec (standard for MP4)
        trimmed_video.write_videofile(output_path, codec="libx264", fps=30)

        print(f"✅ Video trimmed successfully: {output_path}")

    except Exception as e:
        print(f"❌ ERROR: Failed to trim video {input_path}.\n{e}")

# Example usage (for testing)
if __name__ == "__main__":
    input_video = "data/input/edit1.mp4"
    trimmed_video = "data/output/trimmed.mp4"
    
    # Trim from 5 seconds to 15 seconds
    trim_video(input_video, trimmed_video, 5, 15)
