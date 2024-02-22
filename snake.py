import turtle  # Importa el módulo turtle para trabajar con gráficos
import time  # Importa el módulo time para trabajar con el tiempo
import random  # Importa el módulo random para generar números aleatorios

posponer = 0.1  # Define el tiempo de espera entre actualizaciones de pantalla

# Crea una instancia de la clase Screen del módulo Turtle y la almacena en la variable window.
window = turtle.Screen()
# Modifica el título de la ventana
window.title("Snake")
# Modifica el color de fondo de la ventana
window.bgcolor("black")
# Modifica el tamaño de la ventana
window.setup(width=600, height=600)
# Define la frecuencia de actualización de la pantalla
window.tracer(0)

# Características de la cabeza de la serpiente
cabeza = turtle.Turtle()  # Crea una instancia de Turtle para la cabeza de la serpiente
cabeza.speed(0)  # Establece la velocidad de dibujo de la cabeza
cabeza.shape("circle")  # Establece la forma de la cabeza
cabeza.penup()  # Levanta el lápiz para que no dibuje mientras se mueve
cabeza.goto(0, 0)  # Mueve la cabeza al punto (0, 0) en la pantalla
cabeza.color("white")  # Establece el color de la cabeza
cabeza.direction = "stop"  # Inicialmente, la dirección de la cabeza está detenida

# Características de la comida de la serpiente
comida = turtle.Turtle()  # Crea una instancia de Turtle para la comida de la serpiente
comida.speed(0)  # Establece la velocidad de dibujo de la comida
comida.shape("circle")  # Establece la forma de la comida
comida.penup()  # Levanta el lápiz para que no dibuje mientras se mueve
comida.goto(0, 100)  # Mueve la comida al punto (0, 100) en la pantalla
comida.color("red")  # Establece el color de la comida
comida.direction = "stop"  # Inicialmente, la dirección de la comida está detenida

# Cuerpo de la serpiente, representado como una lista vacía inicialmente
segmentos = []

# Funciones para controlar la dirección de la serpiente
def arriba():
    cabeza.direction = "up"  # Establece la dirección de la cabeza hacia arriba

def abajo():
    cabeza.direction = "down"  # Establece la dirección de la cabeza hacia abajo

def izquierda():
    cabeza.direction = "left"  # Establece la dirección de la cabeza hacia la izquierda

def derecha():
    cabeza.direction = "right"  # Establece la dirección de la cabeza hacia la derecha

# Función para mover la serpiente
def mov():
    if cabeza.direction == "up":  # Si la dirección de la cabeza es hacia arriba
        y = cabeza.ycor()  # Obtiene la coordenada y actual de la cabeza
        cabeza.sety(y + 20)  # Mueve la cabeza hacia arriba agregando 20 a la coordenada y

    if cabeza.direction == "down":  # Si la dirección de la cabeza es hacia abajo
        y = cabeza.ycor()  # Obtiene la coordenada y actual de la cabeza
        cabeza.sety(y - 20)  # Mueve la cabeza hacia abajo restando 20 a la coordenada y

    if cabeza.direction == "left":  # Si la dirección de la cabeza es hacia la izquierda
        x = cabeza.xcor()  # Obtiene la coordenada x actual de la cabeza
        cabeza.setx(x - 20)  # Mueve la cabeza hacia la izquierda restando 20 a la coordenada x

    if cabeza.direction == "right":  # Si la dirección de la cabeza es hacia la derecha
        x = cabeza.xcor()  # Obtiene la coordenada x actual de la cabeza
        cabeza.setx(x + 20)  # Mueve la cabeza hacia la derecha agregando 20 a la coordenada x

# Configuración de los eventos del teclado
window.listen()  # Escucha los eventos del teclado
window.onkeypress(arriba, "Up")  # Asocia la tecla "Arriba" con la función arriba()
window.onkeypress(abajo, "Down")  # Asocia la tecla "Abajo" con la función abajo()
window.onkeypress(izquierda, "Left")  # Asocia la tecla "Izquierda" con la función izquierda()
window.onkeypress(derecha, "Right")  # Asocia la tecla "Derecha" con la función derecha()

# Bucle principal del juego
while True:
    window.update()  # Actualiza continuamente la ventana

    # Verifica si la cabeza de la serpiente alcanza la comida
    if cabeza.distance(comida) < 20:
        # Genera una nueva posición aleatoria para la comida
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Crea un nuevo segmento para la serpiente y lo agrega a la lista de segmentos
        nuevo_segmento = turtle.Turtle()  # Crea una nueva instancia de Turtle
        nuevo_segmento.speed(0)  # Establece la velocidad de dibujo del nuevo segmento
        nuevo_segmento.shape("circle")  # Establece la forma del nuevo segmento
        nuevo_segmento.penup()  # Levanta el lápiz para que no dibuje mientras se mueve
        nuevo_segmento.goto(0, 100)  # Mueve el nuevo segmento al punto (0, 100) en la pantalla
        nuevo_segmento.color("grey")  # Establece el color del nuevo segmento
        nuevo_segmento.direction = "stop"  # Inicialmente, la dirección del nuevo segmento está detenida
        segmentos.append(nuevo_segmento)  # Agrega el nuevo segmento a la lista de segmentos

    # Mueve el cuerpo de la serpiente
    total_Seg = len(segmentos)  # Obtiene la cantidad total de segmentos de la serpiente
    for index in range(total_Seg - 1, 0, -1):  # Itera a través de los segmentos de la serpiente
        x = segmentos[index - 1].xcor()  # Obtiene la coordenada x del segmento anterior
        y = segmentos[index - 1].ycor()  # Obtiene la coordenada y del segmento anterior
        segmentos[index].goto(x, y)  # Mueve el segmento actual a las coordenadas del segmento anterior

    # Mueve el primer segmento del cuerpo a la posición de la cabeza
    if total_Seg > 0:  # Si hay al menos un segmento en el cuerpo de la serpiente
        x = cabeza.xcor()  # Obtiene la coordenada x de la cabeza
        y = cabeza.ycor()  # Obtiene la coordenada y de la cabeza
        segmentos[0].goto(x, y)  # Mueve el primer segmento a las coordenadas de la cabeza

    # Mueve la cabeza de la serpiente
    mov()  # Llama a la función para mover la serpiente
    time.sleep(posponer)  # Espera un tiempo antes de la próxima actualización
