import random
from bottle import post, request,template
from datetime import datetime
import check

def rand():
    return round(random.random(),2)

@post("/home", method="post")
def Monte():  
    if not (check.fieldTest(request.forms.get('PA')) or check.fieldTest(request.forms.get('PB')) or check.fieldTest(request.forms.get('PC')) or check.fieldTest(request.forms.get('PD')) or check.fieldTest(request.forms.get('PE'))):
        return "Input error"
    PA = (float)(request.forms.get('PA')) #Считывание данных
    PB = (float)(request.forms.get('PB'))
    PC = (float)(request.forms.get('PC'))
    PD = (float)(request.forms.get('PD'))
    PE = (float)(request.forms.get('PE'))
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
    
    arr = []
    PAA = []
    PBA = []
    PCA = []
    PDA = []
    PEA = []

    PAA.append(PA)
    PBA.append(PB)
    PCA.append(PC)
    PDA.append(PD)
    PEA.append(PE)

    A = []
    B = []
    C = []
    D = []
    E = []
    tf = []
    koltru = 0.00
    p1 = 1 - (1 - PA) * (1 - PB) * (1 - PC)
    p2 = 1 - (1 - PD) * (1 - PE)
    p = p2 * p1

    for i in range(100):
        AR = rand()
        BR = rand()
        CR = rand()
        DR = rand()
        ER = rand()

        A.append(AR)
        B.append(BR)
        C.append(CR)
        D.append(DR)
        E.append(ER)
        if(((PA > AR) or (PB > BR) or (PC > CR)) and ((PD > DR) or (PE > ER))):
            tf.append("True")
            koltru += 1
            arr = (PAA,PBA,PCA,PDA,PEA,A,B,C,D,E,tf)
        else: 
            tf.append("False")
            arr = (PAA,PBA,PCA,PDA,PEA,A,B,C,D,E,tf)
    f = open(r'data.txt','a')
    f.write("\n P(A) = {0}; p(B) = {1}; P(C) = {2}; P(D) = {3}; P(E) = {4}".format(PA, PB, PC, PD, PE))
    f.write('\n' + "RND A = {0}; RND B = {1}; RND C = {2}; RND D = {3}; RND E = {4}".format(AR,BR,CR,DR,E))
    f.write('\n' + "System reliability P * = {0}".format(koltru/100))
    f.write('\n' + "System reliability analytically P = {0}".format(round(p,5)))
    f.write('\n' + "Absolute error - {0}".format(round(abs(koltru/100-p),5)))
    return template('Monte_Karlo.html', title = "Monte", message = 'Your application description page.',year=datetime.now().year, output=arr,tre = koltru,nad = p)
