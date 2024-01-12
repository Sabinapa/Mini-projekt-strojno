import os

from PIL import Image, ImageDraw

pot_do_slike = "abcrki.jpg"
slika = Image.open(pot_do_slike)


# Width, height
sirina, visina = slika.size
print(sirina, visina)

start_x = 0
start_y = 0
end_x = sirina
end_y = visina

stevilo_kvadratov_x = 10
stevilo_kvadratov_y = 20

# Višina in širina kvadrata
sirina_kvadrata = sirina // stevilo_kvadratov_x
visina_kvadrata = visina // stevilo_kvadratov_y

print(f"Širina kvadrata: {sirina_kvadrata}px")
print(f"Višina kvadrata: {visina_kvadrata}px")

crka = "A"
# Mapa za shranjevanje izrezanih kvadratov
mapa_izrezanih_kvadratov = crka

# Prepričajte se, da mapa obstaja, če ne, jo ustvarite
if not os.path.exists(mapa_izrezanih_kvadratov):
    os.makedirs(mapa_izrezanih_kvadratov)

counter = 0
# Izreži in shrani kvadrate
for j in range(stevilo_kvadratov_y):
    for i in range(stevilo_kvadratov_x):
        # Izračunaj koordinate vsakega kvadrata
        x1 = i * sirina_kvadrata
        y1 = j * visina_kvadrata
        x2 = x1 + sirina_kvadrata
        y2 = y1 + visina_kvadrata
        counter += 1

        if counter == 100:
            crka = 'B'

        # Izreži kvadrat
        izrezan_kvadrat = slika.crop((x1, y1, x2, y2))

        # Sestavi pot za shranjevanje
        pot_do_izrezanega_kvadrata = f"{mapa_izrezanih_kvadratov}/{crka}{counter}.png"

        # Shrani izrezan kvadrat
        izrezan_kvadrat.save(pot_do_izrezanega_kvadrata)

'''
# Ustvarite objekt za risanje na sliki
risanje = ImageDraw.Draw(slika)

# Narišite črto na sredini slike (kot preverjanje risanja)
barva_crte = (255, 0, 0)  # Barva črte v RGB formatu (zelena)
risanje.line([(0,125), (150,125)], fill=barva_crte)

# Prikažite sliko
slika.show()
'''

# Ne pozabite končati z zapiranjem slike
slika.close()
