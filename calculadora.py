from tkinter import *

Calculadora = Tk()
Calculadora.title('Calculadora')
Calculadora.geometry('335x415')
Calculadora.resizable(False, False)
Calculadora['bg'] = '#252729'

largura_tela = Calculadora.winfo_screenwidth()
altura_tela = Calculadora.winfo_screenheight()

largura_janela = 335
altura_janela = 415

pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

Calculadora.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

conta = ''

InputArea = Frame(Calculadora, bg='#252729')
InputArea.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
lb_input = Label(InputArea, text='0', font='Arial 25 bold', bg='#252729', fg='white', anchor="e")
lb_input.pack(fill="both", expand=True)
BotoesArea = Frame(Calculadora, bg='#252729')
BotoesArea.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

def calculo(valores):
    global conta
    conta += valores
    lb_input.config(text=conta)

def resultado():
    global conta
    try:
        conta = str(eval(conta, {"_builtins_": None}, {}))
        lb_input.config(text=conta)
    except:
        lb_input.config(text="Erro")
        conta = ""

def limpar():
    global conta
    conta = ""
    lb_input.config(text="0")

def teclado(event):
    global conta
    tecla = event.char

    if tecla in '0123456789+-*/.%':
        calculo(tecla)
    elif tecla == '\r': 
        resultado()
    elif tecla == '\x08':
        conta = conta[:-1]
        lb_input.config(text=conta if conta else "0")

botoes = [
    ('C', 0, 0, limpar), ('/', 0, 1, lambda: calculo('/')), ('X', 0, 2, lambda: calculo('*')), ('%', 0, 3, lambda: calculo('/100')),
    ('7', 1, 0, lambda: calculo('7')), ('8', 1, 1, lambda: calculo('8')), ('9', 1, 2, lambda: calculo('9')), ('-', 1, 3, lambda: calculo('-')),
    ('4', 2, 0, lambda: calculo('4')), ('5', 2, 1, lambda: calculo('5')), ('6', 2, 2, lambda: calculo('6')), ('+', 2, 3, lambda: calculo('+')),
    ('1', 3, 0, lambda: calculo('1')), ('2', 3, 1, lambda: calculo('2')), ('3', 3, 2, lambda: calculo('3')), ('=', 3, 3, resultado),
    ('0', 4, 0, lambda: calculo('0')), ('.', 4, 1, lambda: calculo('.'))
]

for (text, row, col, cmd) in botoes:
    Button(BotoesArea, text=text, font="Arial 20 bold", command=cmd, bg='#000000', fg='white', width=3)\
    .grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(4):
    BotoesArea.columnconfigure(i, weight=2)

for i in range(5):
    BotoesArea.rowconfigure(i, weight=1)

Calculadora.bind("<Key>", teclado)

mainloop()