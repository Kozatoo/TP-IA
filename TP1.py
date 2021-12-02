targetedState = [0,1,2,3,4,5,6,7,8]
closedStates = {}
import sys 
sys.setrecursionlimit(181000)

compteur = 0
comparaison = 0
#voir si le jeu est soluble ou pas
def soluble(game): 
    swapNumber=0
    newGame= game
    for i in range(len(game)):
        for j in range(i+1,len(game)):
            if(i==newGame[j]):
                swapNumber+=1
                newGame[i],newGame[j]= newGame[j],newGame[i]
    return (swapNumber % 2 == 0)

def calculateh(game):
    total=0 
    for i in range(9):
        if(game[i]!=targetedState[i]):
            total+=1
    return total-1

#trouver la position de la case vide
def find_zero(game):
    for i in range(9):
        if(game[i]==0):
            return i

def showGame(game):
    print(' ___________')
    for i in range(3):
        print('|',game[i*3],',',game[i*3+1],',',game[i*3+2],'|')

    print(' ___________')
#find next move
class move:
    def up(game,zero):
        if(zero<3):
            return 
        game[zero],game[zero-3]=game[zero-3],game[zero]
        return game
    def down(game,zero):
        if(zero>5):
            return 
        # print(zero)
        # print(game)
        game[zero],game[zero+3]=game[zero+3],game[zero]
        return game
    def left(game,zero):
        if(zero%3==0):
            return 
        game[zero],game[zero-1]=game[zero-1],game[zero]
        return game
    def right(game,zero):
        if(zero%3==2):
            return 
        game[zero],game[zero+1]=game[zero+1],game[zero]
        return game

def add_possible_perm(game,g,open):
    zero_position=find_zero(game)
    newStates= [
        move.up(game.copy(),zero_position),
        move.down(game.copy(),zero_position),
        move.left(game.copy(),zero_position),
        move.right(game.copy(),zero_position)
        ]
    # print("newStates",newStates)
    #possible error here
    for state in newStates:
        if(state and not str(state) in  closedStates):
            open.append([state,g+1])
            global compteur
            compteur+=1
            closedStates[str(state)]=True

def BFS(game):
    open = [[game,0]]
    # print(open)
    depth=1
    while( open != []):

        global comparaison
        comparaison+=1
        if(depth != open[0][1]):
            depth=open[0][1]
            print(depth)
        if(open[0][0]!=targetedState):
            add_possible_perm(open[0][0], open[0][1],open)
            open.pop(0)
        else : 
            return True
    print(open)
    print("No BFS ")

def DFS(game): 
    open= []
    add_possible_perm(game,0,open)
    if(open==[]):
        return False
    else:
        for child in open:
            if child[0] == targetedState:
                global comparaison
                comparaison+=1
                print(child[0])
                return True
            if(DFS(child[0])):
                print(child[0])
                return True
        return False
def iterativeDFS(game):
    open=[]
    open.append([game,0])
    depth=1
    
    while(open!=[]):
        [head,t]=open.pop()
        if(head==targetedState):
            print(len(open))
            return True
        else:
            add_possible_perm(head,t,open)
    if(open==[]):
        return False
    print("No BFS")
            

def depthDFS(game,depth):
    open= []
    add_possible_perm(game,depth,open)
    if(open==[] or depth<0 ):
        return False
    else:
        for child in open:
            global comparaison
            comparaison+=1
            if child[0] == targetedState:
                showGame(child[0])
                showGame(game)
                return True
            if(depthDFS(child[0],depth-1)):
                showGame(child[0])
                return True
        return False

def iterativeDepthDFS(game,maxDepth):
    depth=0
    
    while(depth<maxDepth):
     
        global closedStates
        closedStates={}
        print("depth",depth,'-',maxDepth)
        if depthDFS(game,depth):
            return True
        else :
            depth+=1
    return False

def aStar(game):
    open=[[game,0]]
    while True : 
        g=open[0][1]
        min_state=open[0][0]
        add_possible_perm(min_state,g,open)
        minh=calculateh(min_state)+g
        for s in open:
            if(calculateh(s[0])+s[1]<minh ):
                min_state=s[0]
                minh = calculateh(s[0])+s[1]
                g=s[1]
        # print('minstate',min_state)
        closedStates[str(min_state)]=True
        # closedStates.append(min_state)
        # print("s",min_state,'g',g)
        # print(open)
        open.remove([min_state,g])
        # print(calculateh(min_state))
        if(calculateh(min_state)== -1 ):
            return True
        if open == []:
            # print("No solution")
            return False
     
    
#choose the next state
def next_state():
    g=open[0][1]
    min_state=open[0][0]
    minh=calculateh(min_state)+g
    for s in open:
        if(calculateh(s[0])+s[1]<minh ):
            min_state=s[0]
            minh = calculateh(s[0])+s[1]
            g=s[1]
    # print('minstate',min_state)
    closedStates.append(min_state)
    add_possible_perm(min_state,g)
    open.remove([min_state,g])
    # print(calculateh(min_state))
    if(calculateh(min_state)== -1 ):
        return 1
    if open == []:
        print("No solution")
        return 1

#main programe
# game = [1,2,6,7,8,3,4,0,5]
# game=[1,2,0,3,5,7,6,4,8]
game=[1,2,0,3,5,7,6,4,8]

print(iterativeDepthDFS(game,50))
print("Noeud Compté",compteur)
print("Noeud Visité",comparaison)
# if(soluble(game.copy())):
#     print(BFS(game))
# else: 
#     print("There is no solution")
# print(compteur)