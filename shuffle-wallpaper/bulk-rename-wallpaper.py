import shutil
import os

def rename_images(directory_path):
    files = os.listdir(directory_path)
    #print(files)

    count = 1
    for filename in files:
        #check for specific file extensions (images)
        if filename.lower().endswith(('.png','jpg','jpeg','webp')):
            extension = os.path.splitext(filename)[1]
            new_name = f"wallpaper_{count}{extension}"

            old_path = os.path.join(directory_path,filename)
            new_path = os.path.join(directory_path,new_name)
            shutil.move(old_path,new_path)
            print(f"Renamed: {filename} -> {new_name}")
            count += 1


#usage 
rename_images(directory_path="/home/shoyo/Pictures/wallpaper-dir/")


