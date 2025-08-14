
'''
nome = 'leleo'
idade = 16

print(f'o meu nome é{nome} {type(nome)} tenho {idade} anos de idade{idade}')











else: #se nao for verdadeiro
    print('abaixo de ')






    print('acima de 90 kilos.')
else:
    print('abaixo do peso')
'''

'''
   Probelma; crie um sistema que calcule o indice de massa corporal (IMC)
   do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
   no peso ideal ou se precisa emagrecer ou engordar mais. Ultilize a tabela
   do IMC para definir os valores.

   imc= peso / (altura * altura)

   18,5

'''













'''
obesidade grau III
'''
'''
print(20*'-', 'CALCULADORA DE IMC',40*'-')

while True:

    altura = float(input('Digite sua altura: ').replace(',','.'))
    peso = float(input('Digite seu peso:').replace(',','.'))

    imc = peso / (altura * altura)
    print()
    print(f'seu IMC é: {imc:.2f}')
    if imc <= 18.5:
        print('Abaixo do normal')
    elif imc <= 24.9:
        print('Normal')
    elif imc <= 29.9:
        print('sobrepeso')
    elif imc <= 34.9:
        print('obesidade grau I')
    elif imc <= 39.9:
        print('obesidade grau II')
    else:
        print('obesidade grau III')

    opcao = input('deseja calcular novamente ? S - Sim | N - Não').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do sistema!')
        break
    else:
        print('opcao invalida')
        break
    '''
    
    



'''
Probelma 2: um elevador de carga possui capacidade para 200kg. Crie 
um programa que receba do usuario seu peso e o peso de carga e verifica se a carga 
está autorizada a usar o elevador ou não.

'''
'''
limite = 200

peso_usuario= float(input('Digite o seu peso:').replace(',','.'))
carga = float(input('Digite o peso da carga:').replace(',','.'))

if(peso_usuario + carga) >= limite:
   print('nao autorizado.')
else:
    print('autorizado.')
'''
'''
nome = input('Digite seu nome:')
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu telefone:')
anonasc = int(input('Digite sua data de Nascimento'))
print(80*'=')

while True:
    #menu principal
    print(40*'-','Sistema console 2° DS',40*'-')
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opcao = input('Digite uma opção:')

    if opcao == '1':
        altura = float(input('Digite sua altura: ').replace(',','.'))
        peso = float(input('Digite seu peso:').replace(',','.'))

        imc = peso / (altura * altura)
        print()
        print(f'seu IMC é: {imc:.2f}')
        if imc <= 18.5:
            print('Abaixo do normal')
        elif imc <= 24.9:
            print('Normal')
        elif imc <= 29.9:
            print('sobrepeso')
        elif imc <= 34.9:
            print('obesidade grau I')
        elif imc <= 39.9:
            print('obesidade grau II')
        else:
            print('obesidade grau III')
    elif opcao == '2':
        ano_atual = 2025
        idade = ano_atual - anonasc
        print(nome, 'é maior de idade.'if idade >= 18 else 'é menor de idade.')
    elif opcao == '3':
        while True:
            print('Calculadora')
            print('1 - soma')
            print('2 - divisão')
            print('3 - subtração')
            print('4 - multiplicação')
            print('5 - sair')
            opcao_calculo = input('escolha uma operação de matemática:')

            num1 = float(input('Digite o primeiro número:'))
            num2 = float(input('Digite o segundo número:'))

            if opcao_calculo == '1':
                print (f'Resultado da soma é: {num1 + num2}')
            elif opcao_calculo =='2':
                print(f'Resultado da divisão é: {num1/num2}')
            elif opcao_calculo == "3":
                print (f'Resultado da subtração é: {num1 - num2}')
            elif opcao_calculo == '4':
                print(f'Resultado da multiplicação é:{num1 * num2}')
            elif opcao_calculo == '5':
                break
            else:
                print("Opção Inválida")
    elif opcao == '4':
        print(50*'_')
        print(f'Nome:{nome} | Telefone: {telefone}    |')
        print(f'CPF: {cpf} | Data de Nascimento {dt_nascimento}   |')
        print(50*'-')
    elif opcao == '5':
        linhas = 15
        j = 1

        while j<= linhas:
            espacos = linhas - j
            estrelas = 2*j-1

            print(' '* espacos + '*' *estrelas)
            j +=1      
    elif opcao == '6':
        print('saindo do sistema!')
        break
    else:
        print('opcao invalida!')

'''

nome = 'leozada'

for i in nome:
    print(i)