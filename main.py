from protocoloLeitura import Cria_Listas_dados, gerar_dados_aleatorios
from protocoloMinimosQuadrados import ajuste_linear

def mostrar_resultados(beta):
    print("\nResultado do Ajuste:")
    print(f"β0 (intercepto) = {beta[0]:.6f}")
    print(f"β1 (coef. x1)   = {beta[1]:.6f}")
    print(f"β2 (coef. x2)   = {beta[2]:.6f}")
    print(f"\nEquação ajustada:")
    print(f"y = {beta[0]:.6f} + {beta[1]:.6f}*x1 + {beta[2]:.6f}*x2")

def main():
    print("Sistema de Ajuste Linear por Mínimos Quadrados")
    
    while True:
        print("\nMenu:")
        print("1 - Ajustar dados das meninas (arquivo 1)")
        print("2 - Ajustar dados das meninas (arquivo 2)")
        print("3 - Usar dados gerados aleatoriamente")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == '0':
            break
        elif opcao == '1':
            x1, x2, y = Cria_Listas_dados("dadosMeninas1.csv")
        elif opcao == '2':
            x1, x2, y = Cria_Listas_dados("dadosMeninas2.csv")
        elif opcao == '3':
            x1, x2, y = gerar_dados_aleatorios()
            print("\nDados gerados:")
            for i in range(min(5, len(x1))):
                print(f"x1={x1[i]:.3f}, x2={x2[i]:.3f}, y={y[i]:.3f}")
        else:
            print("Opção inválida!")
            continue

        if None in (x1, x2, y):
            continue

        try:
            beta = ajuste_linear(x1, x2, y)
            mostrar_resultados(beta)
        except Exception as e:
            print(f"Erro no ajuste: {e}")
1
if __name__ == "__main__":
    main()