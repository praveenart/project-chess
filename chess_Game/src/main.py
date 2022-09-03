
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
    if x+y==ex+ey or abs(int(str(x)+str(y))-int(str(ex)+str(ey)))%11==0: #another method for check the diagonal  [ x-ex == y-ey ]
        return True
    print("Diagonal error")
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ L MOVE BY THE HORSE]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def lmove(x,y,ex,ey):
    if abs(x-ex)==2 and abs(y-ey)==1: # another method for l'move is [(abs(x-ex),abs(y-ey)) in ((3,1),(1,3))]
        return True
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[INCREMENT THE LOOP]]]]]]]]]]]]]]]]]]]]]]]]
def increment(x,y,ex,ey):
    global grid

    if x==ex:                          #straight check
        for i in range(y+1,ey+1):
            if grid[x][i] !="..":
                print("straight check error 1 I")
                return False
        return True
    elif y==ey:                         #straight check
        for i in range(x+1,ex+1):
            if grid[i][y]!="..":
                print("straight check error 2 I")
                return False
        return True
    elif x!=ex and y!=ey:                                                        #diagonal check
        if x<ex and y<ey:
            for i,j in zip(range(x+1,ex+1),range(y+1,ey+1)):
                if grid[i][j]!="..":
                    print("diagonal check 1 error I")
                    return False
            return True
        elif x<ex and y>ey:
            for i,j in zip(range(x+1,ex+1),range(y-1,ey+1,-1)):
                if grid[i][j]!="..":
                    print("diagonal check 2 error I")
                    return False
            return True
    return False

#[[[[[[[[[[[[[[[[[[[[[[[[DECREMENT IN THE LOOP]]]]]]]]]]]]]]]]]]]]]]]]
def decrement(x,y,ex,ey):
    global grid

    if x==ex:                                                     #straight check
        for i in range(y-1,ey+1,-1):
            if grid[x][i]!="..":
                print("straight check error 1 D")
                return False
        return True
    elif y==ey:                                                    #straight check
        for i in range(x-1,ex+1,-1):
            if grid[i][y]!="..":
                print("striaght check error 2 D")
                return False
        return True
    elif x!=ex and y!=ey:                                                       #diagonal check
        if x>ex and y>ey:
            for i,j in zip(range(x-1,ex+1,-1),range(y-1,ey+1,-1)):
                if grid[i][j]!="..":
                    print("diagonal check 1 error D",i,j)
                    return False
            return True
        elif x>ex and y<ey:
            for i,j in zip(range(x-1,ex+1,-1),range(y+1,ey+1)):
                if grid[i][j]!="..":
                    print("diagonal check error 2 D")
                    return False
            return True
    return False
    

#[[[[[[[[[[[[[[[[[[[[[[[[CHECK THE OBSTACLE IN THE DIAGONAL LINE INBETWEEN THE START AND THE END POINT ]]]]]]]]]]]]]]]]]]]]]]]]
def is_diagonal_block(x,y,ex,ey):
    if (int(str(ex)+str(ey))>int(str(x)+str(y))):
        if increment(x,y,ex,ey) is True:
            return True
        return False
    else:
        if decrement(x,y,ex,ey) is True:
            return True
        return False

#[[[[[[[[[[[[[[[[[[[[[[[[CHECK THE OBSTACAL IN THE STRIGHT LINE INBETWEEN THE START AND END POINT]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def is_straight_block(x,y,ex,ey):
    if ex+ey>x+y:
        if increment(x,y,ex,ey) is True:
            return True
        return False
    else:
        if decrement(x,y,ex,ey):
            return True
        return False

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[MOVE THE COIN ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
def movable(coin,x,y,ex,ey):
    if coin[1]=="P":
        if (straight(x,y,ex,ey) or diagonal(x,y,ex,ey)) and (abs(x-ex)<=1 or abs(y-ey)<=1):
            if coin[0]=="B" and ex>x:
                return True
            elif coin[0]=="W" and x>ex:
                return True
            return False
        return False
    elif coin[1]=="Q":
        if (straight(x,y,ex,ey) or diagonal(x,y,ex,ey)) and (is_diagonal_block(x,y,ex,ey) or is_straight_block(x,y,ex,ey)):
            return True
        print("invalid move")
        return False
    elif coin[1]=="R":
        if straight(x,y,ex,ey) and is_straight_block(x,y,ex,ey):
            return True
        print("INvalid move")
        return False
    elif coin[1]=="H":
        if lmove(x,y,ex,ey):
            return True
        print("invalid move")
        return False
    elif coin[1]=="B" :
        if diagonal(x,y,ex,ey) and is_diagonal_block(x,y,ex,ey):
            return True
        print("invalid move")
        return False
    elif coin[1]=="K":
        if (straight(x,y,ex,ey) or diagonal(x,y,ex,ey)) and (abs(x-ex)<=1 and abs(y-ey)<=1):
            return True
        print("invalid move")
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
        x,y=map(int,input("Enter the start point : ").split())
        ex,ey=map(int,input("Enter the end point : ").split())
        result=valid_move(x,y,ex,ey)
        turn=0
    else:
        print("Black's move !!!")
        x,y=map(int,input("Enter the start point : ").split())
        ex,ey=map(int,input("Enter the end point : ").split())
        result=valid_move(x,y,ex,ey)
        turn=1
        

init_grid()

while True:
    move()
    print_grid()
    print("\n")
    
