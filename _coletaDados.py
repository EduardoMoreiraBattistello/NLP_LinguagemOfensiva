import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="dGkohMLa_kZi3doGEHmWng",         # your client id
                               client_secret="oadEZaJKsUlozNyvi_Err3FvMngPsw",      # your client secret
                               user_agent="eduardobattistello")        # your user agent

subreddit = reddit_read_only.subreddit("BolsonaroBurro")

# Inicialize as listas para armazenar os dados
titulos = []
comentarios_lista = []

for post in subreddit.hot(limit=100):
    # Limpar os comentários e concatenar em uma string
    comentarios = '\n'.join([comment.body for comment in post.comments if isinstance(comment, praw.models.Comment)])
    
    # Adicionar os títulos e os comentários nas listas
    titulos.append(post.title)
    comentarios_lista.append(comentarios)

# Criar um DataFrame com os dados
dados = pd.DataFrame({'Título': titulos, 'Comentários': comentarios_lista})

# Exportar para CSV
dados.to_csv('dados_BolsonaroBurro.csv', index=False, encoding='utf-8-sig')

print("Dados exportados")