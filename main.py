import os

from PIL import Image, ImageDraw

path_image = "abcrki.jpg"
image = Image.open(path_image)

width, height = image.size
print(width, height)

start_x, start_y = 0, 0
end_x, end_y = width, height

number_squares_x = 10
number_squares_y = 20

width_square = width // number_squares_x
height_square = height // number_squares_y

print(f"Širina kvadrata: {width_square}px")
print(f"Višina kvadrata: {height_square}px")

letter = "B"
fileName = letter

if not os.path.exists(fileName):
    os.makedirs(fileName)

counter = 0
for j in range(number_squares_y):
    for i in range(number_squares_x):
        x1 = i * width_square
        y1 = j * height_square
        x2 = x1 + width_square
        y2 = y1 + height_square
        counter += 1

        if counter == 100:
            letter = 'B'

        cropSquare = image.crop((x1, y1, x2, y2))

        nameOfCropS = f"{fileName}/{letter}{counter}.png"

        cropSquare.save(nameOfCropS)


image.close()
