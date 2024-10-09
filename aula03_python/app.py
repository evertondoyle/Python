import numpy as np
import matplotlib.pyplot as plt

def simulacao_monte_carlo(salario, bonus, constante_bonus, num_simulacoes=1000):
    resultados = []
    for _ in range(num_simulacoes):
        # Adicionando alguma variabilidade ao salário e ao bônus
        salario_variavel = np.random.normal(salario, salario * 0.1)
        bonus_variavel = np.random.normal(bonus, bonus * 0.2)
        
        valor_final = constante_bonus + (salario_variavel * bonus_variavel)
        resultados.append(valor_final)
    
    return resultados

# Executando a simulação
resultados = simulacao_monte_carlo(1000, 0.1, 1000)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.hist(resultados, bins=30, edgecolor='black')
plt.title('Simulação de Monte Carlo - Distribuição dos Valores Finais')
plt.xlabel('Valor Final')
plt.ylabel('Frequência')
plt.grid(True, alpha=0.3)
plt.show()

# Exibindo algumas estatísticas
print(f"Média: {np.mean(resultados):.2f}")
print(f"Mediana: {np.median(resultados):.2f}")
print(f"Desvio Padrão: {np.std(resultados):.2f}")