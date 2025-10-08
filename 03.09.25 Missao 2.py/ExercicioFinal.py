#==============================================================================
# EXERCICIO FINAL DA MISSÃO 2 - APRENDIZADO POR REFORÇO
# Imagine que você está ensinando um Doguinho a buscar um petisco. Você não escreve um manual de instruções para ele. Em vez disso, o processo é interativo:
# 
# 1 - O cachorro (o Agente) está em um ambiente (a sala). Ele decide fazer uma Ação (andar para frente).
# 2 - Você dá um Feedback (a Recompensa). Se ele chegou mais perto do petisco, você diz "Bom garoto!" (recompensa positiva).
# 3 - Se ele foi para longe, você não diz nada (recompensa neutra ou negativa, como o custo de energia).
# 4 - O cachorro recebe esse feedback e atualiza o seu "entendimento" sobre qual ação é boa naquela situação.
# 5 - Ele repete esse ciclo de Ação -> Recompensa várias vezes. Depois de muitas tentativas e erros, o cachorro aprende a sequência de ações ideal para conseguir o petisco da forma mais rápida possível.

# O Aprendizado por Reforço é exatamente isso: um método de Machine Learning onde um agente aprende a tomar decisões em um ambiente para maximizar uma recompensa total ao longo do tempo.

# Exercício: Agente Comilão
# Cenário: Nosso agente está em uma linha com 5 posições (0, 1, 2, 3, 4).
# O Agente: Um programa que só pode se mover para a 'direita'.
# O Ambiente: O caminho de 5 posições.
# O Objetivo: Chegar na Comida, que está na posição 4.

# Regras de Recompensa:
# +20 pontos: Se o agente chegar na Comida.
# -1 ponto: Para cada passo que o agente der (representa o custo de energia).
# 
# Sua Missão: Você vai preencher a lógica do ambiente. O agente sempre tentará se mover para a 'direita'. Você precisa atualizar a posição dele, verificar se ele alcançou a comida e calcular a recompensa a cada passo.
#==============================================================================

print("--- Exercício Final - Agente Comilão (Aprendizado por Reforço) ---\n")

# Configuração do ambiente
posicoes = 5           # Posições de 0 a 4
posicao_agente = 0     # Agente começa na posição 0
posicao_comida = 4     # Comida está na posição 4
recompensa_total = 0

# Loop do episódio
while posicao_agente < posicao_comida:
    print(f"Agente está na posição {posicao_agente}.")

    # Ação: mover para a direita
    posicao_agente += 1
    recompensa = -1  # custo do passo
    print(f"Agente se moveu para a posição {posicao_agente}, custo: {recompensa} ponto(s).")
    
    # Verifica se chegou na comida
    if posicao_agente == posicao_comida:
        recompensa += 20  # recompensa por alcançar o objetivo
        print(f"Agente alcançou a comida! Recompensa: +20 pontos!")

    # Atualiza a recompensa total
    recompensa_total += recompensa

print(f"\nRecompensa total acumulada pelo agente: {recompensa_total} pontos.")
