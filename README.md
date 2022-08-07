# JPG to PNG Converter

## Overview
This is a project that converts multiple JPG images to PNG using Python and the Pillow library.


## How it works
If you run JPGtoPNGconverter.py with two parameters, the program is going to scan through the image folder (the first parameter), and convert each .jpg image into .png and save them to output folder (second parameter)
If the output folder does not exist, the program will create the folder
You can use it to convert any JPG image to PNG

## Try It Out
1. You can either
`pip install -r requirements.txt`
or
`pip install Pillow`

2. run `JPGtoPNGconverter.py <image_folder/> <output_folder/>`
e.g. `JPGtoPNGconverter.py pokemon/ new/`

