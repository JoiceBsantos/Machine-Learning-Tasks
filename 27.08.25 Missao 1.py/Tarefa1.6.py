# TAREFAS DE APRENDIZADO NAO SUPERVISIONADO 

# =============================================================================
# TAREFA 6: Encontrar Produtos "Âncora"
# =============================================================================
import numpy as np
from sklearn.cluster import KMeans

print("\n--- Exercício Não Supervisionado ---")

# Dados: [preco_produto, nota_de_popularidade (0-10)]
dados_produtos = np.array([
    [10, 2], [15, 3], [12, 1],      # Categoria 1: Baratos e menos populares
    [200, 9], [180, 8], [210, 10],  # Categoria 2: Caros e muito populares
    [50, 5], [60, 6]                 # Categoria 3: Intermediários
])

# Criar modelo KMeans para 3 clusters
modelo_produtos = KMeans(n_clusters=3, random_state=42, n_init=10)

# Treinar o modelo
modelo_produtos.fit(dados_produtos)

# Centros dos clusters = produtos âncora
produtos_ancora = modelo_produtos.cluster_centers_

print("Produtos Âncora encontrados:")
for i, prod in enumerate(produtos_ancora):
    print(f"Produto Âncora {i+1}: Preço = {prod[0]:.2f}, Popularidade = {prod[1]:.2f}")

