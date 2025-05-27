"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127
-> 72"""
def inverter(num):
    listanum = list(num)
    listanum.reverse()
    return ''.join(listanum)
num = input('Digite o num: ')
print(inverter(num))
