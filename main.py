import os

from PIL import Image, ImageDraw

path_image = "Abceda/crkaz.jpg"
letter_1 = "Z1"
letter_2 = "Z"
image = Image.open(path_image)

width, height = image.size
print(width, height)

number_squares_x = 10
number_squares_y = 20

width_square = width // number_squares_x
height_square = height // number_squares_y

print(f"Širina kvadrata: {width_square}px")
print(f"Višina kvadrata: {height_square}px")

counter_A = 0
counter_B = 0

folder_A = letter_1
if not os.path.exists(folder_A):
    os.makedirs(folder_A)

folder_B = letter_2
if not os.path.exists(folder_B):
    os.makedirs(folder_B)

start_y_B, start_x_B = 0, 0
break_outer = False

for j in range(number_squares_y):
    for i in range(number_squares_x):
        x1 = i * width_square
        y1 = j * height_square
        x2 = x1 + width_square
        y2 = y1 + height_square
        counter_A += 1

        if counter_A == 101:
            start_y_B = j
            start_x_B = 0
            break_outer = True
            break
        crop_square = image.crop((x1, y1, x2, y2))
        name_of_crop = f"{folder_A}/{letter_1}{counter_A}.png"
        crop_square.save(name_of_crop)

    if break_outer:
        break


for j in range(start_y_B, number_squares_y):
    for i in range(start_x_B, number_squares_x):
        x1 = i * width_square
        y1 = j * height_square
        x2 = x1 + width_square
        y2 = y1 + height_square
        counter_B += 1
        crop_square = image.crop((x1, y1, x2, y2))
        name_of_crop = f"{folder_B}/{letter_2}{counter_B}.png"
        crop_square.save(name_of_crop)

image.close()

