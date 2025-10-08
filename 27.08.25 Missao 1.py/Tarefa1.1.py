# TAREFAS DE APRENDIZADO SUPERVISIONADO 


# =============================================================================
# TAREFA 1: Treine o modelo abaixo colocando mais 4 conjuntos de dados
# =============================================================================

# Para começar, instale a biblioteca (no terminal):
# pip install scikit-learn

import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Função de pré-processamento
def limpar_texto(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    texto = re.sub(r'\d+', '', texto)  # Remove números
    texto = texto.strip()  # Remove espaços extras
    return texto

# 1. Conjunto de dados (mensagens + rótulos)
mensagens = [
    "Quero fazer um pedido",
    "Preciso falar com o suporte",
    "Quais promoções vocês têm hoje?",
    "Qual o horário de funcionamento?",
    "Meu produto veio com defeito",
    "Posso pagar com cartão de crédito?",
    "Gostaria de cancelar meu pedido",
    "Vocês fazem entrega?",
    "Tem desconto para pagamento à vista?",
    "Não consigo acessar minha conta"
]

rotulos = [ "pedido", "suporte","promoção","informação","suporte","pagamento",
           "cancelamento","entrega","promoção","suporte"]

# 2. Pré-processamento das mensagens
mensagens_limpas = [limpar_texto(m) for m in mensagens]

# 3. Vetorização (transforma texto em números)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens_limpas)

# 4. Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, rotulos)
print("Modelo treinado com sucesso!")
print(f"Total de mensagens de treinamento: {len(mensagens)}")

# 5. Teste do modelo
print("\n--- Teste do Modelo ---")
testes = [
    "Quero comprar algo",
    "Preciso de ajuda urgente",
    "Tem cupom de desconto?",
    "Qual o horário da loja?",
    "Meu produto quebrou"
]

for teste in testes:
    teste_limpo = limpar_texto(teste)
    X_teste = vectorizer.transform([teste_limpo])
    predicao = modelo.predict(X_teste)
    print(f"'{teste}' -> Intenção: {predicao[0]}")

# 6. Interação com o usuário
print("\n--- Interação Interativa ---")
while True:
    nova_mensagem = input("\nDigite uma mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        break
    nova_mensagem_limpa = limpar_texto(nova_mensagem)
    X_novo = vectorizer.transform([nova_mensagem_limpa])
    predicao = modelo.predict(X_novo)
    print(f"Intenção prevista: {predicao[0]}")

