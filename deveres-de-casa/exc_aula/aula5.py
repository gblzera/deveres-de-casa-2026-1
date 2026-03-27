"""
Exercício em sala de aula

Analisador de Complexidade com Teorema Mestre

Objetivo:

Desenvolver um programa que auxilie na análise da
complexidade de algoritmos de divisão e conquista utilizando
o Teorema Mestre.

Descrição do exercício

Entrada:

O programa deve receber como entrada os parâmetros da relação
de recorrência no formato T(n) = aT(n/b) + f(n).

Especificamente, o programa deve solicitar ao usuário os valores
de:

a (número de subproblemas)

b (fator de redução do tamanho do problema)

f(n) (custo do trabalho fora das chamadas recursivas)

Para simplificar, limite f(n) a funções polinomiais do tipo n k *log p
(n), onde o programa também solicitará os valores de k e p.

Processamento:

1. O programa deve implementar a logica do teorema mestre para determinar a complexidade assintotica da relacao de recorrencia fornecida

2. o programa deve identificar qual caso o teorema mestre se aplica (caso 1, 2 ou 3)

3. o programa deve realizar calculos necessarios para comprara f(n) com n^log_b(a)

Exemplo

Digite o valor de a: 4

Digite o valor de b: 2

Digite o valor de k (expoente de n em f(n)): 2

Digite o valor de p (expoente de log(n) em f(n)): 0

Entrada: a=4, b=2, k=2, p=0, f(n) = n^2

Caso do Teorema Mestre: Caso 1
"""

import math


def formatar_numero(x: float) -> str:
    """Formata número: inteiro se possível, senão 4 casas decimais."""
    if x == int(x):
        return str(int(x))
    return f"{x:.4f}"


def analisar_teorema_mestre(a: int, b: int, k: float, p: float) -> None:
    """
    Analisa a complexidade usando o Teorema Mestre.

    T(n) = aT(n/b) + f(n)
    f(n) = n^k * log^p(n)
    """
    # Calcula log_b(a)
    log_b_a = math.log(a) / math.log(b)
    log_b_a_str = formatar_numero(log_b_a)
    k_str = formatar_numero(k)
    p_str = formatar_numero(p)

    print(f"\nEntrada: a={a}, b={b}, k={k_str}, p={p_str}, f(n) = n^{k_str}", end="")
    if p != 0:
        print(f" * log^{p_str}(n)")
    else:
        print()

    print(f"\nlog_b(a) = log_{b}({a}) = {log_b_a_str}")

    # Comparar k com log_b(a)
    epsilon = 1e-9  # tolerância para comparação de floats

    if k < log_b_a - epsilon:
        # Caso 1: f(n) = O(n^(log_b(a) - ε))
        print(f"\nComo k = {k_str} < log_b(a) = {log_b_a_str}")
        print("f(n) = O(n^(log_b(a) - ε))")
        print("\nCaso do Teorema Mestre: Caso 1")
        print(f"T(n) = Θ(n^log_b(a)) = Θ(n^{log_b_a_str})")

    elif abs(k - log_b_a) <= epsilon:
        # Caso 2: f(n) = Θ(n^log_b(a) * log^p(n))
        print(f"\nComo k = {k_str} = log_b(a) = {log_b_a_str}")
        print(f"f(n) = Θ(n^log_b(a) * log^{p_str}(n))")
        print("\nCaso do Teorema Mestre: Caso 2")
        p_plus_1 = formatar_numero(p + 1)
        if p >= 0:
            print(f"T(n) = Θ(n^log_b(a) * log^(p+1)(n)) = Θ(n^{log_b_a_str} * log^{p_plus_1}(n))")
        else:
            # Caso especial: p < -1 não é coberto pelo teorema mestre padrão
            print(f"T(n) = Θ(n^log_b(a) * log^(p+1)(n)) = Θ(n^{log_b_a_str} * log^{p_plus_1}(n))")

    else:
        # Caso 3: f(n) = Ω(n^(log_b(a) + ε))
        print(f"\nComo k = {k_str} > log_b(a) = {log_b_a_str}")
        print("f(n) = Ω(n^(log_b(a) + ε))")
        print("\nCaso do Teorema Mestre: Caso 3")
        if p != 0:
            print(f"T(n) = Θ(f(n)) = Θ(n^{k_str} * log^{p_str}(n))")
        else:
            print(f"T(n) = Θ(f(n)) = Θ(n^{k_str})")


def main():
    print("=" * 50)
    print("Analisador de Complexidade com Teorema Mestre")
    print("T(n) = aT(n/b) + f(n)")
    print("f(n) = n^k * log^p(n)")
    print("=" * 50)

    a = int(input("\nDigite o valor de a (número de subproblemas): "))
    b = int(input("Digite o valor de b (fator de redução): "))
    k = float(input("Digite o valor de k (expoente de n em f(n)): "))
    p = float(input("Digite o valor de p (expoente de log(n) em f(n)): "))

    if a < 1:
        print("Erro: 'a' deve ser >= 1")
        return
    if b <= 1:
        print("Erro: 'b' deve ser > 1")
        return

    analisar_teorema_mestre(a, b, k, p)


if __name__ == "__main__":
    main()