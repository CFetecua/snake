import turtle
"""
Muestra una ventana
"""
cursor = turtle.Turtle()

"""
hacer un cuadrado moviendo el cursor
"""
for i in range(0,4):
    cursor.forward(100)
    cursor.left(90)

"""
Mantiene la ventana abierta, con un bucle infinito
a la espera de interaccion del usuario
"""
turtle.mainloop()