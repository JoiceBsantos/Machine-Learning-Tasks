# TAREFAS DE APRENDIZADO NAO SUPERVISIONADO 

# =============================================================================
# TAREFA 5: Agrupar frases de chatbot de turismo usando KMeans
# =============================================================================


# Importa as bibliotecas necessárias para vetorização de texto e clustering
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


# 1. Dataset: frases de um chatbot de turismo
# Lista de frases típicas que um usuário pode enviar para um chatbot de turismo
frases = [
    "Quero reservar um hotel",
    "Tem quartos disponíveis para o próximo fim de semana?",
    "Quero comprar passagem aérea para Paris",
    "Qual o preço das passagens para Roma?",
    "Quais passeios turísticos posso fazer em Lisboa?",
    "Tem tour guiado disponível?",
    "Quais restaurantes recomendam na cidade?",
    "Pode me indicar bons lugares para jantar?",
    "Quero reservar uma viagem para a praia",
    "Quais hotéis têm piscina?"
]


# 2. Vetorização
# Transforma as frases em uma matriz de contagem de palavras (bag of words)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)


# 3. Criar modelo KMeans (4 clusters)
# Inicializa o modelo KMeans para agrupar as frases em 4 grupos
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)


# 4. Mostrar a qual cluster cada frase pertence
# Exibe o agrupamento de cada frase do dataset original
print("\nAgrupamento de frases do chatbot de turismo:")
for i, frase in enumerate(frases):
    print(f"'{frase}' => Cluster {kmeans.labels_[i]}")


# 5. Teste automático com novas frases
# Testa o modelo com frases novas para ver a qual cluster elas pertencem
testes = [
    "Quero comprar passagem para Nova York",
    "Tem hotel com café da manhã incluso?",
    "Quais passeios posso fazer em Roma?",
    "Me indique bons restaurantes na cidade"
]

print("\nTestes automáticos:")
for frase in testes:
    X_novo = vectorizer.transform([frase])
    cluster_previsto = kmeans.predict(X_novo)
    print(f"'{frase}' => Cluster {cluster_previsto[0]}")
