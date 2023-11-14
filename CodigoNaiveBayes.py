import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from unidecode import unidecode

# Função de pré-processamento
def preprocess(text):
    text = text.lower()
    text = unidecode(text)
    return text

# Carregar o CSV
df = pd.read_csv("C:/Temp/Trabalho Grau A/TrabalhoGrauA/Labeled_corpus.csv")

# Aplicar pré-processamento à coluna 'text'
df['text_preprocessado'] = df['text'].apply(preprocess)

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(df['text_preprocessado'], df['label'], test_size=0.2, random_state=42)

# Criar a representação vetorial usando o Vector Space Model
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Treinar o modelo Naive Bayes
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Fazer previsões no conjunto de teste
predictions = classifier.predict(X_test_vectorized)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo: {accuracy:.2f}')

# Exibir o relatório de classificação
print('Relatório de Classificação:\n', classification_report(y_test, predictions))