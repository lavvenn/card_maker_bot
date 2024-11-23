import os

from PIL import Image, ImageDraw


class ImageEditor:
    def __init__(self, template_path: str, output_path: str):
        self.template_path = template_path
        self.output_path = output_path


    def create_rounded_image(self, image_path: str, size: tuple[int, int]):
        def prepare_mask(size, antialias = 2):
            mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
            ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
            return mask.resize(size, Image.LANCZOS)


        def crop(im, s):
            w, h = im.size
            k = w / s[0] - h / s[1]
            if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
            elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
            return im.resize(s, Image.LANCZOS)

        im = Image.open(image_path)
        im = crop(im, size)
        im.putalpha(prepare_mask(size, 4))

        return im


    def put_photo_in_template(self, image: Image, photo_position: tuple[int, int]):
        im = Image.open(self.template_path)
        im.paste(image, (20, 50))

        return im


    def draw_text_on_image(self, image: Image, text: str, text_position: tuple[int, int]):
        draw = ImageDraw.Draw(image)
        draw.text(text_position, text, (0, 0, 0))
        image.save(self.output_path)

    def do_all(self, image_path: Image, photo_position: tuple[int, int], text: str, text_position: tuple[int, int]):
        rounded_image = self.create_rounded_image(image_path)
        template_with_photo = self.put_photo_in_template(rounded_image, photo_position)
        self.draw_text_on_image(template_with_photo, text, text_position)
