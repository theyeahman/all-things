#!/usr/bin/env python3

from PIL import Image
import os
from pathlib import Path

# task 1: user enters relative location of images, we locate
#  absolute path of images
"""
rel_path = "./supplier-data/images"

posix_path = Path(rel_path)
print(posix_path.resolve())
"""
def main():
    path_images = confirm_correct_path()
    imgs = find_images_convert(path_images)

def confirm_correct_path():
    confirm_path = 'no'
    while confirm_path.lower() != 'yes':
        rel_path = input(
        "\nInput relative position of images in following form: ./directory/subdirectory/   \nThey are usually found in ./supplier-data/images: \n" )
        full_path = str(Path(rel_path).resolve())
        confirm_path = input("\n Is this the correct folder? (yes/no/quit)  \n "+ full_path + "   ")
        if confirm_path.lower() == "quit":
            exit()
    return full_path

def find_images_convert(img_folder):
    images = os.listdir(img_folder)
    print('Dealing with ' + str(len(images)) + ' files')
    count = 0
    for i in images:
        if i[-4:] == 'tiff':
            count += 1
            im = Image.open(os.path.join(img_folder,i)).convert('RGB').resize((600,400))
            im.save(os.path.join(img_folder,i[:-4]+'jpeg'),"JPEG")
    print('Processed '+str(count)+' tiff images')

if __name__ == '__main__':
    main()

# task friendly

"""
#!/usr/bin/env python3
from PIL import Image
import os

def main():
    find_images_convert("./supplier-data/images/")

def find_images_convert(img_folder):
    images = os.listdir(img_folder)
    print('Dealing with ' + str(len(images)) + ' files')
    count = 0
    for i in images:
        if i[-4:] == 'tiff':
            count += 1
            im = Image.open(os.path.join(img_folder,i)).convert('RGB').resize((600,400))
            im.save(os.path.join(img_folder,i[:-4]+'jpeg'),"JPEG")
    print('Processed '+str(count)+' tiff images')

if __name__ == '__main__':
    main()


"""
