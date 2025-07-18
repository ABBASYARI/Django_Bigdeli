from PIL import Image

img = Image.open(r"C:\Users\AbbasYari\Desktop\kingfisher-9174586_1280.jpg")
img.save("image_compressed.webp", format="webp", optimize=True, quality=80)
