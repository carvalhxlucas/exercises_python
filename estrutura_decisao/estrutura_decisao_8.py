# Lista de exercícios de Estrutura de Decisao

# link da lista: https://wiki.python.org.br/EstruturaDeDecisao

# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

leite = float(input('Informe o valor do leite: '))
refrigerante = float(input('Informe o valor do refrigerante: '))
energetico = float(input('Informe o valor do energético: '))

if leite < refrigerante and leite < energetico:
    print(f'O valor do leite é de R${leite}, sendo o mais barato.')
elif refrigerante < leite and refrigerante < energetico:
    print(f'O valor do refrigerante é de R${refrigerante}, sendo o mais barato.')
elif energetico < leite and energetico < refrigerante:
    print(f'O valor do energético é de R${energetico}, sendo o mais barato.')