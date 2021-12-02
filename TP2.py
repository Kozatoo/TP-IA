# 0 3 6
# 1 2 4
# 5 2 8 
#set the game 
targetedState = [0,1,2,3,4,5,6,7,8]
closedStates ={}
close = []
compteur=0
comparaison= 0
# h determine le nombre de piece mal placé
def positionDistance(position,value):
    difHorizontal= abs((position%3)-(value%3))
    difVertical=abs(int(position/3)-int(value/3))
    return difHorizontal + difVertical
def calculateh1(game):
    total=0
    for i in range(8):
        total+= positionDistance(i,game[i])
    return total
def calculateh(game):
    total=0             
    for i in range(9):
        if(game[i]!=targetedState[i]):
            total+=1
    return total

def find_zero(game):
    for i in range(9):
        if(game[i]==0):
            return i
def valid_pos(x):
    return x>=0 and x<9 

#possible permutations
#up
class move:
    def up(game,zero):
        if(zero<3):
            return 
        game[zero],game[zero-3]=game[zero-3],game[zero]
        return game
    def down(game,zero):
        if(zero>5):
            return 
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
    
def soluble(game): 
    swapNumber=0
    newGame= game
    for i in range(len(game)):
        for j in range(i+1,len(game)):
            if(i==newGame[j]):
                swapNumber+=1
                # print('game',newGame)
                # print('i',i,'j',j)
                newGame[i],newGame[j]= newGame[j],newGame[i]
    # print(game)
    # print(newGame)
    # print(swapNumber)
    return (swapNumber % 2 == 0)

    

def possible_perm(game,g):
    zero_position=find_zero(game)
    up_state=move.up(game.copy(),zero_position)
    down_state=move.down(game.copy(),zero_position)
    left_state=move.left(game.copy(),zero_position)
    right_state=move.right(game.copy(),zero_position)
    global compteur
    if(up_state and not str(up_state) in closedStates):
        open.append([up_state,g+1])
        compteur+=1
    if(down_state and not str(down_state) in closedStates):
        open.append([down_state,g+1])
        compteur+=1
    if(left_state and not str(left_state) in closedStates):
        open.append([left_state,g+1])
        compteur+=1
    if(right_state and not str(right_state) in closedStates):
        open.append([right_state,g+1])
        compteur+=1
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
    closedStates[str(min_state)]=True
    # print("minstate",min_state)
    possible_perm(min_state,g)
    open.remove([min_state,g])
    # print(calculateh(min_state))
    if(calculateh(min_state)== 0):
        return 1
    if open == []:
        print("No solution")
        return 1
    
# A* algorithm
#main
# game = [1,0,2,5,6,4,8,2,7]
# game=[1,2,0,3,5,7,6,4,8]
game = [3,1,2,4,5,0,6,7,8]
open=[[game.copy(),0]]
# possible_perm(game,0)
# for i in range(1):
#     next_state()
while(not next_state()):
    # inpust = input()
    comparaison+=1
print(game)
print("Noeuds Visités",compteur)
print(comparaison)
# next_state(open)
# print(open)
# next_state(open)
# print(game)
# print(open)
# print("test")
# print(positionDistance(0,8))
# 
