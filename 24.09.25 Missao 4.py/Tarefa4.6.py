# ==============================================================================================
# Exercício 6: Tarefa: Criar uma árvore de decisão para diagnosticar se um paciente tem 'Gripe' 
# ou 'Resfriado' com base na febre e na intensidade da tosse.
# ==============================================================================================

import numpy as np
from sklearn.tree import DecisionTreeClassifier

print("\n--- 3.3: Exercício - Diagnóstico Médico 🩺 ---")

# Dados de treinamento: [Febre, Tosse]
sintomas = np.array([
    [1, 1],
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1],
    [0, 0]
])
diagnostico = np.array([1, 0, 0, 0, 1, 0])  # 1 = Gripe, 0 = Resfriado

# Treinamento do modelo
modelo_saude = DecisionTreeClassifier(random_state=42)
modelo_saude.fit(sintomas, diagnostico)

# Entrada interativa 
febre = int(input("O paciente está com febre? (1 = Sim, 0 = Não): "))
tosse = int(input("O paciente está com tosse forte? (1 = Sim, 0 = Não): "))

novo_paciente = np.array([[febre, tosse]])
previsao_saude = modelo_saude.predict(novo_paciente)

mapa_diagnostico = {0: '🤧 Resfriado', 1: '🤒 Gripe'}
resultado_saude = mapa_diagnostico[previsao_saude[0]]

print(f"\nDiagnóstico para [Febre={'Sim' if febre else 'Não'}, Tosse={'Forte' if tosse else 'Leve/Não'}]: {resultado_saude}")
