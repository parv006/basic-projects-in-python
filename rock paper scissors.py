import random as rd
choices=['rock','paper','scissors']
while True:

    i=rd.randint(1,3)

    p=int(input('write 1 for rock , 2 for paper , 3 for scissors'))
    if p==i:
        print('draw')

    elif p==1 and i==2:
        print('you lose')

    elif p==1 and i==3:
        print('you win')

    elif p==2 and i==1:
        print('you win')
    elif p==2 and i==3:
        print('you lose')
    elif p==3 and i==1:
        print('you lose')
    elif p==3 and i==2:
        print('you win')
    else:
        print('invalid input')
    print('computer choice:',choices[i-1])
    print('your choice:',choices[p-1])        
    print('do you want to play again')
    play=input('yes or no')
    if play=='yes':
        continue
    else:
        break   