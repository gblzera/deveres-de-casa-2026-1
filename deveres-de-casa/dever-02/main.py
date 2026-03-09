# Cálculo do fatorial usando recursão
# Código comentado por IA - Claude

import time
import sys

# Aumenta o limite de recursão do Python para suportar n = 1000
sys.setrecursionlimit(2000)


# Função recursiva que calcula o fatorial de n
# Caso base: fatorial de 0 é 1
# Caso recursivo: n * fatorial(n - 1)
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


# Função que mede o tempo de execução do cálculo do fatorial para um dado n
def medir_tempo(n):
    inicio = time.time()
    resultado = fatorial(n)
    fim = time.time()
    tempo = fim - inicio
    print(f"fatorial({n}) calculado em {tempo:.6f} segundos")
    return resultado, tempo


def main():
    # Lê um número inteiro do usuário
    n = int(input("Digite um número inteiro para calcular o fatorial: "))

    # Calcula e exibe o fatorial do número digitado
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")

    # Mede o tempo de execução para os valores solicitados
    print("\n--- Medição de tempo de execução ---")
    valores_teste = [10, 100, 500, 1000]
    for valor in valores_teste:
        medir_tempo(valor)

    # Análise de complexidade
    print("\n--- Análise de Complexidade ---")
    print("Complexidade: O(n)")
    print("Raciocínio: a função fatorial(n) faz exatamente n chamadas recursivas")
    print("(n, n-1, n-2, ..., 1, 0), cada uma executando uma multiplicação O(1).")
    print("Portanto, o tempo de execução cresce linearmente com n.")


if __name__ == "__main__":
    main()
