
num = []
pe = int(input("Quantos números deseja adicionar: "))
for i in range(pe):
    pe1 = int(input(f"Digite o número {i+1}: "))
    num.append(pe1)

pares = 0
soma_pares = 0
for j in num:
    if j % 2 == 0:
        soma_pares += j
        pares += 1

if pares > 0:
    media = soma_pares / pares
    print(f"Média dos números pares: {media}")
else:
    print("Nenhum número par foi inserido.")
