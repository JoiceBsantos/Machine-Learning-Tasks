# ===============================================================================================================
# Exercício 2: Tarefa: Você tem dados da temperatura em uma cidade com base na altitude (em metros). 
# Crie um modelo para prever a temperatura a 2500 metros.
# ===============================================================================================================


import numpy as np
from sklearn.linear_model import LinearRegression

print("\n--- 1.3: Exercício - Prever Temperatura ---")
altitudes = np.array([500, 1000, 1500, 2000, 3000]).reshape(-1, 1)
temperaturas = np.array([25, 20, 15, 10, 5])

modelo_temp = LinearRegression()
modelo_temp.fit(altitudes, temperaturas)
altitude_nova = np.array([[2500]])
temp_prevista = modelo_temp.predict(altitude_nova)
print(f"A temperatura prevista a 2500 metros é de {temp_prevista[0]:.1f}°C.")
