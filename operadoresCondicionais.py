#se 5 é maior que 3 entao 
print("exemplo 1")
if 5 > 3:
  print('5 é maior que 3')

#se 5 é maior que 6 entao....senão...
print("exemplo 2")
if 5 > 6:
      print('5 é maior')
else:
  print('5 não é maior')

#else if  - se n é igual a 4 entao .....senão se n for igual a 3  entao .....senão .....
print("exemplo 3")
n = 9
if n == 4:
  print('n é igual a 4')
else:
  if n == 3:
    print('n é igual a 3')
  else:
    print('n não é igual a 4 nem 3')

#if com operadores lógicos e relacionais
print("exemplo 4")
x = 1
y = 5
#avaliar os relacionais -> x>1 - falso pois x é 1  e 1 não é maior que 1
#y == 0 - falso pois y é 5 e não é igual a zero
# então temos (falso)ou(falso) = falso, pois no ou só se tiver uma sentença true é que será verdadeira
if (x > 1) or (y == 0):
  print('x é maior que 1 e y é par')
else:
  print('Uma ou nenhuma das condições foram satisfeitas')