import os
import subprocess

input_folder = "input_folder"
output_folder = "output_folder"

# Make sure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a video file
    if filename.endswith(".mp4") or filename.endswith(".mkv"):
        # Set the input and output paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, "output_" + filename)

        # Get the original height of the video
        cmd_height = "ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=s=x:p=0 {}".format(input_path)
        result_height = subprocess.check_output(cmd_height, shell=True)
        original_height = int(result_height.decode().strip())

        # Calculate the new height and set the aspect ratio
        new_height = original_height // 2
        aspect_ratio = "2:1"

        # Build the FFmpeg command with variables
        command = ['ffmpeg', '-i', input_path, '-filter_complex', f'[0:v]crop=3840:{new_height}:0:0,lenscorrection=cx=0:cy=0:k1=-0:k2=-0[outv]',
                   '-map', '[outv]', '-map', '0:a', '-vcodec', 'h264_nvenc', '-aspect', aspect_ratio, '-b:v', '50M', output_path]

        # Run the FFmpeg command
        subprocess.run(command)
