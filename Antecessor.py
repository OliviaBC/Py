tipo = int(input("Informe se o número é: \n\n 1 (inteiro) ou 2 (decimal) - "))

if tipo == 1:
    numero = int(input("\nDigite um número de: "))
    if 0 <= numero and numero <= 100000:
        antecessor = numero - 1
        print("\nO antecessor de {} é {}".format(numero, antecessor))

elif tipo == 2:
    numero2 = float(input("\nDigite um número: "))
    if numero2 != 0 and numero2 != 100000:
        antecessor = numero2 - 0.01
        print("\nO antecessor de {} é {}".format(numero2, antecessor))
    else:
        print("\nPor favor, digite um número que corresponda as orientações.")

else:
    print(
        "\nPor favor, digite um dos números das opções acima.")
