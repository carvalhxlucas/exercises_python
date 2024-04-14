# List de exercícios de Estrutura Sequencial - Exercício 18

# link da lista: https://wiki.python.org.br/EstruturaSequencial

''' 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanhoArquivo = float(input('Informe o tamanho do arquivo que deseja baixar: '))
velocidadeInternet = int(input('Informe a velocidade da sua conexão em Mbps: '))

tempoEstimado = (tamanhoArquivo / (velocidadeInternet / 8)) / 60


print('Tempo estimado para a conclusão do download: ', tempoEstimado,' minutos.')
