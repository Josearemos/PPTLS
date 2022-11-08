import tkinter
from tkinter import *
from Logica import Logica


#Llamada a la logica
logicaobjetos = Logica()

#Primera Ventana

pantallaprincipal = Tk()

#TITULO
pantallaprincipal.title("PPTLS")

#TAMAÑO Y NO PUEDE CAMBIAR EL TAMAÑO
pantallaprincipal.geometry('1600x1000')
pantallaprincipal.geometry("+%d+%d" % (500,200))
pantallaprincipal.resizable(0,0)

#BACKGROUND
imagenfondo = PhotoImage(file = "fondojuego.png")
background = Label(pantallaprincipal,image = imagenfondo, text = "")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


#IMAGENES BOTONES
img_piedra = tkinter.PhotoImage(file='piedra.png')
img_papel = tkinter.PhotoImage(file='papel.png')
img_tijeras = tkinter.PhotoImage(file='tijeras.png')
img_lagarto = tkinter.PhotoImage(file='lagarto.png')
img_spock = tkinter.PhotoImage(file='spock.png')

#BOTONES
btn_humano = Button(pantallaprincipal,
                image="",
                command=lambda:[],
                width=235, height=229,
                anchor="center",
                font=("Verdana", 14))
btn_humano.place(x=250, y=280)
btn_humano.place_forget()

btn_cpu = Button(pantallaprincipal,
                image="",
                command=lambda:[],
                width=235, height=229,
                anchor="center",
                font=("Verdana", 14))
btn_cpu.place(x=1150, y=280)
btn_cpu.place_forget()

btn_piedra = Button(pantallaprincipal,
                image= img_piedra,
                command=lambda: [logicaobjetos.clickhumanopiedra(btn_cpu,btn_humano)],
                width=235, height=229,
                anchor="center",
                font=("Verdana",14))
btn_piedra.place(x=70, y=740)


btn_papel = Button(pantallaprincipal,
                    image=img_papel,
                    command=lambda: [logicaobjetos.clickhumanopapel(btn_cpu,btn_humano)],
                    width=235, height=229,
                    anchor="center",
                    font=("Verdana", 14))
btn_papel.place(x=400, y=740)


btn_tijeras = Button(pantallaprincipal,
                    image=img_tijeras,
                    command=lambda:[logicaobjetos.clickhumanotijeras(btn_cpu,btn_humano)],
                    width=235, height=229,
                    anchor="center",
                    font=("Verdana", 14))
btn_tijeras.place(x=700, y=740)

btn_lagarto = Button(pantallaprincipal,
                    image=img_lagarto,
                    command=lambda: [logicaobjetos.clickhumanolagarto(btn_cpu,btn_humano)],
                    width=235, height=229,
                    anchor="center",
                    font=("Verdana", 14))
btn_lagarto.place(x=1000, y=740)

btn_spock = Button(pantallaprincipal,
                    image=img_spock,
                    command=lambda: [logicaobjetos.clickhumanospock(btn_cpu,btn_humano)],
                    width=235, height=229,
                    anchor="center",
                    font=("Verdana", 14))
btn_spock.place(x=1300, y=740)



pantallaprincipal.mainloop()


#REGLAS
#Piedra aplasta lagarto
#Piedra aplasta tijeras

#Papel cubre piedra
#Papel desaprueba Spock

#Tijeras cortan papel
#Tijeras decapitan lagarto

#Lagarto envenena Spock
#Lagarto come papel

#Spock destruye tijeras
#Spock vaporiza piedra