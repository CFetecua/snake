import turtle
import time
import random

class Snake_class:
    def __init__(self):
        self.posponer = 0.1
        self.window = turtle.Screen()
        self.window.title("Snake")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.cabeza = turtle.Turtle()
        self.cabeza.speed(0)
        self.cabeza.shape("circle")
        self.cabeza.penup()
        self.cabeza.goto(0, 0)
        self.cabeza.color("white")
        self.cabeza.direction = "stop"

        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape("circle")
        self.comida.penup()
        self.comida.goto(0, 100)
        self.comida.color("red")
        self.comida.direction = "stop"

        self.segmentos = []

        # Configurar eventos del teclado
        self.window.listen()
        self.window.onkeypress(self.arriba, "Up")
        self.window.onkeypress(self.abajo, "Down")
        self.window.onkeypress(self.izquierda, "Left")
        self.window.onkeypress(self.derecha, "Right")

    def arriba(self):
        if self.cabeza.direction != "down":
            self.cabeza.direction = "up"

    def abajo(self):
        if self.cabeza.direction != "up":
            self.cabeza.direction = "down"

    def izquierda(self):
        if self.cabeza.direction != "right":
            self.cabeza.direction = "left"

    def derecha(self):
        if self.cabeza.direction != "left":
            self.cabeza.direction = "right"

    def mov(self):
        if self.cabeza.direction == "up":
            y = self.cabeza.ycor()
            self.cabeza.sety(y + 20)
        elif self.cabeza.direction == "down":
            y = self.cabeza.ycor()
            self.cabeza.sety(y - 20)
        elif self.cabeza.direction == "left":
            x = self.cabeza.xcor()
            self.cabeza.setx(x - 20)
        elif self.cabeza.direction == "right":
            x = self.cabeza.xcor()
            self.cabeza.setx(x + 20)

    def verificar_colision(self):
        if self.cabeza.distance(self.comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self.comida.goto(x, y)

            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("circle")
            nuevo_segmento.penup()
            nuevo_segmento.color("grey")
            self.segmentos.append(nuevo_segmento)

    def main(self):
        self.window.listen()  # Escuchar eventos del teclado
        self.window.onkeypress(self.arriba, "Up")
        self.window.onkeypress(self.abajo, "Down")
        self.window.onkeypress(self.izquierda, "Left")
        self.window.onkeypress(self.derecha, "Right")

        while True:
            self.window.update()
            self.verificar_colision()
            self.mov()
            time.sleep(self.posponer)

            # Mover los segmentos de la serpiente
            total_Seg = len(self.segmentos)
            if total_Seg > 0:
                for index in range(total_Seg - 1, 0, -1):
                    x = self.segmentos[index - 1].xcor()
                    y = self.segmentos[index - 1].ycor()
                    self.segmentos[index].goto(x, y)

                x = self.cabeza.xcor()
                y = self.cabeza.ycor()
                self.segmentos[0].goto(x, y)

            # Agregar un nuevo segmento detrás de la cabeza de la serpiente
            if self.cabeza.direction != "stop":
                nuevo_segmento = turtle.Turtle()
                nuevo_segmento.speed(0)
                nuevo_segmento.shape("circle")
                nuevo_segmento.penup()
                nuevo_segmento.color("grey")
                nuevo_segmento.goto(self.cabeza.xcor(), self.cabeza.ycor())  # Colocar el segmento en la posición de la cabeza
                nuevo_segmento.direction = "stop"
                self.segmentos.insert(0, nuevo_segmento)  # Insertar el nuevo segmento al inicio de la lista



if __name__ == "__main__":
    juego = Snake_class()
    juego.main()