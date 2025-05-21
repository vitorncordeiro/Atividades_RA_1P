def verifica(arg):
    if arg > 0:
        return "P"
    else:
        return "N"
numero = verifica(-1)
print(numero)