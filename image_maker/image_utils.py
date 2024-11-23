import os

from PIL import Image

def convert_to_png(image_path: str):
    im = Image.open(image_path)
    os.remove(image_path)
    image_path = image_path.split(".")[0]
    im.save(f"{image_path}.png")
    