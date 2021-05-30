from bottle import  route, view, template, post, request
import math
import random
from datetime import datetime

@post('/three-chanel_system_with_rejection', method='post')
@route('/three-chanel_system_with_rejection')
@view('three-chanel_system_with_rejection')
def threeChanelSystemWithRejection():
    timeEnd = float(request.forms.get('T2'))
    multiplier = int(request.forms.get('A'))
    currentrequest = 0;
    requests = []
    while currentrequest <= timeEnd:
        requests.append(currentrequest)
        nextRequest = round((1 / multiplier) * math.log10(random.randint(1,10)),2)
        currentrequest = currentrequest + nextRequest
    timeOnProcessing = int(request.forms.get('T1')) 
    CurrentRequestinTheFirstChannel = 0
    CurrentRequestinTheSecondChannel = 0
    CurrentRequestinTheThirdChannel = 0
    firstChanel = []
    secondChanel = []
    thirdChanel = []
    serviced = []
    for i in requests:
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

    requests = [*arr[0]]
    firstChanel = [*arr[1]]
    secondChanel = [*arr[2]]
    thirdChanel = [*arr[3]]
    serviced = [*arr[4]]
    return dict(output = arr, title='About', message='Your application description page.', year=datetime.now().year)