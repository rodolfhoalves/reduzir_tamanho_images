import os
from PIL import Image
from os import listdir

class Img:

    def __init__(self, source_images_path, quality=20):

        self.quality = quality

        self.destination_images = source_images_path + "reduced-images"
        self.source_images_list  = listdir(source_images_path)

        self.criaPastaDestino()
        self.reduceImages()


    def __str__(self):
        return f"Imagens reduzindas com o parametro {self.quality} "

    def pastaDeImagensReduzidasExiste(self):
        if os.path.exists(self.destination_images):
            return True
        else:
            return False

    
    def criaPastaDestino(self):
        if not self.pastaDeImagensReduzidasExiste():
             
            os.makedirs(self.destination_images)
            return True
        else:
            return False


    def reduceImages(self):
        for file in self.source_images_list:         
            image = f"{source_images_path}{file}"

            if os.path.isfile(image):
            
                image = Image.open(image)
                image.save(f"{self.destination_images}/{file}", quality=self.quality, optimize=True)

            else:
                pass
        
    
source_images_path = "/home/rodolfho/Pictures/images-para-reduzir/"

resultado = Img(source_images_path)
print(resultado)
