#manipulação de variáveis e constantes

#sem necessidade de declarar o tipo de variável
numero = -3 
numero_jogos = 14
numero_convidados = 15

#exibir o conteúdo da variável
print(numero)
print(numero, numero_jogos)

#strings e char
letra = 'a'
palavra1 = 'Linguagem de programação'
palavra2 = 'Python'
print(letra, palavra1)

#concatenação de variáveis com texto
print('Estou apredendo uma' , palavra1)
print('Esta', palavra1, 'se chama', palavra2)

#entrada de informação por usuário
idade = input('Digite sua idade:')

#saída da informação digitada pelo usuário
print('Sua idade é', idade)

#utilizando o int antes do input, ele transforma a string em inteiro podendo fazer operações com o mesmo
# para a conversão em String quando for necessário, usa-se str antes do input
numeroEmString = int(input('digite um número: '))
print(numeroEmString)
numeroEmString = numeroEmString * 3
print(numeroEmString)



