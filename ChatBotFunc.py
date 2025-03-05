#Biblioteca crucial para o funcionamento do código - Favor baixar no terminal com "pip install fuzzywuzzy"
from fuzzywuzzy import fuzz

#Funções do python
import unicodedata
import string
faq = {
    # Horário de atendimento
    ("horario atendimento", "horario atendimento", "horas atendimento", "horas atendimento"):
        "O horário de atendimento varia de unidade para unidade." + " Por favor, especifique a unidade em sua pergunta.",

    # Sedes no Brasil
    ("endereço sedes brasil", "endereço sedes empresa", "endereço sedes empresa"):
        "A Etical Enterprises tem 2 sedes espalhadas pelo Brasil. Uma no Rio de Janeiro e uma no Ceará.",

    # Rio de Janeiro - São Gonçalo - Localização
    ("endereço sede rio de janeiro", "endereço sede empresa rio de janeiro", "endereço rio de janeiro sede",
     "endereço sede sao gonçalo", "endereço sede empresa sao gonçalo", "endereço sao gonçalo sede"):
        "A sede do Rio de Janeiro fica na cidade de São Gonçalo, Rua De Leonardo Pravo, N* 1500, Nerlin, São Gonçalo.",

    # Rio de Janeiro - São Gonçalo - Horários
    ("horario sede rio janeiro", "horario sede rio janeiro", "horario atendimento rio janeiro", "horario rio janeiro",
     "horario sede sao gonçalo", "horario atendimento sao gonçalo", "horário sao gonçalo"):
        "O horário de funcionamento da sede no Rio de Janeiro na cidade de São Gonçalo é das 9:00 até as 19:00 horas.",

    # Ceará - Fortaleza - Local
    ("endereço sede ceara", "endereço sede empresa ceara", "endereço ceara sede",
     "endereço sede fortaleza", "endereço sede empresa fortaleza", "endereço fortaleza sede"):
        "A sede do Ceará fica na cidade de Fortaleza, Rua Leopodina da Assunção, N* 472, Aldeota, Fortaleza.",

    # Ceará - Fortaleza - Horários
    ("horario sede fortaleza", "horário atendimento sede fortaleza", "horario fortaleza",
     "horario sede ceara", "horário atendimento sede ceara", "horario ceara"):
        "O horário de funcionamento da sede em fortaleza é das 9:00 até as 19:00 horas.",
}


def retirar_acento(texto):
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

#Função principal que encontra a melhor resposta para a pergunta feita baseada na similaridade de texto.
def encontrar_resposta(pergunta):

    if len(pergunta.strip()) <= 15:
        return "Desculpe, não entendi sua pergunta. Tente escrever uma pergunta mais longa."

    #Variável pergunta vai receber o valor da pergunta sem acento e sem pontuações.
    pergunta = retirar_acento(pergunta.lower().translate(str.maketrans("", "", string.punctuation)))

    #Cria uma variável que armazena a pergunta em forma de tokens.
    tokens_pergunta = set(pergunta.split())

    #Variável pra armazenar a melhor resposta.
    melhor_resposta = None

    #Score que a máquina vai determinar como melhor ou não.
    melhor_score = 0

    #Aqui ele vai rodar cada palavra chave dos itens do faq até que o melhor valor seja obtido, ou não.
    for palavra_chave, resposta in faq.items():

        #Aqui eu estou tornando as palavras chaves do meu faq, TODAS ELAS, em tokens, que já expliquei antes.
        tokens_chave = set(" ".join(palavra_chave).split())

        score = len(tokens_pergunta.intersection(tokens_chave))

        #Aqui crio uma variável temporária "palavra" que armazena cada palavra dentro da palavra_chave
        for palavra in palavra_chave:

            #Aqui crio uma variável para armazenar a similiridade.
            similaridade = fuzz.partial_ratio(palavra, pergunta)

            #Aqui estou definindo o quão similar ele precisar ser e, caso não seja tão similar
            #quanto eu quiser, ele vai retornar lá embaixo um valor fixo pra resposta.
            if similaridade > 90:

                #Aqui eu faço a variável score aumentar em 1, o que me permite iniciar o próximo
                #passo do código logo abaixo desse.
                score += 1

        #Pre final do codigo que só executa quando o codigo td já fez seu trabalho
        #Se score for maior que melhor resposta, o que é obrigatorio acontecer no final do codigo
        if score > melhor_score:

            #Torno as variáveis de antes sem valor nenhum dentro nos resultados que obtive.
            melhor_score = score
            melhor_resposta = resposta

    if melhor_score > 0:

        #Retornando a melhor_resposta para a variável resposta definida no início da função.
        return melhor_resposta
    else:

        return "Desculpe, não entendi sua pergunta."

