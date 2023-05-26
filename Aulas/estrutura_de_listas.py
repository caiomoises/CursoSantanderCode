# Estrutura de listas

# Antes
nota1 = 7.9
nota2 = 9.5
nota3 = 8.5

# Com lista
notas = [7.9, 9.5, 8.5]

# Criando listas
lista = [] #lista vazia
lista = list() #lista vazia
lista = [26, 'Caio Moisés', 3.141519, True]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)
lista = [26, 'Caio Moisés', 3.141519, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # Começa no indice 0 e vai ate o < 3
print(lista[3:6]) # Comeca no indice 3 e vai ate o < 6
print(lista[3:]) # Começa no indice 3 e vai ate o final da lista
print(lista[2:6:2]) # Começa no 2 vai ate o < 6 e pula de 2 em 2

# Iterações com for
# 1. Utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os indices 

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])