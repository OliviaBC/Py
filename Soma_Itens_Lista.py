lista = []

for i in range(10):
  n = int(input("Digite o %dº número: " %(i+1)))
  lista.append(n)

soma = sum(lista)
print("\nA soma dos números da lista é", soma)