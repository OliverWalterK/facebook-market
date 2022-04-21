from sqlalchemy import create_engine
from PIL import Image
import os

path = "images/"
dirs = os.listdir(path)

def connect_to_db():
    host = 'products.c8k7he1p0ynz.us-east-1.rds.amazonaws.com'
    password = 'aicore2022!'
    port = 5432
    user = 'postgres'
    database = 'postgres'
    api_type = 'psycopg2'
    engine = create_engine(f'postgresql+{api_type}://{user}:{password}@{host}:{port}/{database}')
    engine.connect()
    return engine

## This code will find out what the smallest resolution is from all the images.
def minimum_dimensions():
    min_width = 20000
    min_height = 20000
    for img in dirs:
        size = Image.open(img).size
        width = size[0]
        height = size[1]
        if width < min_width:
            min_width = width
        if height < min_height:
            min_height = height
    print(min_width)
    print(min_height)

def resize_image(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im

if __name__ == '__main__':
    final_size = 512
    for n, item in enumerate(dirs[:5], 1):
        im = Image.open('images/' + item)
        if im.mode != 'RGB':
            im.mode = 'RGB'
        new_im = resize_image(final_size, im)
        new_im.save(f'{n}_resized.jpg')