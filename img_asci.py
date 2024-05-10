from PIL import Image

def ascii_conv(image, saveas):
    img = Image.open(image)
    w, h = img.size

    scalex = (w * 1)//100
    scaleh = (h * 1)//100

    img = img.resize((w//scalex, h//scaleh))
    w, h = img.size
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()

    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = " "
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = " "
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "."
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = "o"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "."
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(700,750):
                grid[y][x] = "@"
            else:
                grid[y][x] = " "

    with open(saveas, 'w') as art:
        for row in grid:
            for char in row:
                art.write(char)
            art.write("\n")

if __name__ == '__main__':
    ascii_conv("shikh_thiffa.jpg", "shikh.txt")
