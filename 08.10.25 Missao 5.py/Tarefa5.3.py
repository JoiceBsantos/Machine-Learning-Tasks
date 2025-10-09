# ========================================================================================================
#Exercício 3 – Detecção de Churn de Clientes (Classificação)
# ========================================================================================================
#Cenário: Você trabalha para uma empresa de telecomunicações. A diretoria está preocupada com a perda de 
#clientes (o chamado "churn"). Sua missão é construir um modelo que preveja se um cliente está prestes a 
#cancelar seu plano, com base em seu perfil e uso do serviço.
#Tipo: Classificação, pois o alvo (Churn) é uma categoria binária (Sim ou Nao).
#Desafio: Complete o esqueleto de código abaixo para treinar e avaliar um modelo de detecção de churn.
# ========================================================================================================


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# --- 2. DATASET ---
data = {
    'Idade': [25, 45, 35, 50, 22, 55, 41, 28, 33, 60, 39, 48, 29, 52, 31, 65, 27, 38, 43, 58],
    'Plano_Mensal': [70, 95, 80, 105, 50, 110, 90, 65, 75, 115, 85, 100, 72, 108, 78, 120, 68, 82, 92, 112],
    'Meses_Contrato': [1, 24, 12, 36, 2, 48, 18, 5, 8, 60, 15, 30, 3, 40, 6, 55, 4, 10, 22, 50],
    'Tipo_Contrato': ['Mensal', 'Anual', 'Mensal', 'Dois anos', 'Mensal', 'Dois anos', 'Anual', 'Mensal', 'Mensal', 'Dois anos', 'Anual', 'Dois anos', 'Mensal', 'Dois anos', 'Mensal', 'Dois anos', 'Mensal', 'Anual', 'Anual', 'Dois anos'],
    'Suporte_Tecnico': ['Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Nao', 'Sim', 'Sim', 'Nao', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Sim', 'Nao', 'Nao'],
    'Churn': ['Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Sim', 'Sim', 'Nao', 'Nao', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Nao']
}
df_churn = pd.DataFrame(data)
df_churn.loc[3, 'Plano_Mensal'] = np.nan

# --- 3. PREPARAÇÃO DOS DADOS ---
X = df_churn.drop('Churn', axis=1)  
y = df_churn['Churn']               

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25, random_state=42)  

colunas_numericas = ['Idade', 'Plano_Mensal', 'Meses_Contrato']
colunas_categoricas = ['Tipo_Contrato', 'Suporte_Tecnico']

pipeline_numerico = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler())])
pipeline_categorico = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(transformers=[('num', pipeline_numerico, colunas_numericas),
                                               ('cat', pipeline_categorico, colunas_categoricas)])

# 4. TREINAMENTO DO MODELO
modelo_cla = LogisticRegression(max_iter=1000) 
pipeline_final_cla = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', modelo_cla)])

pipeline_final_cla.fit(X_treino, y_treino)  
print("\n Modelo de Classificação treinado com sucesso!")

# 5. AVALIAÇÃO DO MODELO
previsoes_churn = pipeline_final_cla.predict(X_teste)  
acuracia = accuracy_score(y_teste, previsoes_churn)    
relatorio = classification_report(y_teste, previsoes_churn)
matriz_conf = confusion_matrix(y_teste, previsoes_churn)

print("\n--- Resultados da Avaliação (Classificação) ---")
print(f"Acurácia: {acuracia*100:.2f}%")
print("\nRelatório de Classificação:")
print(relatorio)

# Visualização da Matriz de Confusão
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_conf, annot=True, fmt='d', cmap='Blues', xticklabels=['Nao Churn', 'Churn'], yticklabels=['Nao Churn', 'Churn'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

