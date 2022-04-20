from PIL import Image
import glob

list_img = glob.glob('images/*.jpg')

## This code will find out what the smallest resolution is from all the images.
# def minimum_dimensions():
#     min_width = 20000
#     min_height = 20000
#     for img in list_img:
#         size = Image.open(img).size
#         width = size[0]
#         height = size[1]
#         if width < min_width:
#             min_width = width
#         if height < min_height:
#             min_height = height
#     print(min_width)
#     print(min_height)

# final_size = 512
# img = Image.open(list_img[0])
# black_img = Image.new(mode='RGB', size=(final_size, final_size))
# prev_size = img.size
# max_dim = max(img.size)
# ratio = final_size / max_dim
# new_img_size = (int(prev_size[0] * ratio), int(prev_size[1] * ratio))
# new_img = img.resize(new_img_size)
# black_img.paste(new_img, ((final_size - new_img_size[0]) // 2, (final_size - new_img_size[1]) // 2))
# black_img.show

min_width = 512
final_size = 512
for n, img in enumerate(list_img[:50], 1):
    next_img = Image.open(img)
    if next_img.mode != 'RGB':
        next_img.mode = 'RGB'
    black_img = Image.new(mode='RGB', size=(final_size, final_size))
    # prev_size = img.size
    # max_dim = max(img.size)
    # ratio = final_size / max_dim
    # new_img_size = (int(prev_size[0] * ratio), int(prev_size[1] * ratio))
    # new_img = img.resize(new_img_size)
    # black_img.paste(new_img, ((final_size - new_img_size[0]) // 2, (final_size - new_img_size[1]) // 2))
    # black_img.save(f'image_{n}.jpg')