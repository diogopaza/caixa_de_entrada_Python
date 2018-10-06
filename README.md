<h1>Introdução ao GUI Tkinter do Python</h1>
<h3>Neste artigo será criado uma janela com dois campos de entrada que serão somados e o
resultado será exibido </h3>
<h3>Oque é Tkinter</h3>
<p>Tkinter é uma biblioteca da linguagem Python que acompanha a instalção padrão e permite desdenvolver interfaces gráficas. Isso significa que qualquer computador que tenha o interpretador Python instalado é capaz de criar interfaces gráficas usando o Tkinter.</p>
<h4>Conceitos de GUI( Graphic User Interface)</h4>
<ul>
	<li><strong>Container:</strong> É uma analogia a um container físico e tem como objetivo
	organizar e guardar objetos. Ele serve para organizar os widgets, que são os componentes da
	 interface gráfica do usuário, como os botões, menus, ícones entre outros. </li>
	 <li><strong>Event Handler:</strong> São tratadores de eventos. por exemplo ao clicarmos em um botão
	 para executar uma ação, uma rotina é executada. Essa rotina é chamada de event handler</li>
	 <li><strong>Event Loop:</strong> O event loop verifica constantemente se outro evento foi acionado. 
	 Caso a hipótese seja verdadeira, ele irá executar a rotina correspondende</li>
</ul>

<h6>Exemplo comentado</h6>
from tkinter import *

janela = Tk()

def bt_click():
    print("bt_click")
    if( str( ed1.get() ).isnumeric() and str( ed2.get() ).isnumeric()  ):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 + num2
    else:
        lb["text"] = "Valores informados inválidos"

ed1 = Entry(janela)
ed1.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, text="soma",width=20, command= bt_click )
bt.place( x=100,y=150)

lb = Label(janela, text="Label1")
lb.place(x=100, y=200)


janela.geometry("400x300+500+200")

janela.mainloop

