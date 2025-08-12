# concatenação
# quebra de linha
# formatando decimais
# alterando virgula e ponto
# if else
# operador ternario

#FIXME - concatenação com +

nome = "leleo"
idade = 16
altura = 1.94

# saida de dados
print('Olá meu nome é,' + nome + ',tenho' +str(idade) + 'anos de idade')

#FIXME - concatenação com ,
print('Olá, meu nome é,', nome,'tenho', idade, 'anos de idade')

#FIXME - concatenação com format
print('Olá, meu nome é, {}, tenho {} anos de idade'.format(nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {type(nome)} e tenho {idade+1} anos de idade')

'''
# eliminando quebra de linha
print('O sábio sabia ', end='')
print('que sabiá sabia assobiar.')


valor = 1.23456789

# exibindo o valor com duas casas depois da virgula
print(f'{valor:,.2f}')

print(50*'=')
peso = input('digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}'.replace('.',','))

#Variaveis

numero_inteiro = 10
numero_decimal = 3.14
texto = 'Olá mundo !'
verdadeiro_ou_falso = True
'''
'''
#prints na tela

print('int:', numero_inteiro)
print('float:', numero_decimal)
print('str:', texto)
print('bool:', verdadeiro_ou_falso)

'''
'''
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade: '))

print('Antes do if')
if idade >= 18:
    print('você é maior de idade!')
    print('você esta dentro do bloco IF')
else:
    print('você é menor de idade!')
    print('você está dentro do bloco ELSE')
print('Você está fora da estrutura condicional if else')

num1 = 10

if num1 %2 ==0:
    print('numero par')
else:
    print('numero impar')
'''
'''
print(40*'-',  'BOLETIM ESCOLAR', 40*'-')

nome_aluno = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 =float(input('Digite a terceira nota:'))
nota4 =float(input('Digite a quarta nota:'))

media = (nota1 + nota2 + nota3 + nota4)/4

# >= 7: aprovado
# >= 5: recuperação
# reprovado

if media >=7:
    print(f'{nome_aluno}!!!ALUNO APROVADO!')
    print(f'Nota1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3:{nota3} | nota 4 {nota4}')
    print(20*'=')
    print(f'Média: {media}')

elif media >=5:
    print(f'{nome_aluno}!!!ALUNO DE RECUPERAÇÃO!')
    print(f'Nota1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3:{nota3} | nota 4 {nota4}')
    print(20*'=')
    print(f'Média: {media}')

else:
    print(f'{nome_aluno}!!!ALUNO REPROVADO!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3:{nota3} | nota 4 {nota4}')
    print(20*'=')
    print(f'Média: {media}')
'''
print(40*'-',  'MONTANHA-RUSSA', 40*'-')
#variaveis
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))

# verifica se o usuario possui os requisitos minimos
if idade >= 12 and altura >= 1.6:
    print(f'A entrada de {nome} está autorizada.')
else:
    print(f'A entrada de {nome} não está autorizada')


#variaveis
nome = 'Alex'
idade = 39

#operador ternário
print(nome, 'é maior de idade.'if idade >=18 else 'é menor de idade.')














'''
parte do vitor:
input_name = input('qual o seu nome?: ')
print('seja bem vindo ao sistema python', input_name)

parte do leleo:#Variaveis

numero_inteiro = 10
numero_decimal = 3.14
texto = 'Olá mundo !'
verdadeiro_ou_falso = True

#prints na tela

print('int:', numero_inteiro)
print('float:', numero_decimal)
print('str:', texto)
print('bool:', verdadeiro_ou_falso)

parte da Gabi

soma = 12 + 7
print("o resultado da soma é: ", soma)

div = 15 % 4
print("o resto da divisão é: ",div)

mult = 3**4 
print("o resultado da multiplicação é: ", mult)

parte do humberto:
numerostr = str(20)
adicional = 4
numero_float = int(numerostr)
soma = (numero_float + adicional)
print(soma)
'''


