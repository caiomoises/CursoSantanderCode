# Maior de idade
idade = int(input('informe sua idade: '))

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você não é maior de idade!')

# Aprovado ou reprovado
media = float(input('Informe a média do aluno: '))
faltas = int(input('Quantas faltas você tem: '))
presenca = (100*faltas) / 64

if media >= 7 and presenca > 75:
    print('Você foi aprovado!')
elif media >=5 and media < 7:
    print('Você foi para a 4ª prova!')
else:
    print('Você não foi aprovado!')


# While
numero_sorteado = 15

numero_escolhido = int(input('Escolha um número de 1 a 20: '))

while numero_sorteado != numero_escolhido:
    print('Você errou, tente novamente...')
    
    numero_escolhido = int(input('Escolha um número de 1 a 20: '))
print('Você acertou!')

#criando um contador
contador = 0

while contador <= 5:
    print(contador)
    contador += 1