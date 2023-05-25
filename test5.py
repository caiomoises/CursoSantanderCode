# for

for i in range(10): # Vai de 0 ate menor que 10
    print(i)

for i in range(1, 11): # Vai de 1 ate menor que 11
    print(i) 
    
for i in range(1, 11, 2): # Vai de 1 ate menor que 11 pulando de 2 em 2
    print(i)

# Média
soma = 0
for i in range(3):
    nota = float(input(f'Insira sua {i+1}ª nota: '))
    soma = soma + nota

media = soma / 3
print('Sua média é: ', media)