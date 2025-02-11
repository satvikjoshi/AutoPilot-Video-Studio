import cv2
import numpy as np
import librosa
import torchaudio
import torch
from moviepy.editor import VideoFileClip
import speechbrain as sb
import os


class VideoAnalyzer:
    def __init__(self, video_path):
        """Initialize with video path and extract video/audio properties."""
        self.video_path = video_path
        self.video_clip = VideoFileClip(video_path)
        self.audio_path = self.extract_audio()
    
    def extract_audio(self):
        """Extracts audio from the video and saves it as a WAV file."""
        audio_output = self.video_path.replace(".mp4", ".wav")
        self.video_clip.audio.write_audiofile(audio_output, codec='pcm_s16le')
        return audio_output

    def detect_speech_regions(self):
        """Analyzes the audio to detect speech vs silence."""
        y, sr = librosa.load(self.audio_path, sr=16000)
        energy = librosa.feature.rms(y=y)[0]
        threshold = np.percentile(energy, 25)  # Dynamic silence threshold

        speech_regions = []
        is_speaking = False
        start_time = 0

        for i, e in enumerate(energy):
            time = i * (len(y) / len(energy)) / sr  # Convert frame index to time
            if e > threshold and not is_speaking:
                start_time = time
                is_speaking = True
            elif e <= threshold and is_speaking:
                speech_regions.append((start_time, time))
                is_speaking = False

        return speech_regions

    def detect_scene_changes(self):
        """Detects scene changes based on color histogram differences."""
        cap = cv2.VideoCapture(self.video_path)
        prev_hist = None
        scene_changes = []
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hist = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])

            if prev_hist is not None:
                diff = cv2.compareHist(hist, prev_hist, cv2.HISTCMP_CORREL)
                if diff < 0.8:  # Lower correlation = scene change
                    scene_changes.append(frame_count / frame_rate)

            prev_hist = hist
            frame_count += 1

        cap.release()
        return scene_changes

    def analyze_motion(self):
        """Detects high-motion areas to avoid cutting important action scenes."""
        cap = cv2.VideoCapture(self.video_path)
        prev_frame = None
        motion_frames = []
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if prev_frame is not None:
                diff = cv2.absdiff(prev_frame, gray)
                motion_level = np.sum(diff) / diff.size  # Calculate motion intensity
                if motion_level > 5:  # Arbitrary threshold for "high motion"
                    motion_frames.append(frame_count / frame_rate)

            prev_frame = gray
            frame_count += 1

        cap.release()
        return motion_frames

    def generate_analysis_report(self):
        """Runs all analysis functions and compiles a report."""
        speech_regions = self.detect_speech_regions()
        scene_changes = self.detect_scene_changes()
        motion_frames = self.analyze_motion()

        analysis_report = {
            "speech_regions": speech_regions,
            "scene_changes": scene_changes,
            "motion_frames": motion_frames
        }
        return analysis_report

# Example usage:
if __name__ == "__main__":
    video_path = "data/input/sample.mp4"
    analyzer = VideoAnalyzer(video_path)
    report = analyzer.generate_analysis_report()

    print("✅ Analysis Complete!")
    print(report)
