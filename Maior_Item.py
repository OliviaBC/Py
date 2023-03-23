lista = []
i = 0

for i in range(10):
    n = int(input("Digite o %dº número: " % (i + 1)))
    lista.append(n)
print("\n", lista)

maior = max(lista)
print("\n O maior item da lista é o número", maior)
