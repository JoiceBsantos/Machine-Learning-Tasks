# ===================================================================================================
# TAREFA 3:  -  Aprendizado Não Supervisionado - Aqui, não temos rótulos, apenas um monte de dados.
# A tarefa do algoritmo é encontrar padrões, grupos (clusters) por conta própria."Vamos usar o algoritmo 
# KMeans para encontrar 2 grupos de clientes com base no valor gasto e na frequência de visitas. 
# Não dizemos qual cliente pertence a qual grupo; o algoritmo deve descobrir."
# ===================================================================================================

import numpy as np
from sklearn.cluster import KMeans

print("--- Exercício 3 - Missão 2 (Aprendizado Não Supervisionado) ---")

# Dados: [valor_gasto_medio, frequencia_visitas_mensal]
clientes = np.array([
    [30, 1], [45, 2], [35, 1],    # Grupo de baixo valor/frequência
    [500, 8], [600, 10], [550, 9] # Grupo de alto valor/frequência
])

# Criar modelo KMeans para 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# Treinar o modelo e obter o cluster de cada cliente
clusters_encontrados = kmeans.fit_predict(clientes)

print(f"Dados dos clientes (sem rótulos):\n{clientes}")
print(f"Clusters encontrados pelo KMeans para cada cliente: {clusters_encontrados}")
print("Observe como o algoritmo separou corretamente os clientes nos grupos 0 e 1.")
print("-" * 50, "\n")


