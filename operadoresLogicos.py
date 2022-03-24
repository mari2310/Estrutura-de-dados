#variáveis do tipo booleano
a = True
b = False
c = False

print(a, b)

# no AND só será True se as duas condições forem true senão dará false
#duas maneiras de escrever:& / and
e = a and b  
f = b & c
print('e = a and b:',e)
print('f = b & c:',f)

#se precisar dar destaque a uma palavra usa-se as aspas duplas para o texto e as simples para dar enfase a palavra que se escolheu dar
print("'B' and 'C' : ", f)

# no OR  será True caso alguma das variáveis seja true.Se todas forem false, será false
#duas maneiras de escrever:| / or
g = a or b
print('g = a or b:',g)
h = b | c
print('h = b | c:',h)

#not inverte o valor booleano. se a variável for true e colocar not antes da variavel, ela apresentará valor false
print('not a:',not a)
print('not b:',not b)

#operadores relacionais: analisa a relacão e retorna verdadeiro ou falso
i = 5 > 3
print('i = 5 > 3 : ',i)
j = 5 < 3
print('j = 5 < 3 : ',j)
k = 5 >= 5
print('k = 5 >= 5 : ',k)
l = 5 >= 3
print('l = 5 >= 3 : ',l)
m = 5 == 3
print('m = 5 == 3 : ',m)
n = 5 != 3
print('n = 5 != 3 : ',n)