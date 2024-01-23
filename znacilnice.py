import cv2
import numpy as np
import csv

def count_pixels(cell, color):
    _, thresholded = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    color_value = np.sum(thresholded == color)
    return color_value

grid_size = 5
letter = "Z1"

filenameWhite = f'whitePixels/whitePixels{letter}.csv'
filenameBlack = f'blackPixels/blackPixels{letter}.csv'

with open(filenameWhite, 'w', newline='') as whitePixelsCSV:
    whiteWriter = csv.writer(whitePixelsCSV)

    with open(filenameBlack, 'w', newline='') as blackPixelsCSV:
        blackWriter = csv.writer(blackPixelsCSV)

        for l in range(1, 101):
            path = f"Crke/{letter}/{letter}{l}.png"
            print(path)

            whitePixels = []
            blackPixels = []

            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

            cell_size = image.shape[0] // grid_size

            for i in range(grid_size):
                for j in range(grid_size):
                    cell = image[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]

                    whiteValue = count_pixels(cell, 255)
                    blackValue = count_pixels(cell, 0)

                    whitePixels.append(whiteValue)
                    blackPixels.append(blackValue)

            # append letter to the end of the list
            whitePixels.append(letter)
            blackPixels.append(letter)
            whiteWriter.writerow(whitePixels)
            blackWriter.writerow(blackPixels)