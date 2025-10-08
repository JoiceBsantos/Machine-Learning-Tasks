# ========================================================================================================
# Exercício 4: Tarefa: Classificar Veículo
# ========================================================================================================

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("\n🚗 --- Classificar Veículo --- 🏍️🚚")

# --- Dados de treino ---
dados_veiculos = np.array([
    [150, 2],    # Moto leve
    [1500, 4],   # Carro pequeno
    [8000, 6],   # Caminhão
    [180, 2],    # Moto
    [2000, 4],   # Carro médio
    [10000, 8]   # Caminhão pesado
])
tipo_veiculo = np.array([0, 1, 2, 0, 1, 2])  # 0=Moto, 1=Carro, 2=Caminhão

# --- Treinamento ---
modelo_veiculo = KNeighborsClassifier(n_neighbors=3)
modelo_veiculo.fit(dados_veiculos, tipo_veiculo)

# --- Entrada interativa ---
while True:
    try:
        print("\nDigite as informações do veículo para classificar (ou 'sair' para encerrar):")
        peso_input = input("Peso do veículo em kg: ")
        if peso_input.lower() == 'sair':
            print("\n👋 Encerrando a classificação. Até mais!")
            break

        rodas_input = input("Número de rodas: ")
        if rodas_input.lower() == 'sair':
            print("\n👋 Encerrando a classificação. Até mais!")
            break

        peso = float(peso_input)
        rodas = int(rodas_input)

        # --- Previsão ---
        veiculo_novo = np.array([[peso, rodas]])
        previsao_veiculo = modelo_veiculo.predict(veiculo_novo)
        mapa_veiculos = {0: '🏍️ Moto', 1: '🚗 Carro', 2: '🚚 Caminhão'}
        resultado_veiculo = mapa_veiculos[previsao_veiculo[0]]

        print(f"\n🔍 Um veículo de [{peso} kg, {rodas} rodas] foi classificado como: {resultado_veiculo}")
    except ValueError:
        print("⚠️ Entrada inválida! Digite valores numéricos válidos para peso e número de rodas.")
