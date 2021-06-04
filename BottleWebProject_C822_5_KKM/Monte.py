import random
import math
import Check_Monte_Karlo_NEGR
from datetime import datetime
from bottle import route, template, post, request

@post("/Monte_Karlo_NEGR", method="post")
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
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f = open(r'text.txt','a')
    f.write('\n' + 'Дата и время работы:' + date_time + '\n')
    f.write('Введенные данные:' + '\n')
    f.write('Время обработки каждой заявки:' + DSR + 'минут' +'\n')
    f.write('Время принятия заявок:' + WH + 'минут' + '\n')
    f.write('Альфа:' + Alpha + '\n')
    f.close()
    return Resurs()

def Resurs():
    x = 0
    req = []
    WH = int(request.forms.get('WH'))
    Alpha = int(request.forms.get('Alpha'))
    currentrequest = 0
    while(currentrequest <= WH):
        req.append(round(currentrequest,3))
        Ti = -(1/Alpha) * math.log10(random.randint(1,10)/10)
        currentrequest = currentrequest + round(Ti,3)
    return Queue(req)



def Queue(req):
    DSR = float(request.forms.get('DSR'))
    FirstFlow = []
    SecondFlow = []
    ThirdFlow = []
    FourthFlow = []
    i = 0
    x = 0
    FSTFRequest = [0,0,0,0]
    req1 = req.copy()
    while i < len(req):
        if req[i] >= FSTFRequest[0]:
            FSTFRequest[0] = round(req[i] + DSR,3)
            FirstFlow.append(round(FSTFRequest[0],3))
            SecondFlow.append(" ")
            ThirdFlow.append(" ")
            FourthFlow.append(" ")
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[1]:
            FSTFRequest[1] = round(req[i] + DSR,3)
            FirstFlow.append(" ")
            SecondFlow.append(round(FSTFRequest[1],3))
            ThirdFlow.append(" ")
            FourthFlow.append(" ")
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[2]:
            FSTFRequest[2] = round(req[i] + DSR,3)
            FirstFlow.append(" ")
            SecondFlow.append(" ")
            ThirdFlow.append(round(FSTFRequest[2],3))
            FourthFlow.append(" ")
            i = i + 1
            continue
        elif req[i] >= FSTFRequest[3]:
            FSTFRequest[3] = round(req[i] + DSR,3)
            FirstFlow.append(" ")
            SecondFlow.append(" ")
            ThirdFlow.append(" ")
            FourthFlow.append(round(FSTFRequest[3],3))
            i = i + 1
            continue
        else:
            req[i] = round(req[i],3) + 0.01
    Result(req1,FirstFlow,SecondFlow,ThirdFlow,FourthFlow)
    arr = []
    arr = (req1,FirstFlow,SecondFlow,ThirdFlow,FourthFlow)
    return template('Monte_Karlo_NEGR.html', title='Monte', message='GG',year=datetime.now().year, output=arr)
    
def Result(req1,FirstFlow,SecondFlow,ThirdFlow,FourthFlow):
    z = 0
    f = open(r'text.txt','a')
    f.write('Результат выполнения программы:' + '\n')
    f.write('Заявка, очередь и окончанение выполнения:' + '\n')
    while z < len(req1):
        f.write(str(round(req1[z],3))+"   "+str(FirstFlow[z])+" "+str(SecondFlow[z])+" "+str(ThirdFlow[z])+" "+str(FourthFlow[z]) + '\n')
        z = z + 1
    f.close()
