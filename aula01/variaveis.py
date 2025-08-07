# comentario de linha

print("Olá mundo, esse é o meu primeiro script em \npython")
print("hello word")
print('eai meu fi')

'''
comentario de bloco
'''
print(500*"-","eu sou o rei",50*"--")


nome = "leleo"
idade = "16 anos"
nascimento = 2008
print("ola meu nome é",nome)
print("eu tenho",idade)
print("e eu nasci em",nascimento)

# tipos de variaveis

nome = "leleo"
idade = 16
altura = 1.94
ativo = True

print("o tipo da variavel nome é:",type(nome))
print("o tipo da variavel idade é:",type(idade))
print("o tipo da variavel altura é:",type(altura))
print("o tipo da variavel ativo é:" ,type(ativo))

# Operadores
num1 = 10
num2 = 10
soma = num1 + num2
divi = num1 / num2
divisao_inteira = num1 // num2
mult = num1 * num2
expo = num1 ** num2
sub = num1 - num2
resto = num1 %2

print('Resultado da soma',num1, '+', num2, "é:", soma)
print("Resultado da divisao", num1, "/", num2, "é:", divi)
print("Resultado da divisao inteira é:", divisao_inteira)
print("Resultado da multiplicação", num1, "X", num2, "é;", mult )
print("Resultado do expoente é:", expo )
print("Resultado da subtração", num1, "-", num2, "é:", sub)
print("Resultado do resto", num1, "é;", resto ) 

print(30*'-', 'operadores de comparação', 30*'-')
# operadores de comparação
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2 
num1 != num2

ano = 2025
print("ano atual", ano)
ano += 1
print('ano acrecido de +1', ano)
ano -= 1
print('ano decrecido de -1',ano)

# operadores logicos
# AND, OR, NOT

print(30*'-', 'Entrada de dados',30*'-')

nome_usuario = input('digite o seu nome: ')
print("Seja bem-vindo ao sistema python", nome_usuario)

print(30*'-', 'calculadora', 30*'-')

# input por padrão é (str) -> (texto) ou seja (1010), entao é necessario colocar (int)
# numeros com virgula é utilizado (float) inves de (int)
# bool = valores logicos como True e False
numero1 = int(input("digite o primeiro numero:"))
numero2 = int(input('digite o segundo numero:'))

soma = numero1 + numero2
divi = numero1 / numero2
mult = numero1 * numero2
sub = numero1 - numero2

print('Resultado da soma',numero1, '+', numero2, "é:", soma)
print("Resultado da divisao", numero1, "/", numero2, "é:", divi)
print("Resultado da multiplicação", numero1, "X", numero2, "é;", mult )
print("Resultado da subtração", numero1, "-", numero2, "é:", sub) 

'''
print(30*'-', 'Convertendo tipos de dados',30*'-')

ano_nascimento = input("digite seu ano de nascimento:")
print(type(ano_nascimento))
# convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))


n1 = 10
n2 = 20

print("A soma é:", n1+n2, type(n1), float(n2))
'''
saudacao = input('digite seu nome: ')
cpf = input('digite seu CPF: ')
telefone = input("digite seu telefone:")

print(20*'-', 'dados pessoais', 20*'-')
print('nome:', saudacao)
print('CPF:', cpf, '| Telefone: ',telefone)
print(50*'-')