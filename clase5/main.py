from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)

        """image.show()

        image_blackwhite = image.convert("L")
        image_blackwhite.show()
        image_blackwhite.save("space_bn_.jpg")"""

        font = ImageFont.truetype("fonts/Roboto-Bold.ttf", 120)
        draw = ImageDraw.Draw(image)
        draw.text(
            (500,0),
            "SPACE 2024",
            (255,255,255),
            font
        )

        image.show()
        image.save("space_font.jpg")

        #Create thumbnail
        image.thumbnail((500,500))
        image.show()
        image.save("space_thumbnail.jpg")

    except:
        print("No se encontro la imagen")

if __name__ == "__main__":
    get_image("space.jpg")