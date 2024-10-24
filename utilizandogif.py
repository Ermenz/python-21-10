from tkinter import *
from PIL import Image, ImageTk  # Pillow para trabalhar com imagens

cor1 = "#6495ED"  # azul

# Função para exibir GIF animado
def atualizar_gif(ind):
    frame = frames[ind]
    l_logo.configure(image=frame)  # Atualiza o frame no Label
    ind += 1
    if ind == frame_count:  # Reinicia o GIF quando chegar ao último frame
        ind = 0
    janela.after(100, atualizar_gif, ind)  # Atualiza a cada 100ms (ajuste conforme a velocidade desejada)

# Criar a janela principal
janela = Tk()
janela.title("ABA PSICOLOGIA")
janela.geometry("1000x1000")
janela.config(bg=cor1)

# Carregar o ícone da janela
janela.iconphoto(False, PhotoImage(file="frank ocean.gif"))

# Tornar a janela não redimensionável
janela.resizable(width=True, height=True)

# Carregar o GIF animado com Pillow
gif = Image.open("frank ocean.gif")

# Extrair frames do GIF
frames = []
frame_count = gif.n_frames  # Conta o número de frames no GIF
for i in range(frame_count):
    gif.seek(i)  # Navega pelos frames do GIF
    frame = ImageTk.PhotoImage(gif.copy())  # Copia o frame atual
    frames.append(frame)

# Criar um Label para exibir o GIF
l_logo = Label(janela)
l_logo.place(x=100, y=100)

# Iniciar a animação do GIF
janela.after(0, atualizar_gif, 0)

# Loop principal da janela
janela.mainloop()
