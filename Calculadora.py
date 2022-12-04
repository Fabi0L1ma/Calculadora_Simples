from tkinter import *

cor1 = '#1979a9' #AZUL
cor2 = '#f7efed' #BRANCO
cor3 = '#333030' #CINZA
cor4 = '#c20606' #VERMELHO

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

# Criando frames

frame_tela = Frame(janela, width=235, height=50, bg=cor4)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variavel

todos_valores = ''

# Função de entrada de valores:

def entar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Valor na tela:
    valor_texto.set(todos_valores)

# Função dos calculos:

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# Função limpar a tela:

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# Criando label:

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# BOTÕES:

# Botões de limpar, Modulo e Divisão

b_1 = Button(frame_corpo, command=limpar_tela, text='C',width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command= lambda: entar_valores('%'), text='%',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command= lambda: entar_valores('/'), text='/',width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)


# Botões 7, 8, 9 e Multiplicação

b_5 = Button(frame_corpo, command= lambda: entar_valores('7'), text='7',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=52)

b_6 = Button(frame_corpo, command= lambda: entar_valores('8'), text='8',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=59, y=52)

b_7 = Button(frame_corpo, command= lambda: entar_valores('9'), text='9',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=52)

b_8 = Button(frame_corpo, command= lambda: entar_valores('*'), text='*',width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=177, y=52)


# Botões 4, 5, 6 e Subtração

b_9 = Button(frame_corpo, command= lambda: entar_valores('4'), text='4',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=104)

b_10 = Button(frame_corpo, command= lambda: entar_valores('5'), text='5',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=59, y=104)

b_11 = Button(frame_corpo, command= lambda: entar_valores('6'), text='6',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=118, y=104)

b_12 = Button(frame_corpo, command= lambda: entar_valores('-'), text='-',width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=177, y=104)


# Botões 1, 2, 3 e Soma

b_13 = Button(frame_corpo, command= lambda: entar_valores('1'), text='1',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=156)

b_14 = Button(frame_corpo, command= lambda: entar_valores('2'), text='2',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=59, y=156)

b_15 = Button(frame_corpo, command= lambda: entar_valores('3'), text='3',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=118, y=156)

b_16 = Button(frame_corpo, command= lambda: entar_valores('+'), text='+',width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=177, y=156)


# Botões 0, ponto e igual.

b_17 = Button(frame_corpo, command= lambda: entar_valores('0'), text='0',width=11, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=0, y=208)

b_18 = Button(frame_corpo, command= lambda: entar_valores('.'), text='.',width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=118, y=208)

b_19 = Button(frame_corpo, command= calcular, text='=',width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=177, y=208)


janela.mainloop()

