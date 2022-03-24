
a = 10
b = 2
print(a,b)

#soma
print('A soma é', a + b)

#subtração
print('A subtração é', a - b)

#divisão
print('A divisão é', a / b)

#multiplicaçao
print('A multiplicação é', a * b)

#resto da divisão
print('O resto da divisão é', a % b)

#5 elevado a 3
print('5 elevado a 3 é', 5**3)

#raiz quadrada
#usa-se biblioteca
import math
r = math.sqrt(81)
print(r)

#arredondamento
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes
print(casos_por_habitante)
#round para arredondar, numeral pra saber quanos números apos a virgula
estimativa = round(casos_por_habitante, 6)
print(estimativa)
