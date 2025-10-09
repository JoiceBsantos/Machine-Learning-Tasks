# =====================================================================================================
#Exercício 2 – Prevendo Preço de Carros Usados (Regressão)
# =====================================================================================================
#Cenário: Sua tarefa é criar um modelo que estime o preço de venda de um carro usado com base em suas 
#características, para ajudar os vendedores a precificarem seus anúncios de forma justa.
#Tipo: Regressão, pois o alvo (Preco) é um valor numérico contínuo.
#Desafio: Complete o esqueleto de código abaixo para treinar e avaliar um modelo de previsão de preços.
# =====================================================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# --- 2. DATASET ---
data = {
    'Ano': [2018, 2015, 2019, 2020, 2017, 2014, 2018, 2016, 2021, 2013, 2019, 2017, 2015, 2020, 2018, 2016, 2022, 2014, 2019, 2017],
    'Quilometragem': [50000, 120000, 30000, 15000, 70000, 150000, 60000, 95000, 5000, 180000, 40000, 80000, 110000, 20000, 55000, 105000, 2000, 160000, 35000, 75000],
    'Potencia_Motor': [1.6, 2.0, 1.0, 1.4, 1.8, 2.0, 1.6, 1.8, 1.0, 2.2, 1.4, 1.6, 2.0, 1.0, 1.8, 2.0, 1.2, 2.2, 1.4, 1.8],
    'Tipo_Combustivel': ['Flex', 'Gasolina', 'Flex', 'Flex', 'Gasolina', 'Diesel', 'Flex', 'Gasolina', 'Flex', 'Diesel', 'Flex', 'Flex', 'Gasolina', 'Flex', 'Gasolina', 'Diesel', 'Flex', 'Diesel', 'Flex', 'Gasolina'],
    'Cambio': ['Manual', 'Automatico', 'Manual', 'Manual', 'Automatico', 'Manual', 'Automatico', 'Automatico', 'Manual', 'Automatico', 'Manual', 'Manual', 'Automatico', 'Manual', 'Automatico', 'Automatico', 'Manual', 'Automatico', 'Manual', 'Automatico'],
    'Preco': [45000, 38000, 55000, 65000, 52000, 35000, 48000, 46000, 75000, 32000, 58000, 50000, 40000, 68000, 53000, 44000, 82000, 30000, 60000, 51000]
}
df_carros = pd.DataFrame(data)
df_carros.loc[5, 'Quilometragem'] = np.nan
df_carros.loc[11, 'Potencia_Motor'] = np.nan

# --- 3. PREPARAÇÃO DOS DADOS ---
X = df_carros.drop('Preco', axis=1)  # SEU CÓDIGO AQUI
y = df_carros['Preco']               # SEU CÓDIGO AQUI

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)  # SEU CÓDIGO AQUI

colunas_numericas = ['Ano', 'Quilometragem', 'Potencia_Motor']
colunas_categoricas = ['Tipo_Combustivel', 'Cambio']

pipeline_numerico = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
pipeline_categorico = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(transformers=[('num', pipeline_numerico, colunas_numericas),
                                               ('cat', pipeline_categorico, colunas_categoricas)])

# 4. TREINAMENTO DO MODELO
modelo_reg = LinearRegression()  # SEU CÓDIGO AQUI
pipeline_final_reg = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', modelo_reg)])

pipeline_final_reg.fit(X_treino, y_treino)  # SEU CÓDIGO AQUI
print("\n Modelo de Regressão treinado com sucesso!")

# 5. AVALIAÇÃO DO MODELO
previsoes_preco = pipeline_final_reg.predict(X_teste)  # SEU CÓDIGO AQUI

mae = mean_absolute_error(y_teste, previsoes_preco)  # SEU CÓDIGO AQUI
r2 = r2_score(y_teste, previsoes_preco)             # SEU CÓDIGO AQUI

print("\n--- Resultados da Avaliação (Regressão) ---")
print(f"Erro Absoluto Médio (MAE): R$ {mae:.2f}")
print(f"Score R²: {r2:.2f}")

# Visualização
plt.figure(figsize=(10, 6))
plt.scatter(y_teste, previsoes_preco)
plt.plot([y_teste.min(), y_teste.max()], [y_teste.min(), y_teste.max()], '--r', linewidth=2)
plt.xlabel("Preços Reais")
plt.ylabel("Preços Previstos")
plt.title("Preços Reais vs. Previsões do Modelo de Regressão")
plt.show()
