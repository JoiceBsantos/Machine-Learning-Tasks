# ========================================================================================================
# Exercício 5: Tarefa: Crie uma árvore de decisão para aprovar (1) ou negar (0) um empréstimo com base na 
# renda anual (em milhares) e se a pessoa possui casa própria (1=Sim, 0=Não).
# ========================================================================================================

import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("\n--- 3.2: Exercício - Aprovar Empréstimo 💰 ---")

# Base de dados (renda em R$ mil e casa própria [1=sim, 0=não])
dados_credito = np.array([
    [50, 1],
    [30, 0],
    [80, 1],
    [40, 0],
    [120, 1],
    [70, 0]
])
decisao_credito = np.array([1, 0, 1, 0, 1, 1])

# Treinamento do modelo
modelo_credito = DecisionTreeClassifier(random_state=42)
modelo_credito.fit(dados_credito, decisao_credito)

# Interatividade 🧠
renda = float(input("Informe a renda do cliente (em milhares, ex: 90): "))
casa = int(input("O cliente possui casa própria? (1 = Sim, 0 = Não): "))

novo_cliente = np.array([[renda, casa]])
previsao_credito = modelo_credito.predict(novo_cliente)
resultado_credito = "✅ Aprovado" if previsao_credito[0] == 1 else "❌ Negado"

print(f"\nDecisão para o cliente [R${renda}k, Casa Própria: {'Sim' if casa == 1 else 'Não'}] → {resultado_credito}")
