i = 0
maior=0
idade = 0
quantidade = 0

for i in range(10):
    idade = int(input("Digite a %d idade : " %i))
    if(idade > maior):
        maior = idade
    if((idade >= 12) and (idade <= 18)):
        quantidade = quantidade + 1
print ("A maior idade é: %d anos" %maior)
print("\nExistem %d pessoas com idade entre 12 e 18 anos" %quantidade)