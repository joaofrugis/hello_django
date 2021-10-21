from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {}! Anos: {}</h1>'.format(nome, idade))

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse('<h1>A soma dos números é: {}</h1>'.format(soma))

def subtracao(request, n1, n2):
    sub = n1 - n2
    return HttpResponse('<h1>A subtração dos números é: {}</h1>'.format(sub))

def multiplcacao(request, n1, n2):
    mult = n1 * n2
    return HttpResponse('<h1>A multiplcação dos números é: {}</h1>'.format(mult))

def divisao(request, n1, n2):
    div = n1 / n2
    return HttpResponse('<h1>A divisão dos números é: {}</h1>'.format(div))