listfilmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]
for i in range (1,5,1):
    if listfilmes[i] == "Filme 1":
        print("Qual nota você daria para o filme 1?")
        nota = int(input(listfilmes[i] + ": "))
    elif listfilmes[i] == "Filme 2":
        print("Qual nota você daria para o filme 2?")
        nota = int(input(listfilmes[i] + ": "))
    elif listfilmes[i] == "Filme 3":
        print("Qual nota você daria para o filme 3?")
        nota = int(input(listfilmes[i] + ": ")) 
    elif listfilmes[i] == "Filme 4":
        print("Qual nota você daria para o filme 4?")
        nota = int(input(listfilmes[i] + ": "))
    elif listfilmes[i] == "Filme 5":
        print("Qual nota você daria para o filme 5?")
        nota = int(input(listfilmes[i] + ": "))
    pr = input("Deseja sair? (s/n)").lower().upper()
    if pr == "S":
        continue
    else:
        for i in range (1,i+1,1):
            print(listfilmes[i] + " Nota: " + str(nota))
            break
    