def contarBilletes(total, recibido):
    resto = recibido - total
    b500 = lambda resto: resto // 500
    resto = resto % 500
    b100 = lambda resto: resto // 100
    resto = resto % 100
    b50 = lambda resto: resto // 50
    resto = resto % 50
    b20 = lambda resto: resto // 20
    resto = resto % 20
    b10 = lambda resto: resto // 10
    resto = resto % 10
    b5 = lambda resto: resto // 5
    resto = resto % 5
    b1 = lambda resto: resto // 1
    return resto, b500, b100, b50, b20, b10, b5, b1

totalCompra = float(input("Ingrese el valor total de la compra: "))
dineroRecibido = float(input("Ingrese el dinero recibido: "))
restoTotal, b500, b100, b50, b20, b10, b5, b1 = contarBilletes(totalCompra, dineroRecibido)

if restoTotal < 0:
    print("El dinero recibido es insuficiente")
else:
    print("El vuelto consiste en:")
    print("Billetes de $500:", b500)
    print("Billetes de $100:", b100)
    print("Billetes de $50:", b50)
    print("Billetes de $20:", b20)
    print("Billetes de $10:", b10)
    print("Billetes de $5:", b5)
    print("Billetes de $1:", b10)