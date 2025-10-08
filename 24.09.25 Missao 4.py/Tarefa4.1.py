
# ===================================================================================================
# Exercício 1:Prever Pontuação em Jogo
# Tarefa: Criar um modelo que prevê a pontuação final de um jogador com base no número de horas que ele jogou.
# ===================================================================================================

import numpy as np
from sklearn.linear_model import LinearRegression

print("\n--- 1.2: Exercício - Prever Pontuação ---")
horas_jogadas = np.array([1, 3, 5, 8, 10]).reshape(-1, 1)
# Aqui a função "reshape" vai transformar cada número em uma nova lista
pontuacao_final = np.array([10, 25, 60, 90, 110])

modelo_pontuacao = LinearRegression()
modelo_pontuacao.fit(horas_jogadas, pontuacao_final)
horas_novas = np.array([[7]])
pontuacao_prevista = modelo_pontuacao.predict(horas_novas)
print(f"Para 7 horas jogadas, a pontuação prevista é de {pontuacao_prevista[0]:.0f} mil pontos.")