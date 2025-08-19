'''
sala1 = "vingadores"
min1= 14
sala2 = "avatar"
min2 = 14
sala3 = "batman"
min3 = 16
sala4 = "super man"
min4 = 18
sala5 = "homem aranha"
min5 = 16

while True:
    print(30*'-','cineClub',30*'-')
    print('Escolha uma opção de Filme que deseja assistir!')
    print(f'1. Sala 01 - {sala1} idade minima {min1}')
    print(f'2. Sala 02 - {sala2} idade minima {min2}')
    print(f'3. Sala 03 - {sala3} idade minima {min3}')
    print(f'4. Sala 04 - {sala4} idade minima {min4}')
    print(f'5. Sala 05 - {sala5} idade minima {min5}')
    print(f'6. Sair')

    opcao = int(input('Digite a opção desejada:'))
    idade= input('Digite sua idade:')

    if opcao == 1:
        if idade >= min1:
            print(f'Bem vindo ao CineClub')
            print('ingresso para: {sala1}')
            print(f'Sala: 01')
            break
        else:
            print('você nao tem idade para assistir o filme!')
            
    elif opcao == 2:
        if idade >= min2:
            print(f'Bem vindo ao CineClub')
            print('ingresso para: {sala2}')
            print(f'Sala: 02')
            break
        else:
            print('você nao tem idade para assistir o filme!')

    elif opcao == 3:
        if idade >= min3:
            print(f'Bem vindo ao CineClub')
            print('ingresso para: {sala3}')
            print(f'Sala: 03')
            break
        else:
            print('você nao tem idade para assistir o filme!')
    elif opcao == 4:
        if idade >= min4:
            print(f'Bem vindo ao CineClub')
            print('ingresso para: {sala4}')
            print(f'Sala: 04')
            break
        else:
            print('você nao tem idade para assistir o filme!')
    elif opcao == 5:
        if idade >= min5:
            print(f'Bem vindo ao CineClub')
            print('ingresso para: {sala5}')
            print(f'Sala: 05')
            break
        else:
            print('você nao tem idade para assistir o filme!')
    elif opcao == 6:
        print('Saindo do sistema')
        break
    else:
        print('Opção inválida!')

'''
'''
nome_lista = ['fulano, cicrano', 'Beltrano', 'joana', 'maria', 'mariana']
nome = input('informe o nome que deseja encontrar: ')

indice = nome_lista.index(nome)

try:
    print(f'{nome} encontrado no indice {indice}')
except:
    print(f'{nome} nao encontrado.')
#busca o nome desejado
if nome in nome_lista:
    print(nome)
else:
    print(f'{nome} nao encontrado.')
'''
'''
nome_lista = ['fulano', 'cicrano', 'Beltrano', 'joana', 'maria', 'mariana']
nome = input('informe o nome que deseja encontrar: ')

quantidade = nome_lista.count(nome)

try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except:
    print(f'{nome} nao encontrado.')
#busca o nome desejado
if nome in nome_lista:
    print(nome)
else:
    print(f'{nome} nao encontrado.')
'''
'''
nome_lista = ['fulano', 'cicrano', 'Beltrano', 'joana', 'maria', 'mariana']
nome_a_alterar = input('informe o nome que deseja encontrar: ')
nome_lista[nome_lista.index(nome_a_alterar)] = input('informe o novo nome:')

for nome in nome_lista:
    print(nome)

'''
'''
#tabuada
numero = int(input('Digite o numero:'))

for i in range(1,11):
    resultado = numero*i
    print(f'{i} X {numero} = {resultado}') 
'''
'''
#começando a aula

#importando bibliotecas (lib)
import os
from time import sleep

cont = input('Digite um numero inteiro:')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f"Contagem regressiva: {cont_int}...")
        sleep(1)
        cont_int -= 1
        os.system('cls')

except:
    print('Digite um numero valido!')

print("fim da contagem!")
'''
'''programa: Sorteio V.1.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio

'''
'''
#importando bibliotecas(lib)
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
nome5 = input('Digite o quinto nome: ')

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)
'''


'''
programa: Sorteio V.2.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio

'''
'''
#importando bibliotecas(lib)

import random

lista = []

sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair:')
    if nome_candidato != '':
        #append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else:
        sair = True
escolhido = random.choice(lista)

print("escolhido foi : ", escolhido)
'''






'''
programa: Sorteio V.3.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio

'''
'''
#importando lib
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio:')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes:
        os.system('cls')
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)
        # exclui o sorteado da lista original
        
       
        pop -função, remove pelo indice
            pop() - remover o ultimo indice
            pop(0) - remove o indice 0
        del - instrução, remover item pelo indice, mais de um item
            del[escolhido]
        remove - remove a partir de uma variavel
            lista.remove(variavel)
        '''
'''
        print(f'O escolhido foi : {escolhido}')

        lista_nomes.remove(escolhido)


        opcao = input('Deseja sortear outro nome ? S-sim \n| N-não\n:').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Nao ha nomes para serem sorteados!')
        break
print('Programa finalizado!')
print(f'os sorteados foram {lista_sorteados}')

'''
'''
programa: advinhação V.1.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio

'''
'''
#importando lib
from random import randint

print('Tente advinhar o numero!')
num1 = int(input('Digite um numero:'))

num_secreto = randint(1,2)

if num1 == num_secreto:
    print('Parabens, voce ganhou!!!!!')
else:
    print('voce perdeu lerdao')
    print(f'O numero correto é {num_secreto}')
'''
'''
#importando lib
import random
import os
import time

numero_secreto= random.randint(1,100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-', 'Bem vindo ao Inferno mental',30*'-')
print(f'voce tem {max_tentativas} tentativas para adivinhar o numero secreto')
print(' vamos começar?')

while tentativas < max_tentativas:
    try:
        #entrada do usuario
        palpite = int(input('Digite o seu palpite: '))
    
    except ValueError:
        print('Por favor, digite um numero valido.')
        continue

    tentativas += 1

    #verificar palpite
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('tente um numero maior!')
        time.sleep(3)
        os.system('cls')
    else:
        print('Tente um numero menor!')
        time.sleep(3)
        os.system('cls')


if acertou:
    print(f'Parabens voce ganhou!! Voce acertou o numero {numero_secreto} em {tentativas} tentativas')
else:
    print(f'Que pena!! voce nao conseguiu adivinhar o numero secreto{numero_secreto}')

'''
