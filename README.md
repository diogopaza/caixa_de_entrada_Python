<h1>Introdução ao GUI Tkinter do Python</h1>
<h3>Neste artigo será criado uma janela com dois campos de entrada que serão somados e o
resultado será exibido na própria janela.</h3>
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
<p>O módulo Tkinter oferece trê formas de trabalhar com geometria e posicionamento:</p>
<ul>
	<li>Pack</li>
	<li>Grid</li>
	<li>Place</li>
</ul>
<h4>Eventt handler</h4>
<p>Os event handler são ações que são executadas como resposta a determinado evento. Sempre que um evento ocorre, o event loop
interpreta como uma string. Exemplo: o botão ENTER é representado pela string "<Return>"</p>


<h6>Exemplo prático</h6>

//importando a biblioteca tkinter<br>
from tkinter import *<br>


janela = Tk()<br> instanciando a classe Tk pela variável janela

//cria metodo <br>
def bt_click():<br>
    print("bt_click")<br>
    if( str( ed1.get() ).isnumeric() and str( ed2.get() ).isnumeric()  ):<br>
        num1 = int(ed1.get())<br>
        num2 = int(ed2.get())<br>
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

<h2>Exemplo 2, importação e criação simnples de janela com o Tkinter </h2>

import tkinter as tk == importa a biblioteca gráfica<br>

root = tkinter.Tk()<br>

root.mainloop()<br>

<h2>Criando uma aplicação com Banco de Dados</h2>
<p>Será usado o módulo DBI( DataBase Interface ) que usa uma API( Application Programming Interface ) para se comunicar com o banco de dados</p>
<p>O banco de dados usado será o SQLite, que já vem incorporado ao módulo DBI. 
</p>
<p>O SQLite cria um arquivo com extensão .db em disco, contendo todas as tabelas da aplicação.</p>
<h4>Estrutura da aplicação</h4>
<ul>
	<li>App.py == terá os containers da interface e executará a aplicação</li>
	<li>Usuarios.py == Classe de modelo para o Usuário</li>
	<li>Banco.py == Classe de banco de dados</li>
</ul>