import os
import shutil
import re

directory = input("Enter the directory path :")
sub_dir =[]
images = []
count = 0

#get list of item in directory

for item in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,item)):
        sub_dir.append(item)

#Defining search pattern and finding last number in naming convention of folder

pattern = r'Image_(\d)'
for folder in sub_dir:
    match = re.match(pattern, folder)
    if match:
        series = int(match.group(1))
        if series > count:
            count = series

#incrementng counter for next number in series for naming

count = count+1

# Get the list of 'jpg' files in the directory

for img in os.listdir(directory):
    if img.lower().endswith('.jpg'):
        images.append(img)

# Rename and move the images to a new folder

for i, img in enumerate(images):
    old_filepath = os.path.join(directory, img)
    new_filename = f"image_{count + i :06d}.jpg"
    new_directory = os.path.join(directory,"Image_" + str(count + i))
    os.makedirs(new_directory)
    new_filepath = os.path.join(new_directory, new_filename)
    shutil.move(old_filepath, new_filepath)
