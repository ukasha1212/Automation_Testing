import os
import shutil
import re

directory = input("Enter the directory path :")
sub_dir =[]
images = []
count = 0


for item in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,item)):
        sub_dir.append(item)

pattern = r'Image_(\d)'
for folder in sub_dir:
    match = re.match(pattern, folder)
    if match:
        series = int(match.group(1))
        if series > count:
            count = series


count = count+1

# Get the list of image files in the directory
for img in os.listdir(directory):
    if img.lower().endswith('.jpg'):
        images.append(img)

# Rename and move the images to a new folder
for i, img in enumerate(images):
    old_filepath = os.path.join(directory, img)
    new_filename = f"image_{count + i :06d}.jpg"
    new_directory = os.path.join(directory,"Image_" + str(count + i))
    os.makedirs(new_directory, exist_ok=True)
    new_filepath = os.path.join(new_directory, new_filename)
    shutil.move(old_filepath, new_filepath)
