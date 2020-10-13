def calcularViajes(cant):
    # precio -> valor aleatorio asignado
    # ya que la consigna no lo especifica
    precio = 20 
    total = (cant * precio)
    if cant >= 21 and cant <= 30:
        porcentaje = 20
    elif cant >= 31 and cant <= 40:
        porcentaje = 30
    elif cant > 40:
        porcentaje = 40
    else:
        return total
    descuento = (porcentaje*total)/100
    return total - descuento

n = int(input("Ingrese la cantidad de viajes que realizó este mes: "))
print("Total gastado en viajes:", calcularViajes(n))