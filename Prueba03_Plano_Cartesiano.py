import turtle

# —————— Configuración inicial ——————
GRID_SPACING = 50       # separación entre líneas de la cuadrícula
PAN_STEP     = 100      # unidades que desplazamos al presionar flecha

screen = turtle.Screen()
screen.title("Plano cartesiano con Turtle")
screen.tracer(False)    # desactiva animación automática para dibujar rápido

# Ajuste inicial: coordenadas del mundo coinciden con la ventana
# (xmin, ymin, xmax, ymax)
xmin, ymin = -screen.window_width()//2, -screen.window_height()//2
xmax, ymax =  screen.window_width()//2,  screen.window_height()//2
screen.setworldcoordinates(xmin, ymin, xmax, ymax)

# Tortuga auxiliar para dibujar ejes y cuadrícula
drawer = turtle.Turtle(visible=False)
drawer.pensize(1)
drawer.color("#444444")  # gris oscuro

# —————— 1. Ejes ——————
# Eje X
drawer.penup()
drawer.goto(xmin, 0)
drawer.pendown()
drawer.goto(xmax, 0)

# Eje Y
drawer.penup()
drawer.goto(0, ymin)
drawer.pendown()
drawer.goto(0, ymax)

# —————— 2. Cuadrícula ——————
# Líneas verticales
for x in range(int(xmin/GRID_SPACING)*GRID_SPACING,
               int(xmax/GRID_SPACING)*GRID_SPACING + 1,
               GRID_SPACING):
    if x == 0: continue
    drawer.penup()
    drawer.goto(x, ymin)
    drawer.pendown()
    drawer.goto(x, ymax)

# Líneas horizontales
for y in range(int(ymin/GRID_SPACING)*GRID_SPACING,
               int(ymax/GRID_SPACING)*GRID_SPACING + 1,
               GRID_SPACING):
    if y == 0: continue
    drawer.penup()
    drawer.goto(xmin, y)
    drawer.pendown()
    drawer.goto(xmax, y)

screen.tracer(True)  # reactiva animación

# —————— 3. Panning con teclas ——————
def pan_left():
    global xmin, xmax
    xmin -= PAN_STEP; xmax -= PAN_STEP
    screen.setworldcoordinates(xmin, ymin, xmax, ymax)

def pan_right():
    global xmin, xmax
    xmin += PAN_STEP; xmax += PAN_STEP
    screen.setworldcoordinates(xmin, ymin, xmax, ymax)

def pan_up():
    global ymin, ymax
    ymin += PAN_STEP; ymax += PAN_STEP
    screen.setworldcoordinates(xmin, ymin, xmax, ymax)

def pan_down():
    global ymin, ymax
    ymin -= PAN_STEP; ymax -= PAN_STEP
    screen.setworldcoordinates(xmin, ymin, xmax, ymax)

screen.listen()
screen.onkey(pan_left,  "Left")
screen.onkey(pan_right, "Right")
screen.onkey(pan_up,    "Up")
screen.onkey(pan_down,  "Down")

# —————— Tortuga de dibujo ——————
t = turtle.Turtle()
t.color("blue")
t.pensize(2)

# Ejemplo de dibujo fuera del marco inicial:
t.penup()
#t.goto(200, 150)
t.goto(0, 0)
t.pendown()
t.circle(750)

screen.mainloop()
