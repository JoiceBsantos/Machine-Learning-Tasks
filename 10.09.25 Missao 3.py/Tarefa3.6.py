# =================================================================================================================
# Exercício 6: O Vento Traiçoeiro
# Cenário: O ambiente agora é estocástico (imprevisível). Há uma chance de 30% de que a ação do agente falhe por causa
# de um "vento forte". Se a ação falhar, o agente não se move, mas ainda paga o custo de -1 ponto.
# Sua Missão:** Introduzir a aleatoriedade do ambiente na lógica de transição de estado.
# ==================================================================================================================


import numpy as np
import time

print("\n--- Exercício 6: O Vento Traiçoeiro ---")

posicao_agente = 0
objetivo = 9
recompensa_total = 0

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Tentando ir para '{acao}'")
    
    # TODO 1: Simula chance do vento
    vento_soprou = np.random.rand() < 0.3

    # TODO 2: Movimento com vento
    if vento_soprou:
        print("!! O vento soprou! O agente não se moveu.")
    else:
        if acao == 'direita':
            posicao_agente += 1
        else:
            posicao_agente -= 1
        posicao_agente = np.clip(posicao_agente, 0, 9)

    # TODO 3: Recompensa
    if posicao_agente == objetivo:
        recompensa_total += 50
        print(">> Objetivo alcançado! Recompensa +50")
        break
    else:
        recompensa_total -= 1
        print(f"   Recompensa do passo: -1, total acumulado: {recompensa_total}")
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")
