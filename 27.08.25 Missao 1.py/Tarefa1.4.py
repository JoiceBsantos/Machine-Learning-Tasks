# TAREFAS DE APRENDIZADO NAO SUPERVISIONADO 

# =============================================================================
# TAREFA 4: Agrupamento de Mensagens (K-Means com 3 clusters)
# =============================================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# 1. Matriz de mensagens (sem rótulos)
mensagens = [
    "Quero pedir pizza",
    "Qual o valor da pizza grande?",
    "Preciso de suporte no aplicativo",
    "O app está travando",
    "Vocês têm sobremesas?",
    "Meu pedido está atrasado",
    "Como faço para alterar meu pedido?",
    "Tem pizza vegetariana?",
    "Não consigo finalizar a compra"
]

# 2. Vetorizar texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens)

# 3. Criar modelo de agrupamento com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# 4. Mostrar os grupos encontrados
print("\nAgrupamento de mensagens:")
for i, msg in enumerate(mensagens):
    print(f"'{msg}' => Cluster {kmeans.labels_[i]}")

# 5. Teste automático de nova frase
testes = [
    "Quero pedir uma pizza grande",
    "Meu aplicativo não abre",
    "Tem sobremesa disponível?"
]

print("\nTestes automáticos:")
for msg in testes:
    X_novo = vectorizer.transform([msg])
    cluster_previsto = kmeans.predict(X_novo)
    print(f"'{msg}' => Cluster {cluster_previsto[0]}")

# 6. Interação: classificar nova frase do usuário
while True:
    nova_mensagem = input("\nDigite uma nova mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        print("Encerrando classificação. 👋")
        break
    X_novo = vectorizer.transform([nova_mensagem])
    cluster_previsto = kmeans.predict(X_novo)
    print(f"Essa mensagem se parece com o Cluster {cluster_previsto[0]}")
