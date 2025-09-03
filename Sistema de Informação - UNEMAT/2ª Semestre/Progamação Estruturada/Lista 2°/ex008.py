a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
if a > b and a > c:
    print("O maior número é:", a)
elif b > c:
    print("O maior número é:", b)
else:
    print("O maior número é:", c)