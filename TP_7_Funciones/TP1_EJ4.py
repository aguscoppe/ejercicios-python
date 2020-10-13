def contarBilletes(total, recibido):
    resto = recibido - total
    lista = [0, 0, 0, 0, 0, 0, 0]
    while resto > 0:
        if resto >= 500:
            resto -= 500
            lista[0] += 1
        elif resto >= 100:
            resto -= 100
            lista[1] += 1
        elif resto >= 50:
            resto -= 50
            lista[2] += 1
        elif resto >= 20:
            resto -= 20
            lista[3] += 1
        elif resto >= 10:
            resto -= 10
            lista[4] += 1
        elif resto >= 10:
            resto -= 10
            lista[5] += 1
        else:
            resto -= 1
            lista[6] += 1
    return lista, resto

totalCompra = float(input("Ingrese el valor total de la compra: "))
dineroRecibido = float(input("Ingrese el dinero recibido: "))
listaBilletes, restoTotal = contarBilletes(totalCompra, dineroRecibido)

if restoTotal < 0:
    print("El dinero recibido es insuficiente")
else:
    print("El vuelto consiste en:")
    print("Billetes de $500:", listaBilletes[0])
    print("Billetes de $100:", listaBilletes[1])
    print("Billetes de $50:", listaBilletes[2])
    print("Billetes de $20:", listaBilletes[3])
    print("Billetes de $10:", listaBilletes[4])
    print("Billetes de $5:", listaBilletes[5])
    print("Billetes de $1:", listaBilletes[6])