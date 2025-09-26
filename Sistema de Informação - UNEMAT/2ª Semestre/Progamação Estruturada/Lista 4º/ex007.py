a = (1,2,3,4,5)
print(a)
r = int(input("Digite o numero que deseja remover: "))
a.remove(r)
print(a)
#AttributeError: 'tuple' object has no attribute 'remove'