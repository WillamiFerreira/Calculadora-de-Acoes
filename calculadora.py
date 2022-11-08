from PySimpleGUI import PySimpleGUI as sg
from classes import Janelas as jn
from tkinter import *
#janela-inicio. Da linha 3 a 12 está o código responsável pela criação da interface gráfica

#Essas variáveis armazenam dados das operações que serão usados no calculo do IR.
contador = 0
total_vendido = 0
total_investido = 0
impostoirrf = 0
quinze = 0
total_taxa_corretagem = 0
total_preco = 0
media_preco_acao = 0
codigos = []

janela1, janela2, janela3 = jn.janela_home(), None, None

while True:
    window, eventos, valores = sg.read_all_windows()
    #em cada linha  da 27 a 36 é lida da interface gráfica o dado digitado e armazenado em uma variável.
    if window == janela1:
        #variáveis que armazenarão os dados
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
        janela2 = jn.janela_codigos()
        for cod in codigos:
            print(cod)

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
            print('O total de vendas foi menos que R$20 mil, logo não é precisa pagar IR')
        else:
            #calculo do imposto de renda
            lucro_real = (lucro - quinze) - impostoirrf
            print(f'O valor do Imposto de Renda é de R${(lucro - lucro_real) - total_taxa_corretagem:.2f}')
       
    if window == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        window = janela1
        
    if window == janela2 and eventos == 'Go':#quando o botão Go for precionado...
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

