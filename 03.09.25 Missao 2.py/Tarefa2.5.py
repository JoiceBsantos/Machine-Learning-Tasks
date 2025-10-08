# ================================================================================
# TAREFA 5:  -   APRENDIZADO POR REFORÇO: O PERSONAGEM COMILÃO
# Objetivo: Entender o loop básico de interação do RL (Ação -> Recompensa).
# ================================================================================

import time

# --- CONFIGURAÇÃO DO AMBIENTE ---
POSICAO_COMIDA = 4
LINHA_TOTAL = 5  # Total de posições da linha

def visualizar_comilao(posicao_agente, recompensa_total):
    """Mostra a linha com o agente (🐶) e a comida (🍖)"""
    linha = ['-'] * LINHA_TOTAL
    if posicao_agente >= LINHA_TOTAL:
        posicao_agente = LINHA_TOTAL - 1
    linha[posicao_agente] = '🐶'   # Agente
    linha[POSICAO_COMIDA] = '🍖'   # Comida
    print(" ".join(linha) + f"   Recompensa: {recompensa_total}")

def simular_comilao_automatico(posicao_inicial=0, max_passos=10):
    posicao_agente = posicao_inicial
    recompensa_total = 0

    print("--- Simulação Automática do Agente Comilão ---\n")
    visualizar_comilao(posicao_agente, recompensa_total)
    print("-" * 30)

    for passo in range(max_passos):
        print(f"Passo {passo + 1}:")
        
        # Ação automática: mover sempre para a direita
        acao_agente = 'direita'
        print(f"   -> Ação do Agente: '{acao_agente}'")

        # Atualiza posição e calcula custo
        posicao_agente += 1
        recompensa = -1  # custo do passo

        # Verifica se chegou na comida
        if posicao_agente >= POSICAO_COMIDA:
            recompensa += 20
            print(f"🐶 Agente alcançou a comida! Recompensa extra: +20 pontos!")
            recompensa_total += recompensa
            visualizar_comilao(posicao_agente, recompensa_total)
            break

        # Atualiza recompensa total e mostra visualização
        recompensa_total += recompensa
        visualizar_comilao(posicao_agente, recompensa_total)

        time.sleep(0.5)

    print("-" * 30)
    print(f"Recompensa total acumulada pelo agente: {recompensa_total} pontos.\n")

# --- Executar simulação automática ---
simular_comilao_automatico()




      