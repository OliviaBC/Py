import random

lista = []
i = 0;

for i in range(5):
  item = input("Digite o %dº elemento: " %(i+1))
  lista.append(item)

print("\n\n", lista)
random.shuffle(lista)

print("\n", lista)