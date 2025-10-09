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

## Missão 5 – Modelagem Preditiva e Classificação Aplicada

- Desenvolvimento de modelos de **Regressão Linear** para prever o **preço de imóveis e carros usados**, utilizando variáveis numéricas e categóricas.  
- Implementação de **pipelines com pré-processamento automático**, incluindo normalização e codificação de dados.  
- Criação de um modelo de **Classificação (Churn)** com **Regressão Logística** para identificar clientes com risco de cancelamento.  
- Avaliação dos modelos com **MAE, R², Acurácia e Matriz de Confusão**, além de visualizações gráficas comparando resultados reais e previstos.  

---
## 🛠️ Tecnologias Utilizadas

- **Python 3.x** – Linguagem principal para desenvolvimento dos modelos  
- **scikit-learn**
  - Modelos de aprendizado de máquina 
  – Criação e avaliação de modelos de regressão e classificação  
  - `LinearRegression`, `LogisticRegression`  
  - `train_test_split`, `ColumnTransformer`, `Pipeline`  
  - `OneHotEncoder`, `StandardScaler`, `SimpleImputer`  
  - Métricas: `mean_absolute_error`, `r2_score`, `accuracy_score`, `confusion_matrix`, `classification_report`
- **Pandas** – Manipulação e análise de dados tabulares  
- **NumPy** – Operações numéricas e vetorização , cálculos e manipulação de dados
- **Regex** - processamento de texto
- **Matplotlib** – Visualização de comparativos entre valores reais e previstos  
- **Seaborn** – Exibição gráfica da matriz de confusão  

---
## 📚 Bibliotecas Principais

```python
import numpy as np
import pandas as pd
import time
import re
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    accuracy_score,
    confusion_matrix,
    classification_report
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
```

## **📁 Estrutura do Projeto**
```plaintext
ML-CHATBOT/
├── 03.09.25 Missao 2.py
├── 08.10.25 Missao 5.py
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
python "08.10.25 Missao 5.py"  # Missão 5
```
### 🎯 **Resultados de Aprendizagem Obtidos**
- Compreensão dos principais algoritmos de **Machine Learning supervisionado, não supervisionado e por reforço**.  
- Desenvolvimento de habilidades práticas em **Python e scikit-learn**.  
- Capacidade de **criar, treinar e avaliar modelos** com base em dados reais e simulados.  
- Entendimento do **processo de tomada de decisão automatizada**, ajustando parâmetros e interpretando previsões.  
- Aprendizado sobre **interatividade, testes e experimentação** de modelos em diferentes contextos (educacional, financeiro, médico e ambiental).
- Aplicação prática de **regressão e classificação**, uso de **pipelines**, **métricas de desempenho** e **visualização de resultados** em contextos reais.
  
---
## 🤝 Contribuindo  

Este projeto foi desenvolvido como parte de um estudo prático em **Aprendizado de Máquina**, com foco em **aplicações reais e experimentação de algoritmos**.  
Sinta-se à vontade para contribuir com melhorias, como:  

- 🧠 **Aprimorar os modelos e algoritmos existentes**  
- 📊 **Adicionar novos conjuntos de dados e testes experimentais**  
- 🧹 **Melhorar o pré-processamento e tratamento dos dados**  
- ⚙️ **Implementar métricas de avaliação e visualizações adicionais**  
- 📈 **Explorar novas abordagens de aprendizado supervisionado, não supervisionado e por reforço**  

---

## 📝 Licença  

Este projeto tem **fins educacionais** e é **de código aberto**, podendo ser utilizado livremente para estudo, aprimoramento e pesquisa.  

---

## 👩‍💻 Autoria  

Criado e mantido por **Joice Barbosa**, em colaboração com **mais quatro colegas de classe**. Este projeto é **acadêmico** e foi desenvolvido durante as aulas de **Machine Learning**, ministradas pelo professor **[Flávio Santarelli](https://github.com/PROFSANTARELLI)**.  



