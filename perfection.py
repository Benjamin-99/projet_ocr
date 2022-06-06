from PIL import Image

img = Image.open("Images/cnirecto.png")
img.size
largeur_image = 1200
hauteur_image = 764
for y in range(hauteur_image):
    for x in range(largeur_image):
        t, r, v, b = img.getpixel((x, y))
        print(img.getpixel((x, y)))
        if (150 < t < 220) or (150 < r < 220) or (150 < v < 255):
            img.putpixel((x, y), (255, 255, 255, 255))
img.show()
img.save("result.png")
print(img.size)

