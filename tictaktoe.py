grid=[['-','-','-'],['-','-','-'],['-','-','-']]
def printgrid(grid):
    for i in grid:
        print('---------')
        x=' | '.join(i)
        print(x)
    print('---------')
def winner(grid):
    if ((grid[0][0]=='x' and grid[0][1]=='x' and grid[0][2]=='x')or(grid[1][0]=='x' and grid[1][1]=='x' and grid[1][2]=='x')or(grid[2][0]=='x' and grid[2][1]=='x' and grid[2][2]=='x'))or((grid[0][0]=='x' and grid[1][0]=='x' and grid[2][0]=='x')or(grid[0][1]=='x' and grid[1][1]=='x' and grid[2][1]=='x')or(grid[0][2]=='x' and grid[1][2]=='x' and grid[2][2]=='x'))or((grid[0][0]=='x' and grid[1][1]=='x' and grid[2][2]=='x')or(grid[0][2]=='x' and grid[1][1]=='x' and grid[2][0]=='x')):
        return 0
    elif ((grid[0][0]=='y' and grid[0][1]=='y' and grid[0][2]=='y')or(grid[1][0]=='y' and grid[1][1]=='y' and grid[1][2]=='y')or(grid[2][0]=='y' and grid[2][1]=='y' and grid[2][2]=='y'))or((grid[0][0]=='y' and grid[1][0]=='y' and grid[2][0]=='y')or(grid[0][1]=='y' and grid[1][1]=='y' and grid[2][1]=='y')or(grid[0][2]=='y' and grid[1][2]=='y' and grid[2][2]=='y'))or((grid[0][0]=='y' and grid[1][1]=='y' and grid[2][2]=='y')or(grid[0][2]=='y' and grid[1][1]=='y' and grid[2][0]=='y')):
        return 1
    return 2
def makemovex(grid):
  try:
    x=int(input('enter the position for x(1-9): '))
    if x==1:
        if grid[0][0]=='-':
            grid[0][0]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==2:
        if grid[0][1]=='-':
            grid[0][1]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==3:
        if grid[0][2]=='-':
            grid[0][2]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==4:
        if grid[1][0]=='-':
            grid[1][0]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==5:
        if grid[1][1]=='-':
            grid[1][1]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==6:
        if grid[1][2]=='-':
            grid[1][2]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==7:
        if grid[2][0]=='-':
            grid[2][0]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==8:
        if grid[2][1]=='-':
            grid[2][1]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    elif x==9:
        if grid[2][2]=='-':
            grid[2][2]='x'
            printgrid(grid)
            k=winner(grid)
            if k==0:
                print('x is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovex(grid)
    else:
        print('enter position only between 1 and 9')
        makemovex(grid)
    return 0
  except:
      print('enter correct position')
      makemovex(grid)
def makemovey(grid):
  try:
    x=int(input('enter the position for y(1-9): '))
    if x==1:
        if grid[0][0]=='-':
            grid[0][0]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==2:
        if grid[0][1]=='-':
            grid[0][1]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==3:
        if grid[0][2]=='-':
            grid[0][2]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==4:
        if grid[1][0]=='-':
            grid[1][0]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==5:
        if grid[1][1]=='-':
            grid[1][1]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==6:
        if grid[1][2]=='-':
            grid[1][2]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==7:
        if grid[2][0]=='-':
            grid[2][0]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==8:
        if grid[2][1]=='-':
            grid[2][1]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    elif x==9:
        if grid[2][2]=='-':
            grid[2][2]='y'
            printgrid(grid)
            k=winner(grid)
            if k==1:
                print('y is winner')
                return 1
        else:
            print('value is already present please enter correct position :')
            makemovey(grid)
    else:
        print('enter position only between 1 and 9')
        makemovey(grid)
    return 0
  except:
      print('enter correct position')
      makemovey(grid)
i=0
won=False
while True:
    k=makemovex(grid)
    if k==1:
        won=True
        break
    if (('-' not in grid[0])and('-' not in grid[1])and('-' not in grid[2])):break
    m=makemovey(grid)
    if m==1:
        won=True
        break
if won==False:print('Draw')
