# imprime o numero do informado até o anterior do segundo número informado
#para o numero que está na faixa de até 6 imprima o número
print("exemplo 1")
for numero in range(1, 6):
  print(numero)

#for decrescente, informando onde começa até onde termina e de quanto em quanto vai andar
#vai do 5 até o 0 subtraindo 1 por vez
print("exemplo 2")
for numero in range(5, 0, -1):
  print(numero)

#fazer uma soma com for
print("exemplo 3")
soma = 0
# for vai percorrer os números de 1 a 5
for numero in range(1, 6):
    #variavel soma vai receber o valor que já possui mais o valor de número
  soma = soma + numero
  #print(soma) - mostra o valor de soma a cada laço de for feito
print(soma)

#for para uma string
print("exemplo 4")
palavra = 'sorvete'
# o for vai percorrer cada posição da palavra
for letra in palavra:
  #print(letra) - imprime a letra que está percorrerndo a cada laço de for
  if letra == 'v':
      #verificando se a palavra possui a letra v através da variável letra que percorre a palavra
    print('Achou a letra v')

#for dentro de outro for
print("exemplo 5")
#percorre i de 0 a 4
for i in range(0,5):
      print("laço i :",i)
      print('---')
      #percorre j de 0 a 2 dentro do i que está
      for j in range(0,3):
            print("laço j",j)
      print("fim laço")
      print()
      print()

#WHILE-----------------------------------------------------------------------------------------------
print("exemplo 6")
numero = 1
#enquanto numero for menor que 6
while numero < 6:
#exibe o número
  print(numero)
#numero recebe numero mais 1
  numero += 1
print('---')

print("exemplo 7")
numero = 5
#enquanto numero for maior que 0
while numero > 0:
    #exibe o número
  print(numero)
  #numero recebe numero menos 1
  numero -= 1

print("exemplo 8")
soma = 0
numero = 1
#enquanto número for menor que 6
while numero < 6:
    #soma recebe seu valor + numero
  soma += numero
  #numero recebe seu próprio valor + 1
  numero += 1
  #exibe a soma
print(soma)

print("exemplo 9")
numero = 12
while numero < 1 or numero > 10:
#faz com que o código só continue caso seja informado um número válido. senão continuará dentro do while
  numero = int(input('Digite um número de 1 a 10: '))
print("número aceito")