import random
from bottle import post, request 

@post("/home", method="post")
def prepare_organiz():  #Метод для добавления нового партнера
    DSR = request.forms.get('DSR') #Считывание данных
    WH = request.forms.get('WH')
    Alpha = request.forms.get('Alpha')
    if not DSR: #Проверка на заполненность
        return "Enter Duration of service of the request"
    if not WH:
        return "Enter Working hours"
    if not Alpha:
        return "Enter Alpha"
