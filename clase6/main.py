from PIL import Image
import os

def compress_image(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name,file_extension = os.path.splitext(image_folder + file)
            print("Comprimiendo archivo" + file_name + file_extension)

            if file_extension == ".png":
                file_compress = Image.open(image_folder + file)
                file_compress.save(file_name + "_compressed.png",
                                   optimize=True,
                                   quiality=70)
    except:
        print("No se pudo comprimir")

if __name__ == "__main__":
    compress_image("C:/Users/USER/Downloads/tattoos/")