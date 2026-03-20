"""
F(n) = F(n-1)+n+1 com o caso base F(0) = 1
F(n) = F(n-1)+3n+2 como caso base F(1) = 1

crie uma algoritmo python que epca ao usuario um valor n e retorne os valores de F(n) para a funcao, recusriva
"""

# Função 1: F(n) = F(n-1) + n + 1 com caso base F(0) = 1
def funcao1(n):
    if n == 0:
        return 1
    return funcao1(n - 1) + n + 1


# Função 2: F(n) = F(n-1) + 3n + 2 com caso base F(1) = 1
def funcao2(n):
    if n == 1:
        return 1
    return funcao2(n - 1) + 3 * n + 2


# Programa principal
n = int(input("Digite um valor para n: "))

print(f"Função 1 - F({n}) = {funcao1(n)}")
print(f"Função 2 - F({n}) = {funcao2(n)}")