"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M.
ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores 
de entrada todas as vezes que desejar."""
def conversao(horas, minutos, periodo: str): 
    horaConvertida = horas - 12
    return f"{horaConvertida}:{minutos} PM"

def mostrar(horas, minutos, periodo):
    if periodo == 'P':
        return(conversao(horas, minutos, periodo))    
    return f"{horas}:{minutos} AM"
while True:   
    hora = int(input('Digite as horas em formato 24 horas\n'))
    min = int(input('Digie os minutos\n'))
    if hora >= 12:
        p = 'P'
    else:
        p = 'A'
    print(mostrar(hora, min, p))
    if input('Deseja continuar? [s/n]\n') == 's':
        continue
    else:
        print('Encerrando...')
        break
