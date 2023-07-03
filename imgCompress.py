#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""imgCompress.py: Locally compress images for your web projects."""

__author__     = "SilentGlasses"
__version__    = "1.0.0"
__status__     = "Production"

from PIL import Image
import os

def compress_image(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=75)

def compress_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            compress_image(input_path, output_path)
            print(f"Compressed {filename}")

# Get the current directory
current_directory = os.getcwd()

# Set the input directory as the current directory
input_directory = current_directory

# Set the output directory as 'compressed_images' in the current directory
output_directory = os.path.join(current_directory, 'compressed_images')

# Compress images in the input directory and save them to the output directory
compress_directory(input_directory, output_directory)
