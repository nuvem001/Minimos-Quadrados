from protocoloEliminacaoGaussPivotamento import Eliminação_de_Gauss_com_pivoteamento
# def montar_sistema_normal(x1, x2, y):
#     """
#     f(x1,x2) = β0 + β1*x1 + β2*x2
#     """
#     n = len(y)
#     """usando identidades de matrizes, uma matriz 3x3, apartir da matrix 2x3 do livro de frederico de algoritmos numéricos, capitulo de minimos quadrados 4.1.3, ficaria como abaixo"""
#     A = [
#         [n, sum(x1), sum(x2)],
#         [sum(x1), sum(xi**2 for xi in x1), sum(xi*xj for xi, xj in zip(x1, x2))],
#         [sum(x2), sum(xi*xj for xi, xj in zip(x1, x2)), sum(xj**2 for xj in x2)]
#     ]

#     b = [
#         sum(y),
#         sum(xi*yi for xi, yi in zip(x1, y)),
#         sum(xj*yj for xj, yj in zip(x2, y))
#     ]
#     return A, b
def montar_sistema_normal(x1, x2, y):
    n = len(y)
    
    """
    f(x1,x2) = β0 + β1*x1 + β2*x2
    """
    sum_x1 = sum(x1)
    sum_x2 = sum(x2)
    sum_x1_sq = sum(xi**2 for xi in x1)
    sum_x2_sq = sum(xj**2 for xj in x2)
    sum_x1x2 = sum(x1[i] * x2[i] for i in range(n)) 
    
    """usando identidades de matrizes, uma matriz 3x3, apartir da matrix 2x3 do livro de frederico de algoritmos numéricos, capitulo de minimos quadrados 4.1.3, ficaria como abaixo"""

    A = [
        [n, sum_x1, sum_x2],
        [sum_x1, sum_x1_sq, sum_x1x2],
        [sum_x2, sum_x1x2, sum_x2_sq]
    ]
    
    # Calcula os elementos do vetor b
    sum_y = sum(y)
    sum_x1y = sum(x1[i] * y[i] for i in range(n))  # Sem zip!
    sum_x2y = sum(x2[i] * y[i] for i in range(n))  # Sem zip!
    
    b = [sum_y, sum_x1y, sum_x2y]
    
    return A, b

def ajuste_linear(x1, x2, y):
    
    A, b = montar_sistema_normal(x1, x2, y)
    beta = Eliminação_de_Gauss_com_pivoteamento(3, A, b)
    return beta