import random
import math
import Check_Monte_Karlo_NEGR
from datetime import datetime
from bottle import route, template, post, request

@post("/home", method="post")
def prepare_organiz():  #Метод для добавления нового партнера
    DSR = request.forms.get('DSR') #Считывание данных
    WH = request.forms.get('WH')
    Alpha = request.forms.get('Alpha')
    if not DSR: #Проверка на заполненность
        return "Enter Duration of service of the request"
    if not WH:
        return "Enter Working minutes"
    if not Alpha:
        return "Enter Alpha"
    if not Check_Monte_Karlo_NEGR.check_string(DSR):
        return "Enter correct Duration of service of the request!"
    if not Check_Monte_Karlo_NEGR.check_string(WH):
        return "Enter correct Working minutes!"
    if not Check_Monte_Karlo_NEGR.check_string(Alpha):
        return "Enter correct Alpha!"
    Resurs()

def Resurs():
    req = []
    WH = int(request.forms.get('WH'))
    Alpha = int(request.forms.get('Alpha'))
    currentrequest = 0
    while(currentrequest <= WH):
        req.append(round(currentrequest,2))
        Ti = -(1/Alpha) * math.log10(random.randint(1,10)/10)
        currentrequest = currentrequest + round(Ti,3)
    print('Время прихода заявок')
    print(req)
    Queue(req)



def Queue(req):
    DSR = float(request.forms.get('DSR'))
    FirstFlow = []
    SecondFlow = []
    ThirdFlow = []
    FourthFlow = []
    i = 0
    FSTFRequest = [0,0,0,0]
    while i < len(req):
        if req[i] >= FSTFRequest[0]:
            FSTFRequest[0] = round(req[i] + DSR,3)
            FirstFlow.append(FSTFRequest[0])
            SecondFlow.append(0)
            ThirdFlow.append(0)
            FourthFlow.append(0)
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[1]:
            FSTFRequest[1] = req[i] + DSR
            FirstFlow.append(0)
            SecondFlow.append(FSTFRequest[1])
            ThirdFlow.append(0)
            FourthFlow.append(0)
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[2]:
            FSTFRequest[2] = req[i] + DSR
            FirstFlow.append(0)
            SecondFlow.append(0)
            ThirdFlow.append(FSTFRequest[2])
            FourthFlow.append(0)
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[3]:
            FSTFRequest[3] = req[i] + DSR
            FirstFlow.append(0)
            SecondFlow.append(0)
            ThirdFlow.append(0)
            FourthFlow.append(FSTFRequest[3])
            i = i + 1
            continue
        else:
            req[i] = req[i] + 0.01
    Result(req,FirstFlow,SecondFlow,ThirdFlow,FourthFlow)
    #arr = []
    #arr = [req,FirstFlow,SecondFlow,ThirdFlow,FourthFlow]
    #return template('Monte_Karlo_NEGR.html',title='Four-channel queuing system with limited queue', message='GG', year=datetime.now().year, output = arr)

def Result(req,FirstFlow,SecondFlow,ThirdFlow,FourthFlow):
    j = 0
    while j < len(req):
        print(str(round(req[j],3))+"   "+str(round(FirstFlow[j],3))+" "+str(round(SecondFlow[j],3))+" "+str(round(ThirdFlow[j],3))+" "+str(round(FourthFlow[j],3)))
        j = j + 1
