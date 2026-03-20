"""
Implemente uma função recursiva que calcule F(n) conforme a
seguinte recorrência:

F(n)=F(n/2)+3F(n)

com a condição de que n seja uma potência de 2 e o caso
base retorne 5.

O programa deve:

Solicitar ao usuário um valor de n (verifique se é uma potência
de 2).

Calcular e imprimir F(n).
"""


# Verifica se n é potência de 2
def eh_potencia_de_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


# Função recursiva: F(n) = F(n/2) + 3n, caso base F(1) = 5
def F(n):
    if n == 1:
        return 5
    return F(n // 2) + 3 * n


# Programa principal
n = int(input("Digite um valor para n: "))

if eh_potencia_de_2(n):
    print(f"F({n}) = {F(n)}")
else:
    print("Erro: n deve ser uma potência de 2 (ex: 1, 2, 4, 8, 16...)")