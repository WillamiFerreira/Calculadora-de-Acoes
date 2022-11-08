from PySimpleGUI import PySimpleGUI as sg
from classes import Janelas as jn
from tkinter import *
contador = 0
total_vendido = 0
total_investido = 0
impostoirrf = 0
quinze = 0
total_taxa_corretagem = 0
total_preco = 0
media_preco_acao = 0
codigos = []

def janela_codigos():
        sg.theme('lightgreen')
        headings = ['Código']
        layout = [
            [sg.Text('Códigos das empresas')],
        [sg.Table(values=codigos, 
                 headings=headings, 
                 max_col_width=50,
                 auto_size_columns=False,
                 display_row_numbers=False,
                 justification='center',
                 def_col_width=20,
                 alternating_row_color='lightgrey',
                 hide_vertical_scroll=True,
                 header_font='Bold, 10',
                 num_rows=5,
                 key='-TABLE-',
                 row_height=30)],
        [sg.Input(key='codigo_escolhido', size=(42, 10)), sg.Button('Go'), sg.Button('Voltar')],
        ]
        return sg.Window('Detalhes', layout=layout, finalize=True)

janela1, janela2, janela3 = jn.janela_home(), None, None

while True:
    window, eventos, valores = sg.read_all_windows()

    if window == janela1:
        data = valores['data']
        codigo = valores['codigo']
        quantidade = valores['quantidade']
        if valores['tipo'] == True:
            tipo = 'venda'
        else:
            tipo = 'compra'
        preco = valores['preco']
        taxa = valores['taxa']

    if eventos == sg.WIN_CLOSED or eventos == 'Close': 
        break

    if window == janela1 and eventos == 'Detalhar':
        janela1.hide()
        janela2 = janela_codigos()

    if window == janela1 and eventos == 'Salvar':
        if codigo not in codigos:
            codigos.append(codigo)


        arquivo = open(f'{codigo}.txt','a+')
        contador += 1  
        arq = open(f"{codigo}.txt")
        cont = arq.readlines()
        cont.append(f'Data: {data}, Código: {codigo}, Quantidade: {quantidade}, Tipo: {tipo}, Preço: {preco}, Taxa: {taxa}\n')#adiciona mais um elemento(linha) ao conteudo
        print(f'Transação {contador} salvada com sucesso!')
        arq = open(f'{codigo}.txt', 'w')
        arq.writelines(cont)
        arq.close()
        total_preco += float(preco)
    #método que calcula á média do preço das ações.

    if window == janela1 and eventos == "Média":
        media_preco_acao +=  float((total_preco)) / contador
        sg.popup('Média de Preço',f'A média de preço das ações é R${media_preco_acao:.2f}')

    if tipo == 'compra':
            total_investido += int(quantidade) * float(preco)
            total_taxa_corretagem += float(taxa)

    else:
        total_vendido += int(quantidade) * float(preco)
        impostoirrf += 0.005/100 * total_vendido #calculo do importo irrf
        total_taxa_corretagem += float(taxa)

    lucro = total_vendido - total_investido
    quinze = 15/100 * lucro #15% é retirado do lucro no final do mês

    #método para gerar IR
    if window == janela1 and eventos == 'Gerar IR':
        if total_vendido <= 20000:
            sg.popup('O total de vendas foi menos que R$20 mil, logo não é precisa pagar IR')
        else:
            #calculo do imposto de renda
            lucro_real = (lucro - quinze) - impostoirrf
            sg.popup(f'O valor do Imposto de Renda é de R${(lucro - lucro_real) - total_taxa_corretagem:.2f}')
       
    if window == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        window = janela1
        
    if window == janela2 and eventos == 'Go':
        file = valores['codigo_escolhido']
        if valores['codigo_escolhido'] not in codigos:
            sg.popup('Código não registrado')
        else:
            janela2.hide()
            janela3 = jn.janela_lista_acoes()
            file = open(f'{file}.txt')
            print(f'{file.readlines()}')

    if window == janela3 and eventos == 'Voltar':
        janela3.hide()
        janela2.un_hide()
        window = janela2

