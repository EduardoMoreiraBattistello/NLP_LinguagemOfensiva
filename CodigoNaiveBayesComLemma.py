import spacy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
from unidecode import unidecode

# Carregar o modelo spaCy para português
nlp = spacy.load('pt_core_news_sm')

# Função de pré-processamento
def preprocess(text):
    text = text.lower()
    text = unidecode(text)
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    return lemmatized_text

# Carregar o CSV
df = pd.read_csv("C:\\Temp\\Projeto\\Labeled_corpus.csv")

# Aplicar pré-processamento à coluna 'text'
df['text_preprocessado'] = df['text'].apply(preprocess)

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(df['text_preprocessado'], df['label'], test_size=0.2, random_state=42)

# Criar a representação vetorial usando o Vector Space Model
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Treinar o modelo SVM e suprimir o aviso
svm_classifier = LinearSVC(dual=False)
svm_classifier.fit(X_train_vectorized, y_train)

# Fazer previsões no conjunto de teste
predictions = svm_classifier.predict(X_test_vectorized)

# Avaliar a precisão do modelo SVM
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo SVM: {accuracy:.2f}')

# Exibir o relatório de classificação do modelo SVM
print('Relatório de Classificação SVM:\n', classification_report(y_test, predictions))
