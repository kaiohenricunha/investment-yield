import matplotlib.pyplot as plt

def informar_dados():
    valor_inicial = float(input('Digite o valor inicial: '))
    rendimento = float(input('Digite o rendimento por período(%): '))
    valor_aporte = float(input('Digite o valor do aporte por período: '))
    total_periodos = int(input('Digite o número de períodos: '))

    exibir_dados(valor_inicial, rendimento, valor_aporte, total_periodos)
    calculo(valor_inicial, rendimento, valor_aporte, total_periodos)


def exibir_dados(inicial, renda, aporte, periodos):
    print(f'Valor inicial: R$ {inicial}')
    print(f'Rendimento por período (%): {renda}')
    print(f'Aporte a cada período: R$ {aporte}')
    print(f'Total de períodos: {periodos}')

def calculo(valorInicial, valor_rendimento, valorAporte, totalPeriodos):
    lista_periodos = []
    lista_montantes = []

    for periodo in range(totalPeriodos):
        montante1 = valorInicial * (valor_rendimento / 100)
        montante2 = montante1 + valorInicial + valorAporte
        valorInicial = montante2

        txt = "o montante será de R${valor:.2f}."
        print(f'Após {periodo + 1} períodos(s), ' + txt.format(valor = valorInicial))

        lista_periodos.append(periodo)
        lista_montantes.append(valorInicial)

    plt.plot(lista_periodos, lista_montantes)
    plt.xlabel('Período')
    plt.ylabel('Montante')
    plt.title('Valor(R$) acumulado')

    plt.show()


    
informar_dados()