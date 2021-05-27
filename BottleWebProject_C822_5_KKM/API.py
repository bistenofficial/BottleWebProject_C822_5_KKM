from bottle import post, request
import math
import random
@post('/three-chanel_system_with_rejection', method='post')

def flowOfApplicationsGen():
    timeEnd = int(request.forms.get('T1')) * 60
    multiplier = request.forms.get('A')
    currentrequest = 0;
    requests = []
    while currentrequest <= timeEnd:
        requests.append(currentrequest)
        nextRequest = (1 / multiplier) * math.log10(random.randint(0,10) / 10)
        currentrequest = currentrequest + nextRequest
    return requests

@post('/three-chanel_system_with_rejection', method='post')

def threeChanelSystemWithRejection(requests):
    timeOnProcessing = request.forms.get('T2') 
    CurrentRequestinTheFirstChannel = 0
    CurrentRequestinTheSecondChannel = 0
    CurrentRequestinTheThirdChannel = 0
    firstChanel = []
    secondChanel = []
    thirdChanel = []
    serviced = []
    for i in requset:
        if (i >= CurrentRequestinTheFirstChannel):
            firstChanel.append(i + timeOnProcessing)
            CurrentRequestinTheFirstChannel = i + timeOnProcessing
            secondChanel.append(0)
            thirdChanel.append(0)
            serviced.append(1)
        elif (i >= CurrentRequestinTheSecondChannel):
            secondChanel.append(i + timeOnProcessing)
            CurrentRequestinTheSecondChannel = i + timeOnProcessing
            thirdChanel.append(0)
            firstChanel.append(0)
            serviced.append(1)
        elif(i >= CurrentRequestinTheThirdChannel):
            thirdChanel.append(i + timeOnProcessing)
            CurrentRequestinTheThirdChannel = i + timeOnProcessing
            firstChanel.append(0)
            secondChanel.append(0)
            serviced.append(1)
        else:
            serviced.append(0)
        arr = [requests, firstChanel, secondChanel, thirdChanel,serviced]
        return arr