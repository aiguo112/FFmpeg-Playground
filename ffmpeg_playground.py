import ffmpeg

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import subprocess

# Define the input and output file names
input_file = "test.mp4"
output_prefix = "Tile"

# Define the number of rows and columns to split the video into
rows = 3
cols = 3

# Generate the output file names
output_files = [f"{output_prefix}{i+1}.mp4" for i in range(rows*cols)]

# Generate the crop filter options
crop_filters = []
for row in range(rows):
    for col in range(cols):
        crop_filters.append(f"[0:v]crop=1/{cols}*in_w:1/{rows}*in_h:{col}/{cols}*in_w:{row}/{rows}*in_h[out{row*cols+col+1}]")
crop_filter_string = ";".join(crop_filters)

# Generate the -map options
map_options = []
for i, output_file in enumerate(output_files):
    map_options.extend(["-map", f"[out{i+1}]", output_file])

# Define the ffmpeg command
command = [
    "ffmpeg",
    "-i", input_file,
    "-filter_complex", crop_filter_string,
] + map_options

# Run the command
subprocess.run(command)
