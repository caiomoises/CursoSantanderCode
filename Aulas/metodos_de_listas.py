# Metodos de listas

# Metodos para adicionar elementos

lista = [1, 3, 12, 8, 2]

# append -> Adiciona um elemento no fim da lista

print('Lista original', lista, 'Possui:', len(lista), 'elementos')

lista.append(3) 

print('Depois do append:', lista, 'Possui:', len(lista), 'elementos')

# insert -> Adiciona um elemento em qualquer posição da lista

lista.insert(2, 10) # 2 é o indice onde vou adicionar o 10

print('Depois do insert:', lista, 'Possui:', len(lista), 'elementos')

# extend -> Junta duas listas

lista2 = [1, 2, 3]
print('Lista 2:', lista2)

lista.extend(lista2) # Pega os elementos da lista 2 e adiciona no final da lista 

print('Depois do extend:', lista, 'Possui:', len(lista), 'elementos')

#Metodos para remover elementos

# pop -> remove valores atraves do indice

lista.pop() # Elimina o ultimo valor do pop
lista.pop(0) # Elimina o valor que esta no indice 0 
print('Depois do pop', lista, 'Possui:', len(lista), 'elementos')

# remove -> Você diz qual valor quer retirar

lista.remove(3) # Irá remover o valor tres da lista

print('Depois do remove:', lista, 'Possui:', len(lista), 'elementos')

# count -> diz quantas vezes um elemento aparece na lista

print('Quantidade de 2 na lista:', lista.count(2))

# index -> Diz o indice de um determinado elemento na llista

print('Indice do elemento 12:', lista.index(12))

# sort - serve para ordenar a lista

lista.sort()
print('Lista ordenada em ordem crescente:', lista)

lista.sort(reverse=True)
print('Lista ordenada em ordem decrescente:', lista)

# FUNÇÕES PARA LISTAS

# len -> para saber quantos elementos tem na lista

print('A lista possui:', len(lista), 'elementos')

# sum -> soma dos elementos da lista

print('A soma dos valores da lista é:', sum(lista))

# max -> para saber o elemento de maior valor na lista

print('O maior valor da lista é:', max(lista))

# min -> para saber o elemento de menor valor na lista

print('O menor valor da lista é:', min(lista))