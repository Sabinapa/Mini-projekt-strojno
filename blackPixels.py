import os

file = 'blackPixels/'

outputFile = 'BLACKPixels.csv'

with open(outputFile, 'w') as izhod:

    for filename in os.listdir(file):
        if filename.endswith(".csv"):
            path = os.path.join(file, filename)

            with open(path, 'r') as datoteka:
                vsebina = datoteka.read()

                izhod.write(vsebina)

print(f"Združena koda je shranjena v datoteki {outputFile}.")
