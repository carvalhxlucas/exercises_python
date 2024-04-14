# List de exercícios de Estrutura Sequencial - Exercício 15

# link da lista: https://wiki.python.org.br/EstruturaSequencial

# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#      a) salário bruto.
#      b) quanto pagou ao INSS.
#      c) quanto pagou ao sindicato.
#      d) o salário líquido.
#      e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#           + Salário Bruto : R$
#           - IR (11%) : R$
#           - INSS (8%) : R$
#           - Sindicato ( 5%) : R$
#           = Salário Liquido : R$

print('--- GERADOR DE DEMONSTRATIVO DE SALÁRIO --- \n --------------------------------------')

valorHora = float(input('Informe o valor da sua hora trabalhada: '))
quantidadeHora = float(input('Informe a quantidade de horas que você trabalha no mês: '))

salarioBruto = quantidadeHora * valorHora
impostoRenda = (salarioBruto / 100) * 11
inss = (salarioBruto / 100) * 8
sindicato = (salarioBruto / 100) * 5

descontos = impostoRenda + inss + sindicato

salarioLiquido = salarioBruto - descontos

print('---------------------------\n------ DEMONSTRATIVO ------ \n---------------------------\n')
print('Valor bruto: R$',salarioBruto,'\nIR: R$',impostoRenda,'\nINSS: R$',inss,'\nSindicato: R$',sindicato,'\nSalário Liquido: R$',salarioLiquido, '\n---------------------------')