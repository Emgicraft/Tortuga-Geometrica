from turtle import Turtle

# Instancia un objeto Turtle
t = Turtle()

# Configura la pantalla
t.screen.title('Cuadrado')  # Título de la ventana
t.screen.bgcolor("gray")  # Color de fondo de la ventana

# Configura la tortuga
t.color("blue")  # Cambia el color de la tortuga a azul
t.pensize(2)  # Cambia el grosor del lápiz de la

# Mueve la tortuga para formar un cuadrado
lado = 200  # Longitud del lado del cuadrado
for _ in range(4):
    t.forward(lado)  # Mueve la tortuga hacia adelante
    t.left(90)  # Gira la tortuga 90 grados a la derecha

# Mantiene la ventana abierta
t.screen.mainloop()