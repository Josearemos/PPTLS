import random
import tkinter
from tkinter import messagebox


class Logica:
    def __init__(self):
        pass

    def clickhumanopiedra(self,btn_cpu,btn_humano):
        img_piedra = tkinter.PhotoImage(file='piedra.png')
        img_papel = tkinter.PhotoImage(file='papel.png')
        img_tijeras = tkinter.PhotoImage(file='tijeras.png')
        img_lagarto = tkinter.PhotoImage(file='lagarto.png')
        img_spock = tkinter.PhotoImage(file='spock.png')

        imgcpu = random.choice([img_piedra, img_papel, img_tijeras, img_lagarto, img_spock])
        btn_cpu.config(image=imgcpu)
        btn_cpu.place(x=1255, y=310)

        btn_humano.config(image=img_piedra)
        btn_humano.place(x=150, y=310)

        if imgcpu == img_piedra:
            messagebox.showinfo(message="Piedra no aplasta piedra, EMPATAS!!", title="Resultado")

        elif imgcpu == img_papel:
            messagebox.showinfo(message="Papel cubre piedra, PIERDES!!", title="Resultado")

        elif imgcpu == img_tijeras:
            messagebox.showinfo(message="Piedra aplasta tijeras, GANAS!!", title="Resultado")

        elif imgcpu == img_lagarto:
            messagebox.showinfo(message="Piedra aplasta lagarto, GANAS!!", title="Resultado")

        elif imgcpu == img_spock:
            messagebox.showinfo(message="Spock vaporiza piedra, PIERDES!!", title="Resultado")

        btn_humano.place_forget()
        btn_cpu.place_forget()

        return imgcpu,btn_cpu,btn_humano


    def clickhumanopapel(self,btn_cpu,btn_humano):
        img_piedra = tkinter.PhotoImage(file='piedra.png')
        img_papel = tkinter.PhotoImage(file='papel.png')
        img_tijeras = tkinter.PhotoImage(file='tijeras.png')
        img_lagarto = tkinter.PhotoImage(file='lagarto.png')
        img_spock = tkinter.PhotoImage(file='spock.png')

        imgcpu = random.choice([img_piedra, img_papel, img_tijeras, img_lagarto, img_spock])
        btn_cpu.config(image=imgcpu)
        btn_cpu.place(x=1250, y=300)

        btn_humano.config(image=img_papel)
        btn_humano.place(x=150, y=300)

        if imgcpu == img_piedra:
            messagebox.showinfo(message="Papel cubre piedra, GANAS!!", title="Resultado")

        elif imgcpu == img_papel:
            messagebox.showinfo(message="Papel no cubre papel, EMPATAS!!", title="Resultado")

        elif imgcpu == img_tijeras:
            messagebox.showinfo(message="Tijeras cortan papel, PIERDES!!", title="Resultado")

        elif imgcpu == img_lagarto:
            messagebox.showinfo(message="Lagarto come papel, PIERDES!!", title="Resultado")

        elif imgcpu == img_spock:
            messagebox.showinfo(message="Papel desaprueba Spock, GANAS!!", title="Resultado")

        btn_humano.place_forget()
        btn_cpu.place_forget()

        return imgcpu, btn_cpu, btn_humano

    def clickhumanotijeras(self,btn_cpu,btn_humano):
        img_piedra = tkinter.PhotoImage(file='piedra.png')
        img_papel = tkinter.PhotoImage(file='papel.png')
        img_tijeras = tkinter.PhotoImage(file='tijeras.png')
        img_lagarto = tkinter.PhotoImage(file='lagarto.png')
        img_spock = tkinter.PhotoImage(file='spock.png')

        imgcpu = random.choice([img_piedra, img_papel, img_tijeras, img_lagarto, img_spock])
        btn_cpu.config(image=imgcpu)
        btn_cpu.place(x=1250, y=300)

        btn_humano.config(image=img_tijeras)
        btn_humano.place(x=150, y=300)

        if imgcpu == img_piedra:
            messagebox.showinfo(message="Piedra aplasta tijeras, PIERDES!!", title="Resultado")

        elif imgcpu == img_papel:
            messagebox.showinfo(message="Tijeras cortan papel, GANAS!!", title="Resultado")

        elif imgcpu == img_tijeras:
            messagebox.showinfo(message="Tijeras no cortan tijeras, EMPATAS!!", title="Resultado")

        elif imgcpu == img_lagarto:
            messagebox.showinfo(message="Tijeras decapitan lagarto, GANAS!!", title="Resultado")

        elif imgcpu == img_spock:
            messagebox.showinfo(message="Spock destruye tijeras, PIERDES!!", title="Resultado")

        btn_humano.place_forget()
        btn_cpu.place_forget()

        return imgcpu, btn_cpu, btn_humano

    def clickhumanolagarto(self,btn_cpu,btn_humano):
        img_piedra = tkinter.PhotoImage(file='piedra.png')
        img_papel = tkinter.PhotoImage(file='papel.png')
        img_tijeras = tkinter.PhotoImage(file='tijeras.png')
        img_lagarto = tkinter.PhotoImage(file='lagarto.png')
        img_spock = tkinter.PhotoImage(file='spock.png')

        btn_humano.config(image=img_lagarto)
        btn_humano.place(x=150, y=300)

        imgcpu = random.choice([img_piedra, img_papel, img_tijeras, img_lagarto, img_spock])
        btn_cpu.config(image=imgcpu)
        btn_cpu.place(x=1250, y=300)

        if imgcpu == img_piedra:
            messagebox.showinfo(message="Piedra aplasta lagarto, PIERDES!!", title="Resultado")

        elif imgcpu == img_papel:
            messagebox.showinfo(message="Lagarto come papel, GANAS!!", title="Resultado")

        elif imgcpu == img_tijeras:
            messagebox.showinfo(message="Tijeras decapitan lagarto, PIERDES!!", title="Resultado")

        elif imgcpu == img_lagarto:
            messagebox.showinfo(message="Lagarto amigo de lagarto, EMPATAS!!", title="Resultado")

        elif imgcpu == img_spock:
            messagebox.showinfo(message="Lagarto envenena Spock, GANAS!!", title="Resultado")

        btn_humano.place_forget()
        btn_cpu.place_forget()

        return imgcpu, btn_cpu, btn_humano

    def clickhumanospock(self,btn_cpu,btn_humano):

        img_piedra = tkinter.PhotoImage(file='piedra.png')
        img_papel = tkinter.PhotoImage(file='papel.png')
        img_tijeras = tkinter.PhotoImage(file='tijeras.png')
        img_lagarto = tkinter.PhotoImage(file='lagarto.png')
        img_spock = tkinter.PhotoImage(file='spock.png')

        btn_humano.config(image=img_spock)
        btn_humano.place(x=150, y=300)


        imgcpu = random.choice([img_piedra, img_papel, img_tijeras, img_lagarto, img_spock])
        btn_cpu.config(image=imgcpu)
        btn_cpu.place(x=1250, y=300)

        if imgcpu == img_piedra:
            messagebox.showinfo(message="Spock vaporiza piedra, GANAS!!", title="Resultado")

        elif imgcpu == img_papel:
            messagebox.showinfo(message="Papel desaprueba Spock, PIERDES!!", title="Resultado")

        elif imgcpu == img_tijeras:
            messagebox.showinfo(message="Spock destruye tijeras, GANAS!!", title="Resultado")

        elif imgcpu == img_lagarto:
            messagebox.showinfo(message="Lagarto envenena Spock, PIERDES!!", title="Resultado")

        elif imgcpu == img_spock:
            messagebox.showinfo(message="Spock encuentra otros Spock,MULTIVERSO, EMPATAS!!", title="Resultado")

        btn_humano.place_forget()
        btn_cpu.place_forget()

        return imgcpu, btn_cpu, btn_humano