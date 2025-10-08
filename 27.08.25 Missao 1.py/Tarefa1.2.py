# TAREFAS DE APRENDIZADO SUPERVISIONADO 

# =============================================================================
# TAREFA 2: Classificador de mensagens para bot de atendimento acadêmico
# =============================================================================

# Para começar, instale a biblioteca (se ainda não tiver):
# pip install scikit-learn

import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Dataset (frases + rótulos)
frases = [
    "Quando começa a matrícula?",
    "Como posso me inscrever nas disciplinas?",
    "Quais são as datas de prova?",
    "Como acessar minhas notas?",
    "Onde fica a biblioteca?",
    "Quais eventos acadêmicos terão neste semestre?",
    "Posso renovar livros online?",
    "Como recuperar minha senha do portal?",
    "Quais são os horários de atendimento da secretaria?",
    "Tem bolsas de estudo disponíveis?"
]

rotulos = [
    "matricula",
    "matricula",
    "notas",
    "notas",
    "biblioteca",
    "eventos",
    "biblioteca",
    "acesso_portal",
    "informacao",
    "bolsa"
]

# 2. Pré-processamento sem função
frases_limpas = []
for f in frases:
    texto = f.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\d+', '', texto)
    texto = texto.strip()
    frases_limpas.append(texto)

# 3. Vetorização
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases_limpas)

# 4. Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, rotulos)

print("Modelo de atendimento acadêmico treinado com sucesso!")

# 5. Teste automático
teste = [
    "Quero me inscrever em uma disciplina",
    "Como vejo minhas notas?",
    "Onde posso pegar livros na biblioteca?",
    "Quando serão os próximos eventos?",
    "Existe bolsa de estudo para meu curso?"
]

for msg in teste:
    texto = msg.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\d+', '', texto)
    texto = texto.strip()
    X_teste = vectorizer.transform([texto])
    pred = modelo.predict(X_teste)
    print(f"Mensagem: '{msg}' → Intenção prevista: {pred[0]}")

# 6. Interação com o usuário
while True:
    nova_mensagem = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        print("Encerrando o bot.")
        break
    texto = nova_mensagem.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\d+', '', texto)
    texto = texto.strip()
    X_novo = vectorizer.transform([texto])
    predicao = modelo.predict(X_novo)
    print(f" Intenção prevista: {predicao[0]}")
