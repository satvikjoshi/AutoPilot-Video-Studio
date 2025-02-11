import moviepy.editor as mp

def merge_videos(video_paths, output_path):
    """
    Merges multiple video clips into a single video.

    Args:
        video_paths (list): List of file paths for the video clips to merge.
        output_path (str): Path to save the merged video.
    
    Returns:
        None
    """
    try:
        # Load each video file as a separate clip
        clips = [mp.VideoFileClip(video) for video in video_paths]

        # Concatenate the clips together
        final_video = mp.concatenate_videoclips(clips, method="compose")

        # Save the final merged video
        final_video.write_videofile(output_path, codec="libx264", fps=30)

        print(f"✅ Videos merged successfully: {output_path}")

    except Exception as e:
        print(f"❌ ERROR: Failed to merge videos.\n{e}")

# Example usage (for testing)
if __name__ == "__main__":
    video1 = "data/input/clip1.mp4"
    video2 = "data/input/clip2.mp4"
    merged_video = "data/output/merged.mp4"
    
    merge_videos([video1, video2], merged_video)
