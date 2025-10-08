# Cada exercício foca em um conceito fundamental do design de ambientes de RL.
# Eles são projetados para serem resolvidos em sequência, construindo o conhecimento passo a passo.
# O objetivo é que os alunos implementem a lógica do ambiente, que é o primeiro passo para dominar o RL.

# Instruções para os Alunos
# Para cada exercício, você receberá um cenário e um código-fonte com seções marcadas como # TODO.
# Sua missão é preencher essas seções para que a simulação funcione de acordo com as regras descritas.
# No final de cada exercício, a solução completa é fornecida para sua referência.

# Exercício Introdutório: Identificando os Componentes de RL em um Novo Cenário
# Objetivo: Consolidar a compreensão dos conceitos fundamentais do Aprendizado por Reforço (Agente, Ambiente, Estado, Ação, Recompensa, Política e Função de Valor) em um contexto diferente do labirinto.
# Cenário:Imagine que você está construindo um sistema de IA para ensinar um robô-aspirador a limpar eficientemente uma casa. O robô se move em diferentes cômodos, encontra sujeira e, eventualmente, precisa retornar à sua base para recarregar.
# Tarefa:Para este cenário do robô-aspirador, identifique e descreva cada um dos seguintes componentes de Aprendizado por Reforço:
# Agente:
# Ambiente:
# Estado (exemplifique alguns estados possíveis):
# Ação (exemplifique algumas ações possíveis):
# Recompensa (sugira algumas recompensas positivas e negativas):
# Política (descreva brevemente o que uma política representaria aqui):
# Função de Valor Q (o que ela tentaria estimar neste contexto?):

#EXERCICIOS PADRÕES
# Setup Inicial (para todos os exercícios):
# Crie um arquivo Python e instale a biblioteca NumPy:
# pip install numpy
#
# ---

# ### **Exercício 1: O Corredor Simples**

# **Cenário:** O exercício mais básico possível. 
# Um agente está em um corredor de 7 posições (0 a 6) e quer chegar ao final. 
# Ele só pode se mover para frente.

# **Sua Missão:** Implementar a lógica de movimento e a recompensa final.


# ===================================================================================================
# Exercício 1: O Corredor - Cenário:O exercício mais básico possível. Um agente está em um corredor de 
# 7 posições (0 a 6) e quer chegar ao final. Ele só pode se mover para frente.
#Sua Missão:** Implementar a lógica de movimento e a recompensa final.
# ===================================================================================================


import time

print("\n--- Exercício 1: O Corredor ---")

posicao_agente = 0
objetivo = 6
recompensa_total = 0

for passo in range(10):
    print(f"Passo {passo + 1}: Posição atual = {posicao_agente}")
    
    # TODO 1: Atualize a 'posicao_agente' para que ele avance 1 passo.
    posicao_agente += 1

    # TODO 2: Verifique se o agente alcançou o 'objetivo'.
    if posicao_agente == objetivo:
        print(" >> Objetivo alcançado!")
        recompensa_total += 10  # recompensa ao chegar no objetivo
        break
    else:
        # Se não chegou, ele perde 1 ponto de 'recompensa_total' pelo esforço.
        recompensa_total -= 1

    time.sleep(0.5)

print(f"Simulação finalizada! Recompensa total: {recompensa_total}")
