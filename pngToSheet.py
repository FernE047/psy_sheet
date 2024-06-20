from PIL import Image

#each color will have an index
colors = {}
#o output é uma lista de listas, onde cada lista é uma linha da imagem
output = []
#cores é concatenação de RGB com 3 digitos
def getColorIndex(color):
    return color

img = Image.open('Pokemans_054.png')
width, height = img.size
for y in range(height):
    line = []
    for x in range(width):
        color = img.getpixel((x, y))
        colorIndex = getColorIndex(color)
        if colorIndex not in colors:
            colors[colorIndex] = len(colors)
        line.append(colors[colorIndex])
    output.append(line)
with open('Pokemans_054.txt', 'w') as f:
    for line in output:
        f.write(' '.join(str(x) for x in line) + '\n')