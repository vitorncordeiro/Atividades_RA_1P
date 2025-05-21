def printarAteN(n):
    for i in range(1, n+1):
        listai = []
        for j in range(i):
            listai.append(i)
        print(*listai)
numero = int(input('Digite o número: '))
