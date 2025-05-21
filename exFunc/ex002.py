def printarAteN(n):
    for i in range(1, n+1):
        listai = []
        for j in range(1, i+1):
            listai.append(j)
        print(*listai)
numero = int(input('Digite o número: '))
printarAteN(numero)