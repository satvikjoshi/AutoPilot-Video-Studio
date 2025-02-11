import os
import subprocess

def extract_audio(video_path, output_audio_path):
    """
    Extracts audio from a given video and saves it as a WAV file.
    Ensures audio is in 16kHz mono format for proper analysis.
    """
    try:
        command = [
            "ffmpeg", "-i", video_path,  # Input video
            "-q:a", "0", "-map", "a",    # Extract audio only
            "-ar", "16000", "-ac", "1",  # Convert to 16kHz mono
            output_audio_path            # Output file
        ]
        subprocess.run(command, check=True)
        print(f"✅ Extracted audio saved as: {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: Failed to extract audio from {video_path}\n{e}")

if __name__ == "__main__":
    # Paths to input video files
    original_video = "data/input/sample.mp4"
    edited_video = "data/output/final_edit.mp4"

    # Paths to output audio files
    original_audio = "data/input/edit1.wav"
    edited_audio = "data/output/final_edit.wav"

    # Extract audio from both videos
    extract_audio(original_video, original_audio)
    extract_audio(edited_video, edited_audio)
