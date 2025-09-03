a = int(input("Digite um número: "))
par = a % 2
impar = a % 2
if par == 0:
    print("O número é par")
elif impar != 0:
    print("O número é ímpar")