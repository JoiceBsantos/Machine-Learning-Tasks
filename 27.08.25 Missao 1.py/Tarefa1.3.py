# TAREFAS DE APRENDIZADO NAO SUPERVISIONADO 

# =============================================================================
# TAREFA 3: Previsão de Tempo de Entrega de Pizza
# =============================================================================

#Instale scikit-learn se necessário: pip install scikit-learn

import numpy as np
from sklearn.linear_model import LinearRegression

print("\n--- 1.2 Exercício para Alunos (Supervisionado) ---")

# Dados de Treino: [distancia_km, numero_de_pizzas]
dados_entregas = np.array([
    [5, 2],   # 5 km, 2 pizzas
    [2, 1],   # 2 km, 1 pizza
    [10, 4],  # 10 km, 4 pizzas
    [7, 3],   # 7 km, 3 pizzas
    [1, 1]    # 1 km, 1 pizza
])

# Rótulos: Tempo de entrega em minutos
tempos_entrega = np.array([30, 15, 55, 40, 10])

# Criação e treinamento do modelo LinearRegression
modelo_entrega = LinearRegression()
modelo_entrega.fit(dados_entregas, tempos_entrega)

print("Modelo treinado com sucesso!")

# Fazer a previsão para um novo pedido: 8 km de distância e 2 pizzas
pedido_novo = np.array([[8, 2]])
tempo_previsto = modelo_entrega.predict(pedido_novo)

print(f"Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")

# Teste com outros pedidos
testes_entrega = [
    [6, 3],   # 6 km, 3 pizzas
    [9, 1],   # 9 km, 1 pizza
    [11, 4]   # 11 km, 4 pizzas
]

print("\n--- Testes de Previsão de Entrega ---")
for i, teste in enumerate(testes_entrega):
    tempo = modelo_entrega.predict([teste])[0]
    print(f"Pedido {i+1}: {teste[0]} km, {teste[1]} pizza(s) -> {tempo:.2f} minutos")
