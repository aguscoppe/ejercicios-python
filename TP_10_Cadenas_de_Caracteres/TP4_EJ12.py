palos = ["Oros", "Copas", "Espadas", "Bastos"]

listaNaipes = [f"{str(j)} {palos[i]}" for i in range(len(palos)) for j in range(1, 13)]

for naipe in listaNaipes:
    print(naipe)