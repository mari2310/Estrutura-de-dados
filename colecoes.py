#TUPLAS-USA()-------------------------------------------------------------------------------------------------------------------------------------------------------

#Recebe mais de um valor
tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla)

#acessa uma posição específica da tupla
print(tupla[0])

# saber a posição de determinado elemento dentro da tupla
print(tupla.index('Canis familiaris'))

#percorre cada elemento da tupla
for elemento in tupla:
  print(elemento)

#LISTAS-USA[]-----------------------------------------------------------------------------------------------------------------------------------------------

l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

#Junta as duas listas em uma só
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

#criando uma nova lista com os valores duplicados - aparecerá 2 do mesmo elemento
l2_2 = l2 * 2
print(l2_2)

#Acessar elemento de determinada posição
print(l1[0])

#Acessar mais de um elemento da lista
print(l1[0:2])

#Adicionar elemento em uma lista
l1.append('Gorila gorila')
print(l1)

#remover um elemento da lista 
l1.remove('Felis catus')
print(l1)

#deletar toda a lista
del(l1)
#se pedir pra exibir vai dar erro pq não existe mais 
#print(l1)

#para percorrer uma lista com estrututa de repetição
for item in l2_2:
  print(item)

#DICIONARIOS-USA{}-CONCEITO NOME - VALOR----------------------------------------------------------------------------------------------------------------------------------------

coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}

#informando nome e retornando o valor
print(coleta['Aedes aegypt'])

#adicionar novos elementos
coleta['Rhodnius montenegrensis'] = 11
print(coleta)

#apagando registro
del(coleta)['Aedes albopictus']
print(coleta)

#ver o dicionario completo
print(coleta.items())

#imprime somente os nomes das chaves
print(coleta.keys())

#imprime somente os valores
print(coleta.values())

#criando um novo dicionario
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

#juntando o dicionario coleta com o coleta 2
coleta.update(coleta2)
print(coleta)

#percorrendo itens com for
coleta.items()
for especie, num_especimes in coleta.items():
  print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')

#CONJUNTOS----------------------------------------------------------------------------------------------------------------------------------------

biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(biomoleculas)

#trabalhando com conjuntos(SET), não aparecem valores duplicados
print(set(biomoleculas))

#intersecção = valores que estão em ambos os conjuntos
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)

#diferença entre conjuntos - retira de c1 os valores que estão em c1 e c2
c1.difference(c2)

#diferença entre conjuntos - retira de c2 os valores que estão em c1 e c2
c2.difference(c1)