from turtle import Turtle

# Instancia un objeto Turtle
t = Turtle()
# Configura la pantalla
t.screen.title('Triangulo Equilatero') # Título de la ventana
t.screen.bgcolor("gray") # Color de fondo de la ventana

# Configura la tortuga
#t.speed(2) # Velocidad de la tortuga
t.color("azul")  # Cambia el color de la tortuga y su trazo a azul
t.pensize(2)  # Cambia el grosor del lápiz de la tortuga
#t.shape("turtle")  # Cambia la forma de la tortuga a "tortuga"
t.fillcolor("skyblue")  # Cambia el color de relleno a celeste

# Esto activa internamente un flag filling = True y comienza a 
# acumular la secuencia de vértices (las posiciones de la tortuga) en un buffer.
t.begin_fill() # Tal que con cada segmento dibujado se añade a ese buffer de vértices

# Mueve la tortuga
# Por defecto, la tortuga mira hacia la derecha
lado = 300  # Longitud del lado del triángulo
t.forward(lado)  # Mueve la tortuga hacia adelante 100 unidades
t.left(120)    # Gira la tortuga 120 grados a la izquierda
t.forward(lado)  # Mueve la tortuga hacia adelante 100 unidades
t.left(120)    # Gira la tortuga 120 grados a la izquierda
t.forward(lado)  # Mueve la tortuga hacia adelante 100 unidades

# Al invocar end_fill(), Turtle toma la lista completa de puntos 
# almacenados desde el begin_fill(), le añade automáticamente un 
# segmento que conecta el último punto con el primero (cerrando 
# la figura “por ti”) y crea un polígono en pantalla usando 
# create_polygon(..., fill=fillcolor).
t.end_fill()

t.right(90)
t.forward(100)

# Ambos métodos son equivalentes
#t.mainloop() # Forma 1: es un atajo para llamar a Forma 2
t.screen.mainloop() # Forma 2