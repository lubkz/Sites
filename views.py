from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ChatBotFunc import encontrar_resposta

def test_form(request):
    return render(request, "test_form.html")

def index(request):
    return HttpResponse("Bem-vindo ao índice de enquetes!")

def chatbot_page(request):
    return render(request, 'chatbot_form.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        # Obter a mensagem do usuário do corpo da requisição POST
        pergunta = request.POST.get('message')
        print(pergunta)

        # Encontrar a resposta usando a função encontrar_resposta
        bot_response = encontrar_resposta(pergunta)

        # Retornar a resposta do chatbot como uma resposta HTTP
        return JsonResponse({'response': bot_response})
    else:
        # Se não for uma requisição POST, simplesmente renderizar o formulário do chatbot
        return render(request, 'chatbot_form.html')
