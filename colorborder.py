from PIL import Image
import os

def color_edges(input_path, output_path, edge_color, edge_size):
    image = Image.open(input_path)

    image = image.convert("RGBA")
    data = image.getdata()

    newData = []
    for y in range(image.height):
        for x in range(image.width):
            if x < edge_size or x >= image.width - edge_size or y < edge_size or y >= image.height - edge_size: #if we are on edge color white
                newData.append(edge_color)
            else:
                newData.append(data[y * image.width + x])

    image.putdata(newData)
    image.save(output_path, "PNG")


input_folder = "Z1"
output_folder = "Crke/Z1"

edge_color = (255, 255, 255, 255) # color white for edge
edge_size = 15

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        color_edges(input_path, output_path, edge_color, edge_size)
