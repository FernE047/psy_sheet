from PIL import Image

output = []
def getColorIndex(color):
    return color

img = Image.open('Pokemans_054.png')
width, height = img.size
for y in range(height):
    line = []
    for x in range(width):
        color = img.getpixel((x, y))
        line.append(color)
    output.append(line)
with open('Pokemans_054.txt', 'w') as f:
    for line in output:
        f.write(' '.join(str(x) for x in line) + '\n')