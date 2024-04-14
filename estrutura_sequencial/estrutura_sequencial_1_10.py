# Lista de exercicios de Estrutura Sequencial - Exercícios do 1 ao 10

# link da lista: https://wiki.python.org.br/EstruturaSequencial

# 1 - Faca um Programa que mostre a mensagem "Alo mundo" na tela.
print('Hello World!')

# 2 - Faca um Programa que peca um numero e entao mostre a mensagem O numero informado foi [numero].
numero = input('Informe um número:')
print(numero)

# 3 - Faca um Programa que peca dois numeros e imprima a soma.
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

total = num1 + num2

print('A soma dos dois números resulta em: ',total)

# 4 - Faca um Programa que peca as 4 notas bimestrais e mostre a media.
nota1 = float(input('Informe a nota do primeiro bimestre: '))
nota2 = float(input('Informe a nota do segundo bimestre: '))
nota3 = float(input('Informe a nota do terceiro bimestre: '))
nota4 = float(input('Informe a nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('Sua média é de: ', media)

# 5 - Faca um Programa que converta metros para centimetros.
metros = int(input('Informe a medida em metros'))

centimetros = metros * 100

print('Conversão para centimetros: ', centimetros)

# 6 - Faca um Programa que peca o raio de um circulo, calcule e mostre sua area.
raio = float(input('Informe o raio do círculo: '))

areaCirculo = 3.14 * (raio * raio)

print('A área total do círculo é de: ', area)

# 7 - Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.
base = float(input('Informe a medida da base do quadrado: '))
altura = float(input('Informe a medida da altura do quadrado: '))

areaQuadrado = base * altura

print('A área do quadrado é de: ', areaQuadrado)

# 8 - Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes.
valorHora = float(input('Quanto você ganha por hora: '))
quantidadeHoras = int(input('Quantas horas você trabalha por semana: '))

salario = (valorHora * quantidadeHoras) * 4

print('O seu salário é de: ', salario)

# 9 -Faca um Programa que peca a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
grausF = float(input('Informe os graus em Fahrenheit: '))

grausC = 5 * ((grausF - 32) / 9)

print('A temperatura em Celsius é: ', grausC)

# 10 - Faca um Programa que peca a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
grausCelsius = float(input('Informe a temperatura em graus Celsius: '))

grausFahrenheit = (grausCelsius * 1.8) + 32

print('A temperatura em Fahrenheit é de: ', grausFahrenheit)