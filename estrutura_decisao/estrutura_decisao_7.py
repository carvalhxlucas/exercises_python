# Lista de exercícios de Estrutura de Decisao

# link da lista: https://wiki.python.org.br/EstruturaDeDecisao

# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1 < num2 and num1 < num3:
    print(f'Entre os 3 números, o {num1} foi o menor inserido')
elif num2 < num1 and num2 < num3:
    print(f'Entre os 3 números, o {num2} foi o menor inserido')
elif num3 < num1 and num3 < num2:
    print(f'Entre os 3 números, o {num3} foi o menor inserido')