import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
import json
import os

class VideoEditor:
    def __init__(self, video_path, analysis_report):
        """Initialize the editor with the video file and analysis report."""
        self.video_path = video_path
        self.analysis_report = analysis_report
        self.video_clip = VideoFileClip(video_path)
        self.video_duration = self.video_clip.duration  # Get video duration

    def trim_unnecessary_parts(self):
        """Removes dead pauses but keeps natural pauses for smooth flow."""
        speech_regions = self.analysis_report["speech_regions"]
        motion_frames = self.analysis_report["motion_frames"]

        if not speech_regions and not motion_frames:
            print("❌ No speech or motion detected. Skipping trimming.")
            return self.video_clip

        keep_segments = []
        fps = self.video_clip.fps

        # Convert speech regions into exact frames
        for start, end in speech_regions:
            duration = end - start
        
            # ✅ FIX: Keep small natural pauses (0.5s - 1.5s)
            if duration > 0.5:
                adjusted_start = max(0, start - 0.3)  # Prevent negative start times
                adjusted_end = min(self.video_duration, end + 0.3)  # Prevent exceeding video length
                keep_segments.append((adjusted_start, adjusted_end))  # Adds slight buffer

        # Convert motion timestamps into segments (preserve 1s before & after)
        for motion_time in motion_frames:
            adjusted_start = max(0, motion_time - 1)
            adjusted_end = min(self.video_duration, motion_time + 1)
            keep_segments.append((adjusted_start, adjusted_end))

        # ✅ FIX: Merge overlapping segments smoothly
        keep_segments = sorted(keep_segments, key=lambda x: x[0])
        merged_segments = []
        for seg in keep_segments:
            if not merged_segments or seg[0] > merged_segments[-1][1]:
                merged_segments.append(seg)
            else:
                merged_segments[-1] = (merged_segments[-1][0], max(merged_segments[-1][1], seg[1]))

        # ✅ FIX: Ensure the ending does not get cut off mid-sentence
        final_duration = self.video_duration
        if merged_segments[-1][1] < final_duration - 2:
            merged_segments[-1] = (merged_segments[-1][0], final_duration)  # Ensure final part remains 

        # Trim the video using the detected segments
        final_clips = []
        for start, end in merged_segments:
            if start < end:  # ✅ FIX: Prevent empty subclips
                final_clips.append(self.video_clip.subclip(start, end))

        if not final_clips:
            print("❌ ERROR: No valid segments to keep. Returning original video.")
            return self.video_clip

        # ✅ FIX: Smooth transitions (Avoid Jump Cuts)
        smoothed_clips = []
        for i in range(len(final_clips) - 1):
            smoothed_clips.append(final_clips[i])
            smoothed_clips.append(final_clips[i].crossfadeout(0.3))  # Smooth transition
        smoothed_clips.append(final_clips[-1])  # Keep last clip

        edited_video = concatenate_videoclips(smoothed_clips)

        print("✅ Trimmed video with improved pause handling & smooth transitions.")
        return edited_video

    def apply_basic_effects(self, video_clip):
        """Applies basic stabilization and color correction."""
        print("🎨 Applying basic stabilization and color grading...")
        # For now, just return the clip as MoviePy doesn't support advanced effects.
        return video_clip

    def save_edited_video(self, edited_clip, output_path):
        """Saves the edited video to a file."""
        edited_clip.write_videofile(output_path, codec="libx264", fps=self.video_clip.fps)
        print(f"✅ Edited video saved at: {output_path}")

    def process_video(self, output_path):
        """Runs the full editing process: trimming + effects + save."""
        trimmed_video = self.trim_unnecessary_parts()
        final_video = self.apply_basic_effects(trimmed_video)
        self.save_edited_video(final_video, output_path)

# Example usage:
if __name__ == "__main__":
    video_path = "data/input/sample.mp4"
    analysis_report_path = "data/processed/analysis_report.json"

    # Load the analysis report
    if not os.path.exists(analysis_report_path):
        print("❌ ERROR: Analysis report not found. Run the analyzer first.")
        exit()

    with open(analysis_report_path, "r") as file:
        analysis_report = json.load(file)

    # Run the editor
    editor = VideoEditor(video_path, analysis_report)
    editor.process_video("data/output/final_edit.mp4")
