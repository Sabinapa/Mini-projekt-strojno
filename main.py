from PIL import Image, ImageDraw

pot_do_slike = "abceda1.jpg"
slika = Image.open(pot_do_slike)

# Ugotovite sredino slike
sirina, visina = slika.size
sredina_x = sirina // 2
sredina_y = visina // 2

# Ustvarite objekt za risanje na sliki
risanje = ImageDraw.Draw(slika)

# Narišite črto na sredini slike (kot preverjanje risanja)
barva_crte = (255, 0, 0)  # Barva črte v RGB formatu (zelena)
risanje.line([(0, 0), (sredina_x, sredina_y)], fill=barva_crte)

# Prikažite sliko
slika.show()

# Ne pozabite končati z zapiranjem slike
slika.close()
