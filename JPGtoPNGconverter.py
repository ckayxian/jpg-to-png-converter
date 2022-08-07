import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if output folder (new/) exists, if not, create the output folder
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
# save to the output folder
for item in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{item}')
    rename_file = os.path.splitext(item)[0]
    img.save(f'{output_folder}{rename_file}.png', 'png')

print('Images converted successfully!')

