import os

os.system('clear')
# Criando dicionarios

dicionario = {} # criando um dicionario vazio
dicionario = dict()

dicionario = {'nome': 'Caio', 'idade': 26, 'altura': 1.76} # Cria uma chave de acesso

# Acessando dados do dicionario

print(dicionario)
print(dicionario['nome'])

# Adicionando elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

# Editando uma chave

dicionario['altura'] = 1.78

print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave,':' ,dicionario[chave])

# Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)