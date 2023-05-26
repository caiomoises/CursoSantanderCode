nome = input('Insira seu nome: ')
hora = int(input('insira que horas é: '))

if hora >= 0 and hora < 12:
    print(f'Bom dia, {nome}')
elif hora >= 12 and hora < 18:
    print(f'Boa tarde, {nome}')
elif hora >= 18 and hora < 0:
    print(f'Boa noite, {nome}')
else:
    print(f'{nome}, você inseriu uma hora invalida!')