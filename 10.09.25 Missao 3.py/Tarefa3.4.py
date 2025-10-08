# =================================================================================================================
# Exercício 4: O Chão de Lava
# Cenário: Algumas posições no corredor são "quentes" (chão de lava) e dão uma penalidade maior ao agente.
# Sua Missão: Implementar uma recompensa de passo que depende do estado (posição) do agente.
# ==================================================================================================================

import numpy as np
import time

print("\n--- Exercício 4: O Chão de Lava ---")

posicao_agente = 0
objetivo = 9
chao_de_lava = [3, 4, 5]
recompensa_total = 0

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")

    # Movimento do agente
    if acao == 'direita':
        posicao_agente += 1
    else:
        posicao_agente -= 1

    # Limites do corredor
    posicao_agente = np.clip(posicao_agente, 0, 9)

    # Verifica se chegou no objetivo
    if posicao_agente == objetivo:
        recompensa_total += 50
        print(">> Objetivo alcançado! Recompensa +50")
        break
    else:
        # Recompensa variável por estado
        if posicao_agente in chao_de_lava:
            recompensa_passo = -5
            print("   !! Chão de lava! Recompensa -5")
        else:
            recompensa_passo = -1
            print("   Recompensa do passo: -1")
        recompensa_total += recompensa_passo

    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")
