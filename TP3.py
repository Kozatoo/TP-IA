N=5

def etatFinal(s):
    for key,value in s:
        if key != "moves" and value !=1 and value !=2:
            return False
    return True
def utilite(s):
    return 1 if s['moves'] % 2 == 1 else -1
def possibleActions(s):
    newStates=[]
    
def minmax(s):
    if(etatFinal(s)):
        result = utilite(s)
    

Pile= {N:1,"moves":1}


