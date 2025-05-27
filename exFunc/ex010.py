"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
 obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" 
 e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente"""
import numpy
jogadas = {"1ª Jogada": None}
contador = 1
ponto = 0

def lancarDados():
    dado1 = numpy.random.default_rng()
    dado2 = numpy.random.default_rng()
    return dado1.integers(1, 6) + dado2.integers(1, 6)

def conferirResultadoPrimeiraJogada(resultado):
    if jogadas['1ª Jogada'] == 11 or jogadas['1ª Jogada'] == 7:
        return 'Você ganhou'
    else:
        global ponto 
        ponto = resultado
        return ponto
def conferirProximosResultado(resultado):
    if resultado == ponto:
        return "Venceu"
    elif resultado == 7:
        return "Perdeu"
    else:
        return "Continue"

while True:
    if not input('Deseja jogar os dados?[s/n]\n') == 's':
        break
    print(f"Ponto: {ponto}")
    resultado = lancarDados()
    jogadas[f'{contador}ª Jogada'] = resultado
    print(f"Jogadas: {jogadas}")
    if contador == 1:
        resultadoprimeirapartida = conferirResultadoPrimeiraJogada(resultado)
        
        if resultadoprimeirapartida == "Você ganhou":
            print('Ganhou!')
            break
        jogadas[f'{contador}ª Jogada'] = resultado
    else:
        resultadofinal = conferirProximosResultado(resultado)
        if resultadofinal == "Perdeu":
            print("Perdeu")
            break
        elif resultadofinal =="Venceu":
            print('Venceu')
            break

        
        jogadas[f'{contador}ª Jogada'] = resultado


    contador += 1    
    

    
    

    


