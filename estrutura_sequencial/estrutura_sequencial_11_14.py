# List de exercícios de Estrutura Sequencial - Exercícios do 11 ao 14

# link da lista: https://wiki.python.org.br/EstruturaSequencial

# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#      a) o produto do dobro do primeiro com metade do segundo .
#      b) a soma do triplo do primeiro com o terceiro.
#      c) o terceiro elevado ao cubo.
num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe mais um número inteiro: '))
num3 = float(input('Informe um número real: '))

# resposta a
calculoA = (num1 * 2) + (num2 / 2)
# resposta b
calculoB = (num1 * 3) + num3
# resposta c
calculoC = num3 ** 3
# -------------------------------------------------

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe a sua altura: '))

pesoIdeal = (72.7 * altura) - 58

print('O seu peso ideal é: ', pesoIdeal)
# -------------------------------------------------

# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#      a) Para homens: (72.7*h) - 58
#      b) Para mulheres: (62.1*h) - 44.7
genero = input('Informe o seu gênero de acordo com as alternativas: \nA - Feminino \nB - Masculino\nR: ')

# verifica se o genero é feminino
if (genero == 'A') :
    alturaMulher = float(input('Informe a sua altura: '))
    pesoIdealFeminino = (61.1 * alturaMulher) - 44.7

    print('O seu peso ideal é de: ', pesoIdealFeminino)

# verifica se o genero é masculino
elif (genero == 'B') :
    alturaHomem = float(input('Informe a sua altura: '))
    pesoIdealMasculino = (72.7 * alturaHomem) - 58

    print('O seu peso ideal é de: ',pesoIdealMasculino)

# opção inválida
else :
    print('Opção inválida!')
# -------------------------------------------------

# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
print(' ---- Bem-vindo ao Controlador de Peixe do Seu João ---- \n ------------------------------------------------------- ')
pesoPeixe = float(input('Informe quantos kg de peixe você está levando: '))
limite = 50

#armazena o valor do excesso de peixe
excesso =  pesoPeixe - limite

# calcula a multa por excesso de peixe
multa = excesso * 4

# verifica se deve pagar multa
if (excesso > 0):
    print('Você excedeu o limite! Pague a multa no valor de: R$',multa)
else: 
    print('Peso dentro do permitido, liberado!')