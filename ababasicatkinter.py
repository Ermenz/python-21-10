from tkinter import *
from PIL import Image, ImageTk

cor1 = "#6495ED" #azul


janela = Tk()
janela.title("ABA PSICOLOGIA")
janela.geometry("1000x1000")
janela.config(bg = "#6495ED")

janela.iconphoto(False, PhotoImage(file ="frank ocean.gif"))
janela.resizable(width=False, height=False)
img = ImageTk.PhotoImage(Image.open("frank ocean.gif"))
l_logo = Label(janela, image=img)
l_logo.place(x=80, y=10)



janela.mainloop()




