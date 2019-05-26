from io import BytesIO
import numpy as np
from PIL import Image
from flask import send_file


def get_rgb_from_int(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return red, green, blue


def replace_color(img: Image, orig_color, replacement_color):
    im = img.convert('RGBA')

    data = np.array(im)  # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    white_areas = (red == orig_color[0]) & (blue == orig_color[1]) & (green == orig_color[2])
    data[..., :-1][white_areas.T] = replacement_color  # Transpose back needed

    return Image.fromarray(data)


def serve_pil_image(pil_img: Image):
    # https://stackoverflow.com/a/10170635
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
