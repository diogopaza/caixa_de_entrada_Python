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

<h6>Exemplo prático</h6>

//importando a biblioteca tkinter<br>
from tkinter import *<br>


janela = Tk()<br>

//cria metodo <br>
def bt_click():<br>
    print("bt_click")<br>
    if( str( ed1.get() ).isnumeric() and str( ed2.get() ).isnumeric()  ):<br>
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 + num2<br>
    else:<br>
        lb["text"] = "Valores informados inválidos"<br>

ed1 = Entry(janela)<br>
ed1.place(x=100, y=100)<br>
ed2 = Entry(janela)<br>
ed2.place(x=100, y=130)<br>

bt = Button(janela, text="soma",width=20, command= bt_click )<br>
bt.place( x=100,y=150)<br>

lb = Label(janela, text="Label1")<br>
lb.place(x=100, y=200)<br>


janela.geometry("400x300+500+200")<br>

janela.mainloop<br>

