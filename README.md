# ⚡ High-Speed Terminal Chatbot - Groq API

Este é um assistente virtual de alta performance desenvolvido em **Python puro**, utilizando a infraestrutura da **Groq** para processamento de linguagem natural com baixíssima latência.

## 🛠️ Tecnologias e Diferenciais
- **Linguagem:** Python 3.x (Script de Terminal).
- **Motor de IA:** Groq API (Modelos Llama 3 / Mixtral).
- **Gestão de Contexto:** Implementação de histórico de mensagens para memória de curto prazo da IA.
- **Performance:** Foco em velocidade de resposta extrema através de LPUs (Language Processing Units).

## 🧠 Lógica de Implementação
O script utiliza um loop contínuo (`while`) para interação em tempo real, mantendo o contexto da conversa em uma lista estruturada de dicionários, enviada a cada nova interação para a API da Groq.

## 🚀 Como Executar
1. Clone o repositório.
2. Instale a biblioteca da Groq: `pip install groq`.
3. Configure sua `GROQ_API_KEY`.
4. Execute: `python main.py`.
