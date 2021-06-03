from bottle import template, post, request
import math
import random
from datetime import datetime
import re
import os

def check_mail(str): # fuction for input check
    pattern=r"^(?=.+)(?:[1-9]\d*)?(?:\.\d+)?$"
    number_re=re.compile(pattern)
    return bool(number_re.findall(str))

@post('/three-chanel_system_with_rejection', method='post')
def threeChanelSystemWithRejection(): 
    if (check_mail(request.forms.get('T2')) and check_mail(request.forms.get('A')) and check_mail(request.forms.get('T1')) and check_mail(request.forms.get('TIMES'))):
        timeEnd = float(request.forms.get('T2'))
        multiplier = float(request.forms.get('A'))
        count = int(request.forms.get('TIMES'))
        x = [] # We create arrays with which we will be throughout all iterations
        allRequests = []
        firstChanel = []
        secondChanel = []
        thirdChanel = []
        serviced = []
        while (count > 0): # until the tests are over
            currentrequest = 0;
            requests = []
            while currentrequest <= timeEnd: # create an array with orders
                allRequests.append(currentrequest)
                requests.append(currentrequest)
                nextRequest = (1 / multiplier) * math.log10(random.randint(1,10))
                currentrequest = round(currentrequest + nextRequest,2)
            timeOnProcessing = float(request.forms.get('T1')) 
            CurrentRequestinTheFirstChannel = 0
            CurrentRequestinTheSecondChannel = 0
            CurrentRequestinTheThirdChannel = 0
            numOfServiced = 0
            for i in requests: # check when the processing of the previous order is finished in the stream and if the voucher arrives after the end, then the voucher rises into the stream
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
                else: # if all threads are busy, the request is refused processing
                    firstChanel.append(' ')
                    secondChanel.append(' ')
                    thirdChanel.append(' ')
                    serviced.append(0)
            allRequests.append('Stop') # summing up the results of the test
            serviced.append("Number of serviced = " + (str)(numOfServiced))
            firstChanel.append(' ')
            secondChanel.append(' ')
            thirdChanel.append(' ')
            count -= 1
            x.append(numOfServiced)
            
        Result(allRequests,firstChanel,secondChanel,thirdChanel,timeOnProcessing, timeEnd, multiplier) # output
        answer = 0
        all = 0
        for i in x: # count the average
            answer += i
            all +=1
        answer = answer / all # summing up the results of all tests
        allRequests.append('-')
        serviced.append("а = " + str(answer))
        firstChanel.append('-')
        secondChanel.append('-')
        thirdChanel.append('-')
        arr = [allRequests, firstChanel, secondChanel, thirdChanel,serviced]
        return template('three-chanel_system_with_rejection.html',output = arr, title='About', message='Your application description page.', year=datetime.now().year)
    else:
        return "Incorrect entry, you must enter numbers greater than 0!"


def Result(req,FirstFlow,SecondFlow,ThirdFlow, t1,t2,a): # function of output
    now = datetime.now()
    working_directory = os.getcwd()
    file_path = working_directory + '\Hystory.txt'
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f = open(file_path,'a')
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