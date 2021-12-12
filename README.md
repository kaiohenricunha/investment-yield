# Requirements

Install matplotlib
```
pip install matplotlib
```
# How it works

The app starts by asking the user to enter the initial amount of money they have, expected yield, monthly contribution and estimated time range in months.

```
def informar_dados():
    valor_inicial = float(input('Digite o valor inicial: '))
    rendimento = float(input('Digite o rendimento por período(%): '))
    valor_aporte = float(input('Digite o valor do aporte por período: '))
    total_periodos = int(input('Digite o número de períodos: '))

    exibir_dados(valor_inicial, rendimento, valor_aporte, total_periodos)
    calculo(valor_inicial, rendimento, valor_aporte, total_periodos)
```

It, then, prints the user's input.

```
def exibir_dados(inicial, renda, aporte, periodos):
    print(f'Valor inicial: R$ {inicial}')
    print(f'Rendimento por período (%): {renda}')
    print(f'Aporte a cada período: R$ {aporte}')
    print(f'Total de períodos: {periodos}')
```

And calculates the investment's value after the specified time, month by month.

```
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
```

This snippet uses the matplotlib library to plot the investment's value after the specified time in a graph.

```
    plt.plot(lista_periodos, lista_montantes)
    plt.xlabel('Período')
    plt.ylabel('Montante')
    plt.title('Valor(R$) acumulado')

    plt.show()
```

This is the output for an initial investiment of R$ 10.000, expected yield of 10% per month, monthly contribution of R$ 300 and a total of 12 months.

![Screen Shot 2021-12-12 at 11 29 32](https://user-images.githubusercontent.com/69804490/145716597-7f1948d9-37c4-4549-adc9-09b046a20c8b.png)

