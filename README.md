# Projeto de Machine Learning - Aplicações Práticas

Este repositório reúne diversas implementações de aprendizado de máquina, explorando técnicas **supervisionadas** e **não supervisionadas** em Python com auxílio do scikit-learn.

---

## 📋 Sobre o Projeto

O objetivo deste projeto é apresentar **soluções práticas** com algoritmos de ML para problemas reais, incluindo:

- **Aprendizado supervisionado:** classificação e regressão de dados  
- **Aprendizado não supervisionado:** clusterização e identificação de padrões  
- **Processamento de Linguagem Natural (NLP):** análise e categorização de textos  
- **Previsão de métricas e resultados:** estimativas de tempo e desempenho
  
---

# 📚 Tarefas Executadas nas Missões 1 a 4
## Missão 1 – Fundamentos de Machine Learning
- Exploração de conceitos básicos de ML e tipos de aprendizado:
  - Aprendizado Supervisionado (regressão e classificação)
  - Aprendizado Não Supervisionado (agrupamento e detecção de anomalias)
  - Aprendizado por Reforço (loop Ação → Recompensa)
- Implementação de exemplos simples usando Python e scikit-learn.
- Simulações de agentes em ambientes discretos.

## Missão 2 – Aprendizado Supervisionado e Reforço
- **Aprendizado Supervisionado**
  - KNN: prever aprovação de alunos com base em notas.
  - Regressão Linear: prever preço de imóveis com base em área e número de quartos.
- **Aprendizado Não Supervisionado**
  - KMeans: identificar clusters de clientes e detectar transações anômalas.
- **Aprendizado por Reforço**
  - Simulação do agente “Comilão” que aprende a alcançar a comida em um ambiente linear.
  - Ciclo de interação: Ação → Recompensa → Atualização de estado.

## 🚀 Missão 3 – Ambientes de Reforço com Condições Variadas
- Cenários progressivos para um agente:
  - Corredor simples: movimento para frente, recompensa ao objetivo.
  - Agente indeciso: movimento aleatório para esquerda/direita.
  - Caminho perigoso: buraco com penalidade de -50 pontos.
  - Chão de lava: penalidade variável por posição.
  - Robô com bateria: condição de término por energia.
  - Vento traiçoeiro: ação estocástica com falha possível.
- Desenvolvimento de lógica de movimento, limites, recompensas e penalidades.
- Experimentos com aleatoriedade e estados adicionais (energia, obstáculos).


## Missão 4 – Modelos Supervisionados e Classificação Interativa
- **Regressão Linear**
  - Previsão de pontuação em jogo e temperatura com base em variáveis contínuas.
- **K-Nearest Neighbors (KNN)**
  - Classificação de alunos aprovados/reprovados.
  - Classificação de veículos (Moto, Carro, Caminhão) com entrada interativa do usuário.
- **Árvores de Decisão**
  - Aprovação de empréstimos com base em renda e casa própria.
  - Diagnóstico médico (Gripe ou Resfriado) baseado em febre e tosse.
- Aplicação prática de modelos supervisionados com dados contínuos e categóricos.
- Desenvolvimento de interatividade e previsão para novos dados.
---
## 🛠️ Tecnologias Utilizadas

- **Python 3.x**  
- **scikit-learn**: modelos de aprendizado de máquina  
- **NumPy**: cálculos e manipulação de dados  
- **Regex**: processamento de texto

---
## 📚 Bibliotecas Principais
```python
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import time
from sklearn.tree import DecisionTreeClassifier
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
```


## **📁 Estrutura do Projeto**
```plaintext
ML-CHATBOT/
├── 03.09.25 Missao 2.py
├── 10.09.25 Missao 3.py
├── 24.09.25 Missao 4.py
├── 27.08.25 Missao 1.py
└── README.md
```
## 🚀 Como Executar
**1. Clone o repositório:**
```
git clone https://github.com/JoiceBsantos/Machine-Learning-Tasks.git
cd Machine-Learning-Tasks
```
**2. Instalar dependências :**
```
pip install scikit-learn numpy
```
**3. Execute o arquivo principal:**

Cada missão está em um arquivo Python separado. Execute o arquivo desejado:

```bash
python "27.08.25 Missao 1.py"  # Missão 1
python "03.09.25 Missao 2.py"  # Missão 2
python "10.09.25 Missao 3.py"  # Missão 3
python "24.09.25 Missao 4.py"  # Missão 4
```
### 🎯 **Resultados de Aprendizagem Obtidos**
- Compreensão dos principais algoritmos de **Machine Learning supervisionado, não supervisionado e por reforço**.  
- Desenvolvimento de habilidades práticas em **Python e scikit-learn**.  
- Capacidade de **criar, treinar e avaliar modelos** com base em dados reais e simulados.  
- Entendimento do **processo de tomada de decisão automatizada**, ajustando parâmetros e interpretando previsões.  
- Aprendizado sobre **interatividade, testes e experimentação** de modelos em diferentes contextos (educacional, financeiro, médico e ambiental).  


