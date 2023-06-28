import os
import shutil
import re

def list_pattern_folders(directory):
    sub_dir = []
    pattern = r'Image_(\d)'
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder)):
            match = re.match(pattern, folder)
            if match:
                sub_dir.append(folder)
    return sub_dir

def fetch_series (sub_dir):
    pattern = r'Image_(\d)'
    count =0
    for folder in sub_dir:
        match = re.match(pattern,folder)
        if match:
            series = int(match.group(1))
            if series > count:
                count = series
    return count

def moving_renamed_images_to_new_folder(directory, count):
     images = []
# Get the list of image files in the directory
    for img in os.listdir(directory        if img.lower().endswith('.jpg'):
            images.append(img)

# Rename and move the images to a new folder
    for i, img in enumerate(images):
       old_filepath = os.path.join(directory, img)
       new_filename = f"image_{count + i :06d}.jpg"
       new_directory = os.path.join(directory,"Image_" + str(count + i))
       os.makedirs(new_directory)
       new_filepath = os.path.join(new_directory, new_filename)
       shutil.move(old_filepath, new_filepath)

def main():


    print('Enter the path of your directory example: user\macintosh\desktop')
    directory = input("Enter the directory path :")
    sub_dir = list_pattern_folders(directory)

    count= fetch_series (sub_dir)

    count= count+1

    moving_renamed_images_to_new_folder(directory, count)

if __name__ == "__main__":
    main()
