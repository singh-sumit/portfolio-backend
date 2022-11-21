from PIL import Image
from pathlib import Path


def resize_image(image, height, width, replace=False):
    img = Image.open(image.path)

    if img.height > height or img.width > width:
        img.thumbnail((height, width))
        img.save(image.path)  # saving image to same path

    if replace:
        remove_image(image)

def remove_image(image):
    pass

def renamed_image_loc(instance, filename):
    upload_to = "tech/icons/"
    ext = filename.split('.')[-1]

    if not instance.id:
        filename = '{}.{}'.format(instance.name.lower(), ext)

    return Path(upload_to).joinpath(filename)