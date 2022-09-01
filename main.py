
grid=[([".."]*8)[:] for i in range(8)]

turn=1

# W-white coin | B-black coin

# K-king | Q-queen | P-pawn | B-bishop | H-horse | R-rook

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[INITITATE THE GRID]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def init_grid():
    global grid

    arr=["R","H","B","K","Q","B","H","R"]

    for i in range(8):
        grid[0][i]="B"+arr[i]
        grid[1][i]="BP"

    for i in range(8):
        grid[7][i]="W"+arr[i]
        grid[6][i]="WP"

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[DISPLAY THE BOARD]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def print_grid():
    global grid

    for i in range(8):
        for j in range(8):
            print(grid[i][j],end=" ")
        print()

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[STRAIGHT MOVE]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def straight(x,y,ex,ey):
    if x==ex or y==ey:#another method to check the straight [ abs((x+y)-(ex+ey))==10 or abs((x+y)-(ex-ey))<8]
        return True
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[DIAGONAL MOVE ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def diagonal(x,y,ex,ey):
    if x+y==ex+ey or abs((x+y)-(ex+ey))%11==0: #another method for check the diagonal  [ x-ex == y-ey ]
        return True
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ L MOVE BY THE HORSE]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def lmove(x,y,ex,ey):
    if abs(x-ex)==2 and abs(y-ey)==1: # another method for l'move is [(abs(x-ex),abs(y-ey)) in ((3,1),(1,3))]
        return True
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[MOVE THE COIN ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def movable(coin,x,y,ex,ey):
    if coin[1]=="P":
        return True
    elif coin[1]=="Q":
        if straight(x,y,ex,ey) or diagonal(x,y,ex,ey):
            return True
        return False
    elif coin[1]=="R":
        if straight(x,y,ex,ey):
            return True
        return False
    elif coin[1]=="H":
        if lmove(x,y,ex,ey):
            return True
        return False
    elif coin[1]=="B":
        if diagonal(x,y,ex,ey):
            return True
        return False
    elif coin[1]=="K":
        if straight(x,y,ex,ey) or diagonal(x,y,ex,ey):
            return True
        return False
    else:
        return False 


#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[CHECK THE MOVEMENT IS VALID OR NOT]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def valid_move(x,y,ex,ey):
    global turn,grid

    coin=grid[x][y]
    end_coin=grid[ex][ey]

    if coin==".." or (turn==1 and (coin[0]=="B" or end_coin[0]=="W")) or (turn==0 and (coin[0]=="W" or end_coin[0]=="B")):
        print("invalid")
        return False
    else:
        result=movable(coin,x,y,ex,ey)
        if result is True:
            grid[ex][ey]=coin
            grid[x][y]=".."
        else:
            print("Invalid move ... Given end is not reached")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ MAKE MOVEMENT]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def move():
    global turn 

    if turn==1:
        print("white's move !!!")
        x,y=map(int,input("Enter the start point").split())
        ex,ey=map(int,input("Enter the end point").split())
        result=valid_move(x,y,ex,ey)
        turn=0
    else:
        print("Black's move !!!")
        x,y=map(int,input("Enter the start point").split())
        ex,ey=map(int,input("Enter the end point").split())
        result=valid_move(x,y,ex,ey)
        turn=1
        

init_grid()

while True:
    move()
    print_grid()
    print("\n")
