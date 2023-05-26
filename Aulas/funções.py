# Funções

# 1. O que são funções e porque utilizá-las?

# Funções que ja utilizamos anteriormente:
""" print()
input()
len()
max()
min() """

# 2. Criação de funções 

# Função inicial

def saudacao():
    print('Seja bem vinda(o)!')

saudacao()


# Função com parâmetros

def saudacao(nome):
    print(f'Seja bem vinda(o) {nome}!')

nome = input('Qual o seu nome? ')
saudacao(nome)

# Função com arâmetro default

def saudacao(nome='Caio', idade = '26'):
    print(f'Seja bem vinda(o) {nome}, você tem {idade} anos de idade!')

saudacao(nome)

# Função com return

def soma(x, y, opera = '+'):
    if opera == '+':
        return x+y
    elif opera == '-':
        return x-y
    elif opera == '*':
        return x*y
    elif opera == '/':
        return x/y

x = int(input('Insira o valor de X: '))
y = int(input('Insira o valor de Y: '))

resultado = soma(x, y)

print(f'O resultado da soma é: {resultado}')