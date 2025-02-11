from moviepy import VideoFileClip as mp
import os

def extract_audio(video_path, output_audio_path):
    """
    Extracts the audio from a video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.
        output_audio_path (str): Path to save the extracted audio file.
    
    Returns:
        None
    """
    try:
        # Load the video file
        video = mp.VideoFileClip(video_path)

        # Extract the audio from the video
        audio = video.audio

        # Save the extracted audio as a WAV file (PCM codec for compatibility)
        audio.write_audiofile(output_audio_path, codec='pcm_s16le')

        print(f"✅ Audio extracted successfully: {output_audio_path}")

    except Exception as e:
        print(f"❌ ERROR: Failed to extract audio from {video_path}.\n{e}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    input_video = "data/input/sample.mp4"
    output_audio = "data/output/sample_audio.wav"
    extract_audio(input_video, output_audio)
