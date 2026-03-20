!pip install langchain==0.3.0 langchain-groq==0.2.0 langchain-community==0.3.0 youtube_transcript_api==0.6.2 pypdf==5.0.0

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from youtube_transcript_api import YouTubeTranscriptApi

# ========== CONFIGURAÇÃO ==========
api_key = 'API_KEY'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.3-70b-versatile')

# ========== FUNÇÕES DE CARREGAMENTO ==========
def carregar_sites():
    url_site = input('Insira a url do site: ')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carregar_pdf():
    caminho = '/content/drive/MyDrive/python.ia0/arquivos/RoteiroViagemEgito.pdf'
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carregar_youtube():
    url_youtube = input('Insira a url video: ')

    if 'youtu.be/' in url_youtube:
        video_id = url_youtube.split('youtu.be/')[-1].split('?')[0]
    elif 'youtube.com/watch?v=' in url_youtube:
        video_id = url_youtube.split('v=')[-1].split('&')[0]
    else:
        print("❌ URL inválida")
        return ""

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        documento = ' '.join([item['text'] for item in transcript])
        print(f"✅ Transcrição carregada! {len(documento)} caracteres")
        return documento
    except Exception as e:
        print(f"❌ Erro: {e}")
        return ""

# ========== FUNÇÃO DO BOT ==========
def resposta_bot(mensagens, documento):
    system_mensagem = 'Voce e um assistente amigavel chamado olaf que tem acesso as seguintes informacoes para dar uma resposta precisa: {informacoes}'
    mensagens_modelo = [('system', system_mensagem)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content  # ← CORRIGIDO: dict ao invés de set

# ========== MENU PRINCIPAL ==========
print('Ola seja bem vindo como posso ajudar?')

texto_selecao = '''Digite 1 se quiser conversar com um site
Digite 2 se quiser conversar com um pdf
Digite 3 se quiser conversar com um video de youtube
'''

documento = ""  # ← INICIALIZAR

while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carregar_sites()  # ← ARMAZENAR retorno
        break
    if selecao == '2':
        documento = carregar_pdf()  # ← ARMAZENAR retorno
        break
    if selecao == '3':
        documento = carregar_youtube()  # ← ARMAZENAR retorno
        break
    print('Digite um valor entre 1 e 3')

# ========== CHAT LOOP ==========
mensagens = []
while True:
    pergunta = input('User: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado ate a proxima.')
print(mensagens)
