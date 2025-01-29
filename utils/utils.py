import os
import ffmpeg

def convert_to_mp4(input_file, output_file):
    # Use widely compatible settings for video and audio codecs
    ffmpeg.input(input_file).output(
        output_file,
        vcodec='libx264',  # Video codec (H.264 is widely supported)
        acodec='aac',      # Audio codec (AAC is widely supported)
        strict='-2',       # Allows non-strict behavior (for better compatibility)
        preset='fast',     # Balance between speed and quality
        crf=23,            # Constant Rate Factor for a good quality-to-size ratio
        movflags='faststart'  # Move the moov atom to the start for better streaming compatibility
    ).overwrite_output().run()
    
