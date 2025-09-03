letra = input("Digite uma letra: ").upper()

vogais_maiusculas = "AEIOU"

if letra in vogais_maiusculas:
    print("A letra é uma vogal maiúscula.")
else:
    print("A letra não é uma vogal maiúscula.")