from turtle import Turtle, listen, Screen
maxon = Turtle ()
tela = Screen()
maxon.speed(0)
maxon.pensize(5)

def goto_and_mark(x, y):
    maxon.goto(x, y)

def Quadrado():
    maxon.forward(100)
    maxon.right(90)
    maxon.forward(100)
    maxon.right(90)
    maxon.forward(100)

def Circulo():
    r = 45
    maxon.pendown()
    maxon.circle(r)

escolha = ''

while(escolha != 0):

    print("-----------------------------")
    print("o Que voce quer ver desenhado?")
    print("1: Quadrado")
    print("2: Circulo")
    print("0: Parar")
    escolha = int(input())
    cor = input("que cor voce quer ver o desenho? ")
    maxon.color(cor)
    if escolha == 1:
        Quadrado()
    if escolha == 2:
        Circulo()

listen()
tela.mainloop()















