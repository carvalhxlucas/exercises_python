# Lista de exercícios de Estrutura de Decisao

# link da lista: https://wiki.python.org.br/EstruturaDeDecisao

# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a','e','i','o','u','A','E','I','O','U']

letra = input('Digite uma letra: ')

if letra in vogais:
    print('É uma vogal')
else:
    print('É uma consoante')
