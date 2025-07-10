import PIL
from PIL import Image
from PIL import ImageOps

import os

def get_file_path():
    """Takes file path input, defaults to current directory if no input."""
    file_path = input("Enter file path (leave empty for current directory): ")
    if not file_path:  # Checks if input is empty
        file_path = "."  # Sets default to current directory
    
    # Expand user paths (e.g., ~)
    file_path = os.path.expanduser(file_path)
    
    # Get the absolute path
    file_path = os.path.abspath(file_path)
    
    return file_path

def process_jpg_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
                img = os.path.join(dirpath, filename)
                print(img)
                compress_jpg_files(img)

def compress_jpg_files(img):
    #open the image
    with  Image.open(img) as my_image:

        # the original width and height of the image
        image_height = my_image.height
        image_width = my_image.width

        print("The original size of Image is: ", round(len(my_image.fp.read())/1024,2), "KB")

        #compressed the image
        my_image = my_image.resize((round(image_width/3),round(image_height/3)),PIL.Image.NEAREST)
        my_image = ImageOps.exif_transpose(my_image)
        head, tail = os.path.split(img)
        print(head)
        print(tail)
        #save the image
        
        new_directory_path = os.path.join(head,"Compressed")
        print(new_directory_path)
        if new_directory_path:
            os.makedirs(new_directory_path, exist_ok=True)
        new_name = os.path.join(new_directory_path, "compressed_" + tail)
        print(new_name)
        my_image.save(new_name)

        #open the compressed image
        with Image.open(new_name) as compresed_image:
            print("The size of compressed image is: ", round(len(compresed_image.fp.read())/1024,2), "KB")

# Example usage:
directory_path = get_file_path()
#directory_path = "C://Users//Odin.Francis//Documents//Travel//Atsugi 04-25//Test"  # Replace with the actual path
process_jpg_files(directory_path)