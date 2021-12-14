import copy
import string
 
f = open("2021/day14/input.txt", "r")
 
matrice = list()
input = list()
contatore = dict(zip(list(string.ascii_uppercase), [0] * 26))
 
def getnext(val):
    for el in matrice:
        if el[0]==val: return el[1]
    return None
 
def incdiz(val,frequenza,tot=1):
    for e in frequenza:
        if e[0]==val:
            e[1]=e[1]+tot
 
def setfrequenza(frequenza):
    for i in range(len(input) - 1):
        elementi = input[i] + input[i + 1]
        contatore.update({input[i]: contatore.get(input[i]) + 1})
        for coppia in matrice:
            if coppia[0] == elementi:
                incdiz(elementi,frequenza)
    contatore.update({input[len(input) - 1]: contatore.get(input[len(input) - 1]) + 1})
 
def controllarules(frequenzaprec=None):
    tempfreq=list(map(list,zip([el[0] for el in matrice],[0]*len(matrice))))
    for el in frequenzaprec:
        next=getnext(el[0])
        tempstring1=el[0][0]+next
        incdiz(tempstring1,tempfreq,el[1])
        tempstring2=next+el[0][1]
        incdiz(tempstring2,tempfreq,el[1])
        contatore.update({next: contatore.get(next) + el[1]})
    ##print(tempfreq)
    return copy.deepcopy(tempfreq)
 
 
if __name__ == '__main__':
 
    for l in f:
        x = l.replace("\n", "")
        if len(x.split(" -> ")) == 1 and len(x) > 0:
            input = [x[i] for i in range(len(x))]
 
        elif len(x.split(" -> ")) == 2:
            matrice.append(x.split(" -> "))
 
    frequenza=list(map(list,zip([el[0] for el in matrice],[0]*len(matrice))))
 
    setfrequenza(frequenza)
    ##print(frequenza)
    ##print(contatore)
    for i in range(40):
        ##print(i)
        frequenza=controllarules(frequenza)
        ##print(contatore)
 
 
    ##print(contatore)
    massimo=max(contatore.values())
    minimo = min(filter(lambda x: x>0,contatore.values()))
    print("Answer is: " + str(int(massimo - minimo)))
 
