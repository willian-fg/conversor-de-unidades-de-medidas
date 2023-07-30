from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Cores

cor1 = '#3b3b3b'  # Preto
cor2 = '#ffffff'  # Branco
cor3 = '#48b3e0'  # Azul

janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=cor1)

# ------------------Frames---------------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=250, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=0, relief='flat')
frame_direita.place(x=454, y=2)

# ------------------Estilos---------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# ------------------Label frame cima---------------------

l_app_nome = Label(frame_cima, text="Calculadora de Unidades de Medidas", height=1, padx=0, relief='flat',
                   anchor="center", font="Ivy 15 bold", bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

# ------------------Frames Esquerdos---------------------

img_0 = Image.open("icons/icons8-peso-50.png")
img_0 = img_0.resize((50, 50), Image.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text="Massa", image=img_0, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw",
             font="Ivy 10 bold", bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

img_1 = Image.open("icons/icons8-tempo-50.png")
img_1 = img_1.resize((50, 50), Image.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, text="Tempo", image=img_1, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw",
             font="Ivy 10 bold", bg=cor3, fg=cor2)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

img_2 = Image.open("icons/icons8-comprimento-50.png")
img_2 = img_2.resize((50, 50), Image.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, text="Comprimento", image=img_2, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw",
             font="Ivy 10 bold", bg=cor3, fg=cor2)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

img_3 = Image.open("icons/icons8-quadrado-80.png")
img_3 = img_3.resize((50, 50), Image.LANCZOS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text="Área", image=img_3, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw",
             font="Ivy 10 bold", bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

img_4 = Image.open("icons/icons8-volume-50.png")
img_4 = img_4.resize((50, 50), Image.LANCZOS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_esquerda, text="Volume", image=img_4, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw", font="Ivy 10 bold", bg=cor3, fg=cor2)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

img_5 = Image.open("icons/icons8-velocidade-50.png")
img_5 = img_5.resize((50, 50), Image.LANCZOS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_esquerda, text="Velocidade", image=img_5, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw", font="Ivy 10 bold", bg=cor3, fg=cor2)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

img_6 = Image.open("icons/icons8-temperatura-50.png")
img_6 = img_6.resize((50, 50), Image.LANCZOS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_esquerda, text="Temperatura", image=img_6, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw", font="Ivy 10 bold", bg=cor3, fg=cor2)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

img_7 = Image.open("icons/icons8-energia-50.png")
img_7 = img_7.resize((50, 50), Image.LANCZOS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_esquerda, text="Energia", image=img_7, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw", font="Ivy 10 bold", bg=cor3, fg=cor2)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

img_8 = Image.open("icons/icons8-pressão-50.png")
img_8 = img_8.resize((50, 50), Image.LANCZOS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_esquerda, text="Pressão", image=img_8, compound=LEFT, width=130, height=50, relief='flat',
             overrelief='solid', anchor="nw", font="Ivy 10 bold", bg=cor3, fg=cor2)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)

# ------------------Frames Direitos---------------------

l_Unidade_nome = Label(frame_direita, text="Unidade", width=17, height=2, padx=0, pady=0, relief='groove',
                       anchor="center", font="Ivy 15 bold", bg=cor2, fg=cor1)
l_Unidade_nome.place(x=0, y=0)

janela.mainloop()
