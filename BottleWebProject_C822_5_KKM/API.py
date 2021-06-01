from bottle import template, post, request
import math
import random
from datetime import datetime

@post('/three-chanel_system_with_rejection', method='post')
def threeChanelSystemWithRejection():
    timeEnd = float(request.forms.get('T2'))
    multiplier = int(request.forms.get('A'))
    currentrequest = 0;
    requests = []
    while currentrequest <= timeEnd:
        requests.append(currentrequest)
        nextRequest = (1 / multiplier) * math.log10(random.randint(1,10))
        currentrequest = round(currentrequest + nextRequest,2)
    timeOnProcessing = int(request.forms.get('T1')) 
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

    return template('three-chanel_system_with_rejection.html',output = arr, title='About', message='Your application description page.', year=datetime.now().year)