from PIL import Image
import math


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx, dy = x1 - x0, y1 - y0
    pasos = max(abs(dx), abs(dy))

    if pasos == 0:
        return

    x_inc, y_inc = dx / pasos, dy / pasos
    x, y = x0, y0

    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)

        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color

        x += x_inc
        y += y_inc


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    #rectangulo utilizando cuatro lineas DDA.

    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    

    dda(pixels, p1[0], p1[1], p2[0], p2[1],
        color, ancho, alto)

    dda(pixels, p2[0], p2[1], p3[0], p3[1],
        color, ancho, alto)

    dda(pixels, p3[0], p3[1], p1[0], p1[1],
        color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos,color, ancho, alto):
    for i in range(n_rayos):

        angulo = 2 * math.pi * i / n_rayos

        # El rayo comienza cerca del centro
        x0 = cx + int((radio // 2) * math.cos(angulo))
        y0 = cy + int((radio // 2) * math.sin(angulo))

        # El rayo termina en el radio exterior
        x1 = cx + int(radio * math.cos(angulo))
        y1 = cy + int(radio * math.sin(angulo))

        dda(pixels, x0, y0, x1, y1,color, ancho, alto)


def dibujar_ventana(pixels, x0, y0, tam,color, ancho, alto):
    dibujar_rectangulo(pixels,x0,y0,x0 + tam,y0 + tam,color,ancho,alto)


def dibujar_arbol(pixels, x, y, ancho, alto):
    marron = (120, 70, 20)
    verde = (20, 140, 40)
    # Tronco
    dibujar_rectangulo(pixels,x - 12, y,x + 12,y + 70,marron,ancho,alto)
    #triangulo
    dibujar_triangulo(pixels,(x - 45, y),(x, y - 80),(x + 45, y),verde,ancho,alto)


#main
ancho, alto = 600, 500

# Fondo celeste
imagen = Image.new("RGB",(ancho, alto),(200, 230, 255))
pixels = imagen.load()

#colores
color_casa = (190, 80, 50)
color_techo = (120, 40, 40)
color_puerta = (90, 50, 20)
color_ventanas = (30, 120, 220)
color_sol = (255, 190, 0)
color_piso = (40, 130, 50)


#Cuerpo de la casa
dibujar_rectangulo(pixels,180, 230,420, 420, color_casa,ancho, alto)

# Techo
dibujar_triangulo(pixels,(160, 230),(300, 110),(440, 230),color_techo,ancho, alto)

# Puerta
dibujar_rectangulo(pixels,270, 330,330, 420,color_puerta,ancho, alto)

#Ventana Izq
dibujar_ventana(pixels,210, 270,50,color_ventanas,ancho, alto)

# Ventana der
dibujar_ventana(pixels,340, 270,50,color_ventanas,ancho, alto)

# Sol
dibujar_sol(pixels,80, 80,55,12,color_sol,ancho, alto)

# Piso
dda(pixels,0, 420,ancho - 1, 420,color_piso,ancho, alto)

#arbol
dibujar_arbol(pixels,90, 350,ancho, alto)
dibujar_arbol(pixels,510, 350,ancho, alto)
imagen.save("casa.png")
print("Imagen generada correctamente: casa.png")