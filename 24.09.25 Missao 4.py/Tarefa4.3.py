# ========================================================================================================
# Exercício 3: Tarefa: Crie um modelo KNN que classifica se um aluno foi aprovado (1) ou reprovado (0) 
# com base em duas notas.
# ========================================================================================================

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("\n--- 2.2: Exercício - Aprovado/Reprovado ---")
notas_alunos = np.array([[8, 7], [5, 4], [9, 8], [4, 2], [7, 9], [3, 5]])
situacao = np.array([1, 0, 1, 0, 1, 0])

modelo_alunos = KNeighborsClassifier(n_neighbors=3)
# Aqui eu digo para ele usar os 3 mais próximos para classificar
modelo_alunos.fit(notas_alunos, situacao)
aluno_novo = np.array([[6, 7]])
previsao_aluno = modelo_alunos.predict(aluno_novo)
resultado_aluno = "Aprovado" if previsao_aluno[0] == 1 else "Reprovado"
print(f"Um aluno com notas [6, 7] foi classificado como: {resultado_aluno}")