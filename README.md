# FFMPEG
FFmpeg Playground 🎥
Welcome to the FFmpeg Playground repository! 🎬 Here, we're diving into the world of multimedia manipulation and exploration with the powerful FFmpeg toolkit. Whether you're a developer, video enthusiast, or just curious about multimedia magic, this repository is your gateway to unlocking a realm of possibilities.

What's Inside:
⬇️ Install the ffmpeg-python library if you haven't already:
```python
pip install ffmpeg-python
```

🔗 Basic Video Conversion: Discover how to transmute video formats like a digital alchemist. Convert between formats, codecs, and containers seamlessly.

🔀 Video Splitting: Learn the art of slicing and dicing videos. Extract segments, scenes, or highlights from a larger video canvas.

🔄 Video Concatenation: Master the craft of weaving videos together. Merge multiple clips into captivating sequences with just a few lines of code.

🎞️ Frame Extraction: Uncover the hidden frames that compose your favorite videos. Extract still images for thumbnails, analysis, or artistic exploration.

🔊 Audio Extraction: Delve into the auditory dimension of videos. Isolate, extract, and manipulate audio tracks for remixing or analysis.

🌈 Filter Effects: Experiment with FFmpeg's filter library to apply dazzling effects to videos. Enhance, blur, distort, and create visual magic.

🎥 Custom Scripts: Get creative! Craft your own scripts using FFmpeg to tailor-make video manipulations that suit your needs.

💡 Why FFmpeg: FFmpeg is a Swiss Army knife for multimedia processing. Its flexibility, power, and extensive library of codecs make it an essential tool for professionals and enthusiasts alike.



# Video Resizing and Lens Correction Tool using FFmpeg

This repository contains a Python script `Lens_Correction.py`  that utilizes FFmpeg to resize videos, perform lens correction, and apply video encoding with hardware acceleration. The script processes video files from an input folder, performs the required transformations, and saves the results in an output folder.

## Usage

1. Ensure you have FFmpeg installed on your system. You can download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) or use package managers like `brew` (macOS) or `apt-get` (Linux).

2. Clone or download this repository to your local machine.

3. Place the video files you want to process in the `input_folder` directory.

4. Open a terminal and navigate to the repository's root directory.

5. Run the script using the following command:

   ```bash
   python process_videos.py
   ```

Replace Python with Python 3 if necessary, depending on your system configuration.

The script will process each video file with the specified transformations and save the results in the output_folder directory.
# Features
Resizes videos to half of their original height while maintaining the aspect ratio.
Applies lens correction to improve the video's visual quality.
Utilizes FFmpeg's hardware acceleration for video encoding using the h264_nvenc codec.
Configurable parameters for output video quality and aspect ratio.
# Requirements
Python 3.x
FFmpeg
# Disclaimer
This script is provided as-is for educational and demonstration purposes. Always respect copyright and licensing laws when using or modifying video content.

Feel free to explore, modify, and enhance this script to fit your specific requirements. If you encounter any issues or have suggestions, please don't hesitate to open an issue or pull request in this repository.

Join the journey into the world of multimedia transformation and exploration. Clone, fork, or contribute to this repository as we decode the secrets of FFmpeg's enchanting capabilities.

Have a favorite video manipulation trick or idea? Contribute your knowledge and let's build a library of FFmpeg wizardry together! ✨

Stay curious, stay creative, and let's make multimedia magic happen! 🌟

# License
This project is licensed under the MIT License. Feel free to fork, modify, and use it according to the terms of the license.
