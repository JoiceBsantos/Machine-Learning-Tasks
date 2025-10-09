# ======================================================================================================================
#Exercício 1 – Prevendo Preços de Imóveis (Regressão Linear)
# ======================================================================================================================
#Missão: Treinar um modelo de Machine Learning com os dados de treino.
#As variáveis abaixo já existem e estão prontas para serem usadas:
#- X_treino_final: As características (tamanho, quartos, cidade) dos imóveis de treino, já limpas e transformadas.
#- y_treino: Os preços reais dos imóveis de treino.
#- X_teste_final: As características dos imóveis de teste, que o modelo nunca viu.
#- y_teste: Os preços reais dos imóveis de teste. Usaremos isso no final para comparar com as previsões do nosso modelo.
# ======================================================================================================================

# --- Bloco de Código do Exercício ---
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# --- Início do Bloco de Contexto (não precisa alterar) ---
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

dados = {
    'tamanho_m2': [50, 70, 100, 120, 65, np.nan, 95, 88, 110, 150],
    'n_quartos': [1, 2, 3, 3, 2, 2, 3, 2, 3, 4],
    'cidade': ['SP', 'RJ', 'SP', 'BH', 'RJ', 'SP', 'BH', 'RJ', 'SP', 'BH'],
    'preco': [150000, 210000, 300000, 350000, 190000, 180000, 280000, 250000, 320000, 450000]
}
df = pd.DataFrame(dados)

imputer = SimpleImputer(strategy='mean')
df['tamanho_m2'] = imputer.fit_transform(df[['tamanho_m2']])

X = df.drop('preco', axis=1)
y = df['preco']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

colunas_numericas = ['tamanho_m2', 'n_quartos']
colunas_categoricas = ['cidade']

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_treino_cat = encoder.fit_transform(X_treino[colunas_categoricas])
X_teste_cat = encoder.transform(X_teste[colunas_categoricas])

scaler = StandardScaler()
X_treino_num = scaler.fit_transform(X_treino[colunas_numericas])
X_teste_num = scaler.transform(X_teste[colunas_numericas])

X_treino_final = np.hstack([X_treino_num, X_treino_cat])
X_teste_final = np.hstack([X_teste_num, X_teste_cat])
# --- Fim do Bloco de Contexto ---

# --- INÍCIO DO TRABALHO ---
# 1. Crie uma instância do modelo de Regressão Linear
modelo_preco_casas = LinearRegression()  # SEU CÓDIGO AQUI

# 2. Treine o modelo com os dados de TREINO
modelo_preco_casas.fit(X_treino_final, y_treino)  # SEU CÓDIGO AQUI
print("Modelo treinado com sucesso!")

# 3. Faça previsões nos dados de TESTE
previsoes = modelo_preco_casas.predict(X_teste_final)  # SEU CÓDIGO AQUI

print("\n--- Resultados da Avaliação ---")
for i in range(len(previsoes)):
    print(f"Imóvel {i+1}: Preço Real = R${y_teste.iloc[i]:.2f} | Previsão do Modelo = R${previsoes[i]:.2f}")

# 4. Avalie a performance do modelo
mae = mean_absolute_error(y_teste, previsoes)  # SEU CÓDIGO AQUI
r2 = r2_score(y_teste, previsoes)  # SEU CÓDIGO AQUI

print(f"\nErro Absoluto Médio (MAE): R$ {mae:.2f}")
print(f"Score R²: {r2:.2f}")
# --- FIM DO SEU TRABALHO ---


