numero = int(input("Digite um número inteiro: "))

if(numero % 2 == 0) and (numero < 100):
  print("O numero é par e menor que 100")
if(numero % 2 == 0) and (numero >= 100):
  print("O numero é par e maior ou igual a 100")
if(numero % 2 != 0) and (numero < 100):
  print("O numero é ímpar e menor que 100")
if(numero % 2 != 0) and (numero >= 100):
  print("O numero é ímpar e maior ou igual a 100")