# 💬 ChatBot Interativo com Python + Django

Este projeto foi minha primeira tentativa de construir uma aplicação web completa usando **Python com Django**. A proposta era desenvolver um **ChatBot funcional**, simulando atendimento automatizado para uma empresa fictícia, utilizando **interpretação de linguagem natural personalizada**, sem uso de IA externa.

## 🎯 Objetivo

Criar um sistema capaz de interpretar mensagens do usuário e responder de forma coerente, com base em **palavras-chave organizadas por intenção**, tudo rodando no backend Python e integrado ao frontend via Django.

## ⚙️ O que foi feito

- Integração com Django (estrutura básica de views, rotas e templates)
- Construção manual de um interpretador de mensagens:
  - Mapeamento de palavras-chave por categorias (intenção)
  - Sistema de verificação de correspondência com frases do usuário
  - Respostas pré-programadas associadas a combinações de palavras-chave
- Interface simples em **HTML/CSS/JavaScript** para simular conversa
- Tratamento de erros e respostas inesperadas

## 📌 Contexto

Este projeto começou como ideia para o **trabalho final da disciplina de Lógica de Programação**, mas devido ao prazo curto e resistência dos colegas de grupo, uma versão simplificada foi apresentada oficialmente.

Desde então, evoluí o sistema com mais calma, melhorando a estrutura do código e a lógica do interpretador.


### 🧠 Como o interpretador funciona
 
O coração deste projeto é uma função chamada `encontrar_resposta`, que simula um ChatBot simples utilizando **análise de similaridade textual**. A lógica funciona da seguinte forma:

 
1.  
**Pré-processamento da pergunta:**
 
  - Remove acentos, pontuação e transforma tudo para minúsculas.
 
  - Divide a frase em **tokens** (palavras individuais).
 
 
2.  
**Comparação com as "perguntas-chave" do FAQ:**
 
  - As chaves do dicionário `faq` representam perguntas ou intenções.
 
  - Cada chave é dividida em tokens, e comparada com a entrada do usuário.
 
  - A pontuação da similaridade é calculada: 
 
    - **Pontos por interseção direta** entre tokens.
 
    - **Pontos adicionais por similaridade textual**, utilizando a biblioteca `fuzzywuzzy` (com `partial_ratio`).
 
 
3.  
**Seleção da melhor resposta:**
 
  - Se a pontuação de similaridade for acima do limite mínimo, a resposta correspondente é retornada.
 
  - Caso contrário, o bot responde com uma mensagem padrão de erro.

 
Essa lógica básica de NLP (Processamento de Linguagem Natural) **não usa modelos de IA ou APIs externas**, sendo completamente artesanal. Ela é altamente customizável, e o dicionário `faq` pode ser adaptado para qualquer domínio ou empresa fictícia.
  

## 🚧 Próximos passos (planejados)

- Refatorar backend com Flask (mais leve que Django)
- Adicionar interface com entrada de texto em tempo real
- Treinamento real via IA ou integração com APIs externas (OpenAI, por exemplo)

## ✨ O que aprendi

- Fundamentos de back-end com Django
- Manipulação de rotas e templates HTML
- Lógica de construção de interpretadores básicos
- Estruturação de código reutilizável
- Conceitos básicos de **NLP (Natural Language Processing)** sem IA
- Trabalho com HTML, CSS e JavaScript para comunicação com backend

---

📂 Linguagem: Python  
🧠 Conceitos: Backend, NLP artesanal, lógica, Django  
💻 Ferramentas: PyCharm
