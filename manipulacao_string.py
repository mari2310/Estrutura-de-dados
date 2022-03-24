#manipulação de strings
a = 'casaco'
print(a)

#colocar em maiúscula
maiuscula = a.upper()
print(maiuscula)

#colocar em minúscula
minuscula = maiuscula.lower()
print(minuscula)

#primeira letra maiuscula
nome = a.capitalize()
print(nome)

#pegar começo da palavra
metade_palavra = a[0:3]
#no python ele não pega o ultimo elemento - a[0:3].Ele vai de 0 até 2 nesse exemplo.
print(metade_palavra)

#pegar final da palavra
ultimas_letras = a[3:]
print(ultimas_letras)

#trocar caracteres
b = a.replace('aco', 'inha')
print(a)
print(b)

#pesquisar na string - encontra a posição da letra . sempre começa no 0.se tivermais de uma
#ocorrência, só retorna a posição da primeira ocorrência encontrada.Se a letra não existir irá retornar -1
c = b.find('s')
print(c)

#contagem de caracteres.Considera os espaços
e = 'casaco '
print(len(e))

#para não contar os espaços
f = e.strip()
print(len(f))

#Formatação - utilizar o f antes do texto faz acessar o valor contido nas variáveis e não simplesmente exibir o nome da variável
n1 = 14
n2 = 16
print('Dividindo {n1} por {n2} o resultado é {n1/n2}')
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')