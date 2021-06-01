from bottle import template, post, request
import math
import random
from datetime import datetime
import re

def check_mail(str): 
    pattern=r"^(?=.+)(?:[1-9]\d*)?(?:\.\d+)?$"
    number_re=re.compile(pattern)
    return bool(number_re.findall(str))

@post('/three-chanel_system_with_rejection', method='post')
def threeChanelSystemWithRejection():
    if (check_mail(request.forms.get('T2')) and check_mail(request.forms.get('A')) and check_mail(request.forms.get('T1'))):
        timeEnd = float(request.forms.get('T2'))
        multiplier = float(request.forms.get('A'))
        currentrequest = 0;
        requests = []
        while currentrequest <= timeEnd:
            requests.append(currentrequest)
            nextRequest = (1 / multiplier) * math.log10(random.randint(1,10))
            currentrequest = round(currentrequest + nextRequest,2)
        timeOnProcessing = float(request.forms.get('T1')) 
        CurrentRequestinTheFirstChannel = 0
        CurrentRequestinTheSecondChannel = 0
        CurrentRequestinTheThirdChannel = 0
        firstChanel = []
        secondChanel = []
        thirdChanel = []
        serviced = []
        numOfServiced = 0
        for i in requests:
            if (i >= CurrentRequestinTheFirstChannel):
                firstChanel.append(round((i + timeOnProcessing),2))
                CurrentRequestinTheFirstChannel = i + timeOnProcessing
                secondChanel.append(' ')
                thirdChanel.append(' ')
                serviced.append(1)
                numOfServiced +=1
            elif (i >= CurrentRequestinTheSecondChannel):
                secondChanel.append(round((i + timeOnProcessing),2))
                CurrentRequestinTheSecondChannel = i + timeOnProcessing
                thirdChanel.append(' ')
                firstChanel.append(' ')
                serviced.append(1)
                numOfServiced +=1
            elif(i >= CurrentRequestinTheThirdChannel):
                thirdChanel.append(round((i + timeOnProcessing),2))
                CurrentRequestinTheThirdChannel = i + timeOnProcessing
                firstChanel.append(' ')
                secondChanel.append(' ')
                serviced.append(1)
                numOfServiced +=1
            else:
                firstChanel.append(' ')
                secondChanel.append(' ')
                thirdChanel.append(' ')
                serviced.append(0)
        requests.append('Stop')
        serviced.append("Number of serviced = " + (str)(numOfServiced))
        firstChanel.append(' ')
        secondChanel.append(' ')
        thirdChanel.append(' ')
        arr = [requests, firstChanel, secondChanel, thirdChanel,serviced]
        Result(requests,firstChanel,secondChanel,thirdChanel,timeOnProcessing, timeEnd, multiplier)
        return template('three-chanel_system_with_rejection.html',output = arr, title='About', message='Your application description page.', year=datetime.now().year)
    else:
        return "Incorrect entry, you must enter numbers greater than 0!"


def Result(req,FirstFlow,SecondFlow,ThirdFlow, t1,t2,a):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f = open(r'C:\Users\kseno\source\repos\bistenofficial\BottleWebProject_C822_5_KKM\BottleWebProject_C822_5_KKM\Hystory.txt','a')
    f.write('\n' + 'Date and time:' + date_time + '\n')
    f.write('Enterd values:' + '\n')
    f.write('T1:' + str(t1) + '\n')
    f.write('T2:' + str(t2) + '\n')
    f.write('a:' + str(a) + '\n')
    z = 0
    f.write('Result of program:' + '\n')
    f.write('Request and time when done:' + '\n')
    while z < len(req):
        f.write(str(req[z])+"   "+str(FirstFlow[z])+" "+str(SecondFlow[z])+" "+str(ThirdFlow[z]) + '\n')
        z += 1
    f.close()