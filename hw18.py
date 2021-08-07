#!/usr/bin/python3

from PIL import Image
sizes = [(90, 90), (130, 130), (200, 200), (250, 250)]
files = ['hw17.jpg', 'hw18_1.jpg', 'hw18_2.jpg', 'hw18_3.jpg']
new_names = []


def image_resize(big_image, photo_size):
    try:
        with Image.open(big_image) as im:
            im.thumbnail(photo_size)
            photo_size = list(map(str, photo_size))
            new_names.append(f"{big_image.split('.')[0] + '_' + '_'.join(photo_size)}.jpg")
            im.save(f"{big_image.split('.')[0] + '_' + '_'.join(photo_size)}.jpg")
    except Exception as e:
        print("Error" + str(e))


# меняем размер фотографий files на размер sizes
for image, size in zip(files, sizes):
    image_resize(image, size)


# Вывод на печать
for new, old in zip(new_names, files):
    # print(new, old)
    with Image.open(old) as old_photo:
        print(f"Старый размер фото {old}: {old_photo.size}")
    with Image.open(new) as new_photo:
        print(f"Новый размер фото {new}: {new_photo.size}")
