import random
from bottle import post, request 

@post("/home", method="post")
def prepare_organiz():  #Метод для добавления нового партнера
    PA = request.forms.get('PA') #Считывание данных
    PB = request.forms.get('PB')
    PC = request.forms.get('PC')
    PD = request.forms.get('PD')
    PE = request.forms.get('PE')
    if not PA: #Проверка на заполненность
        return "Enter Duration of service of the request"
    if not PB:
        return "Enter Working hours"
    if not PC:
        return "Enter Alpha"
    if not PD:
        return "Enter Alpha"
    if not PE:
        return "Enter Alpha"