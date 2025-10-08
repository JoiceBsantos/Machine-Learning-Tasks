# =================================================================================================================
# Exercício 2: O Agente Indeciso - Cenário: Agora o agente pode se mover para 'esquerda' ou 'direita' em um 
# corredor de 10 posições (0 a 9). Ele não pode atravessar as paredes (posições < 0 ou > 9).Sua Missão: Implementar 
# a lógica de movimento para ambas as direções e garantir que o agente permaneça dentro dos limites do corredor.
# ==================================================================================================================

import numpy as np
import time

print("\n--- Exercício 2: O Agente Indeciso ---")

posicao_agente = 5
objetivo = 9
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    # TODO 1: Atualiza posição com base na ação
    if acao == 'direita':
        posicao_agente += 1
    elif acao == 'esquerda':
        posicao_agente -= 1

    # TODO 2: Garante limites do corredor (0 a 9)
    posicao_agente = max(0, min(posicao_agente, 9))

    # TODO 3: Verifica se chegou no objetivo
    if posicao_agente == objetivo:
        print(" >> Objetivo alcançado!")
        recompensa_total += 20
        break
    else:
        recompensa_total -= 1  # custo do passo

    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")


