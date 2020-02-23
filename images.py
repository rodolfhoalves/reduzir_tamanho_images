import os
from PIL import Image
from os import listdir

source_images_path = "/images-para-reduzir/"
destination_images_path = "/images-para-reduzir/novas_images/"

source_images_list  = listdir(source_images_path)


for file in source_images_list:         
        image = f"{source_images_path}{file}"
        if os.path.isfile(image):
           
            image = Image.open(image)
            image.save(f"{destination_images_path}{file}", quality=20, optimize=True)

        else:
            continue
