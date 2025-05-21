def somaImposto(taxaImposto, custo):
    novoValor = custo * (taxaImposto/100 + 1)
    return novoValor
produto1 = somaImposto(20, 1000)
print(f"{produto1:.2f}")