# ===================================================================================================
# TAREFA 1:  -  Aprendizado Supervisionado – Aprender com Respostas - "No aprendizado supervisionado, 
# nós damos ao modelo as perguntas (dados) e as respostas (rótulos) e ele precisa aprender a regra que 
# os conecta. Pense em um gabarito de prova."
# ===================================================================================================


import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("--- Exercício 1 - Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [nota_prova_1, nota_trabalho_2]
# Rótulos: 0 = Reprovou, 1 = Passou
X_treino = np.array([
    [8, 9], [7, 8], [9, 10], [8, 7],   # Passou
    [4, 5], [3, 6], [5, 4], [2, 3]     # Reprovou
])
y_treino = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Criar o modelo KNN
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# Treinar o modelo
modelo_knn.fit(X_treino, y_treino)

# Testar com novos alunos
aluno_A = np.array([[9, 8]])  # Esperamos que passe (1)
aluno_B = np.array([[3, 4]])  # Esperamos que reprove (0)

# Fazer previsões
previsao_A = modelo_knn.predict(aluno_A)
previsao_B = modelo_knn.predict(aluno_B)

# Mostrar resultados
print(f"Dados de treino (Notas): \n{X_treino}")
print(f"Rótulos de treino (Situação): {y_treino}")
print("-" * 20)
print(f"Previsão para o Aluno A: {'Passou' if previsao_A[0] == 1 else 'Reprovou'}")
print(f"Previsão para o Aluno B: {'Passou' if previsao_B[0] == 1 else 'Reprovou'}")
print("-" * 50, "\n")
