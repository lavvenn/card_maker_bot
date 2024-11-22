from PIL import Image, ImageDraw


def create_rounded_image(image_path: str, output_path: str, size: tuple[int, int]):
        # Подготавливает маску, рисуя её в <antialias> раз больше и
        # затем уменьшая, чтобы получилось сглаженно.
        def prepare_mask(size, antialias = 2):
            mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
            ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
            return mask.resize(size, Image.LANCZOS)

        # Обрезает и масштабирует изображение под заданный размер.
        # Вообще, немногим отличается от .thumbnail, но по крайней мере
        # у меня результат получается куда лучше.
        def crop(im, s):
            w, h = im.size
            k = w / s[0] - h / s[1]
            if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
            elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
            return im.resize(s, Image.LANCZOS)

        im = Image.open(image_path)
        im = crop(im, size)
        im.putalpha(prepare_mask(size, 4))
        im.save(output_path)


def put_photo_in_template(image_path: str, template_path: str, output_path: str):
    im = Image.open(template_path)
    im.paste(Image.open(image_path), (20, 50), Image.open(image_path))
    im.save(output_path)


def draw_text_on_image(image_path: str, text: str, output_path: str):
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    draw.text((200, 10), text, (0, 0, 0))
    im.save(output_path)


def main():
    create_rounded_image('images/image.png', 'images/image_rounded.png', (150, 150))
    put_photo_in_template('images/image_rounded.png', 'images/template.png', 'images/image_in_template.png')
    draw_text_on_image('images/image_in_template.png', 'Hello, world!', 'images/image_with_text.png')


if __name__ == '__main__':
    main()