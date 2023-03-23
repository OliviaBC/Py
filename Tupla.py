'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
''' 

def posicoes(tupla, item):     
  lista = []

  for i in enumerate(tupla):
    if i[1] == item:
      lista.append(i[0])
  return lista
  

tupla = (2, 1, 2, 3, 2)
resultado = posicoes(tupla, 2)                
print(resultado)