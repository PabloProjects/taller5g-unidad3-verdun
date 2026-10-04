from PIL import Image
import math


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:

        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x0 += sx

        if e2 < dx:
            err += dx
            y0 += sy


def generar_puntos_circulo(cx, cy, radio, n):

    puntos = []

    for i in range(n):

        angulo = 2 * math.pi * i / n

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        puntos.append((x, y))

    return puntos


def dibujar_roseta(pixels, puntos, ancho, alto):

    n = len(puntos)

    for i in range(n):

        for j in range(i + 1, n):

            color = (int(255 * i / n),int(255 * j / n),180)
            x0, y0 = puntos[i]
            x1, y1 = puntos[j]

            bresenham(pixels,x0, y0,x1, y1,color,ancho, alto)



for n in [12, 24, 36]:

    imagen = Image.new("RGB",(700, 700),"white")
    pixels = imagen.load()

    puntos = generar_puntos_circulo(350,350,300,n)

    dibujar_roseta(pixels,puntos,700,700)
    imagen.save(f"roseta_{n}.png")
    print(f"Generada roseta_{n}.png")