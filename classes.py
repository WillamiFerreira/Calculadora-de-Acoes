from PySimpleGUI import PySimpleGUI as sg
from tkinter import *

class Janelas():
    def janela_home():
        sg.theme('lightgreen')
        menu_def=['&Tools', ['&Detalhar','&Média','&Close',]],['&Save',['&Save File', 'Save &As','Save &Copy'  ]]
        layout = [
            [sg.Menu(menu_def, background_color='darkgrey',text_color='black', disabled_text_color='yellow', font='Verdana', pad=(10,10))],
            [sg.Text('Data:  '), sg.Text(), sg.Text(), sg.Input(key='data', size=(28))],
            [sg.Text('Código:      '), sg.Input(key='codigo', size=(28))],
            [sg.Text('Quantidade:'), sg.Input(key='quantidade', size=(28))],
            [sg.Text('Tipo:'), sg.Radio('Compra', "Radio01", default=False), sg.Radio('Venda', "Radio01", default=True, key='tipo')],
            [sg.Text('Preço:'), sg.Input(key='preco', size=(32))],
            [sg.Text('Taxa: '), sg.Input(key='taxa', size=(32)) ],
            [sg.Text()],
            [sg.Output(size=(40, 10))],#Output me permite mostrar as coisa na tela,
            [sg.Button('Salvar'), sg.Button('Gerar IR')],
        ]
        return sg.Window('Calculadora de IR', layout=layout, finalize=True)

    def janela_codigos():
        sg.theme('lightgreen')
        layout = [
            [sg.Text('Códigos das empresas')],
            [sg.Output(size=(40, 10))],
            [sg.Input(key='codigo_escolhido', size=(42, 10)), sg.Button('Go'), sg.Button('Voltar')],
        ]
        return sg.Window('Detalhes', layout=layout, finalize=True)

    def janela_lista_acoes():
        sg.theme('lightgreen')
        layout = [
            [sg.Output(size=(83, 10))],
            [sg.Button('Voltar')]
        ]
        return sg.Window('Detalhes da empresa escolhida', layout=layout, finalize=True)