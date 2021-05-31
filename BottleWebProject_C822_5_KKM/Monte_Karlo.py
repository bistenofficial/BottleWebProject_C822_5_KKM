import random
from bottle import post, request
import random

@post("/home", method="post")
def Monte():  
    PA = request.forms.get('PA') #Считывание данных
    PB = request.forms.get('PB')
    PC = request.forms.get('PC')
    PD = request.forms.get('PD')
    PE = request.forms.get('PE')
    rnd = round(random.random())
    if not PA: #Проверка на заполненность
        return "Enter P(A)"
    if not PB:
        return "Enter P(B)"
    if not PC:
        return "Enter P(C)"
    if not PD:
        return "Enter P(D)"
    if not PE:
        return "Enter P(E)"
