import os
import shutil

directory = input("Enter the directory path: ")

images = []
count = 0

# Get the list of image files in the directory
for img in os.listdir(directory):
    if img.lower().endswith('.jpg'):
        images.append(img)
        count += 1

# Rename and move the images to a new folder
for i, img in enumerate(images):
    old_filepath = os.path.join(directory, img)
    new_filename = f"image_{i + 1:06d}.jpg"
    new_directory= os.path.join(directory,"Image_" + str(i + 1))
    os.makedirs(new_directory)
    new_filepath = os.path.join(new_directory, new_filename)

    shutil.move(old_filepath, new_filepath)
