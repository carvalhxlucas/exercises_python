# List de exercícios de Estrutura Sequencial - Exercício 16

# link da lista: https://wiki.python.org.br/EstruturaSequencial

# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaPintada = float(input('Informe a área a ser pintada, em metros quadrados: '))
quantidadeLatas = (areaPintada / 3) / 18
valorTotal = quantidadeLatas * 80

print('Quantidade de latas necessárias: ',quantidadeLatas)
print('Valor total a pagar: ',valorTotal)
