from tkinter import *

janela_login = Tk()
janela_login.title('Login')
frame_cabecalho_login = Frame(janela_login)
frame_conteudo_login = Frame(janela_login)
janela_login.geometry('500x300')

# Cabeçalho
texto_orientação_1 = Label(frame_cabecalho_login, text='Faça Login')
texto_orientação_1.grid(row=1, column=1, padx=10, pady=25, columnspan=4)

# Conteudo
texto_orientacao_usuario_login = Label(frame_conteudo_login, text='Digite o seu usuario:')
texto_orientacao_usuario_login.grid(row=1, column=1, padx=5, pady=20, columnspan=2)
usuario_login = Entry(frame_conteudo_login)
usuario_login.grid(row=1, column=3, padx=10, pady=10, columnspan=4)

texto_orientação_senha_login = Label(frame_conteudo_login, text='Digite a sua senha:')
texto_orientação_senha_login.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
senha_login = Entry(frame_conteudo_login)
senha_login.grid(row=2, column=3, padx=10, pady=10, columnspan=4)

logar = Button(frame_conteudo_login, text='Logar')
logar.grid(row=3, column=2, padx=10, pady=20, columnspan=3)

# Configurações
janela_login.configure(background='black')
frame_cabecalho_login.configure(background='black')
frame_conteudo_login.configure(background='black')
texto_orientação_1.configure(background='black', foreground='white', font=('Arial Black', 16, 'italic'))
texto_orientacao_usuario_login.configure(background='black', foreground='white', font=('Times', 12, 'italic'))
texto_orientação_senha_login.configure(background='black', foreground='white', font=('Times', 12, 'italic'))

frame_cabecalho_login.pack()
frame_conteudo_login.pack()
Tk.mainloop(janela_login)