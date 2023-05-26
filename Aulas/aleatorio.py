import os
pessoa1 = 50
pessoa2 = 0
pessoa3 = 0


print(f'A pessoa 1 possui: R${pessoa1}')
print(f'A pessoa 2 possui: R${pessoa2}')
print(f'A pessoa 3 possui: R${pessoa3}')
print('')
print(f'Pessoa 1, você esta devendo R${pessoa1} a pessoa 2')
print('')
pagar = input('Deseja pagar: digite SIM ou NAO - ')
os.system('clear')

if pagar == 'SIM':
    pessoa1 = 0
    pessoa2 = 50
    print(f'Você pagou R${pessoa2} a pessoa 2')
    print('Atualização...')
    print(f'A pessoa 1 possui: R${pessoa1}')
    print(f'A pessoa 2 possui: R${pessoa2}')
    print(f'A pessoa 3 possui: R${pessoa3}')
    print('\n')
    print(f'Pessoa 2, você esta devendo R${pessoa2} a pessoa 3')
    pagar = input('Deseja pagar: digite SIM ou NAO - ')
    os.system('clear')
    if pagar == 'SIM':
        pessoa2 = 0
        pessoa3 = 50
        print(f'Você pagou R${pessoa3} a pessoa 3')
        print('Atualização...')
        print(f'A pessoa 1 possui: R${pessoa1}')
        print(f'A pessoa 2 possui: R${pessoa2}')
        print(f'A pessoa 3 possui: R${pessoa3}')
        print('\n')
        print(f'Pessoa 3, você esta devendo R${pessoa3} a pessoa 1')
        pagar = input('Deseja pagar: digite SIM ou NAO - ')
        os.system('clear')
        if pagar == 'SIM':
            pessoa3 = 0
            pessoa1 = 50
            print(f'Você pagou R${pessoa1} a pessoa 1')
            print('Atualização...')
            print(f'A pessoa 1 possui: R${pessoa1}')
            print(f'A pessoa 2 possui: R${pessoa2}')
            print(f'A pessoa 3 possui: R${pessoa3}')
            print('\n')
            print(f'Ninguém está devendo nada a ninguém! \nPessoa 1 ficou com os mesmo R${pessoa1} do inicio')
        else:
            print('Você decidiu não pagar, então continua devendo')
    else:
        print('Você decidiu não pagar, então continua devendo')
else:
    print('Você decidiu não pagar, então continua devendo')