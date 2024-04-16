# Lista de exercícios de Estrutura de Decisao

# link da lista: https://wiki.python.org.br/EstruturaDeDecisao

# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Como você se identifica? (m/f): ')

if sexo == 'm':
    print('M - Masculino')
elif sexo == 'f':
    print('F - Feminino')
else:
    print('Sexo inválido!')