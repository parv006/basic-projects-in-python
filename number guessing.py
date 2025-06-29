actual=40
level=input('what level do you want to play , h for hard and e for noob: ')
attempts=10
if level=='e' or 'E':    
    attempts=10
if level=='h' or level=='H':
    attempts=5
else:
    print('invalid input')
def game(attempts):
    i=0
    for i in range(attempts):
        guess=int(input('enter your guess: '))
        if guess>actual:
            print('too high')
            print(f'you have {attempts-i-1} attempts left \n')
        elif guess<actual:
            print('too low')
            print(f'you have {attempts-i-1} attempts left \n')
        if guess==actual:
            print('you won!!!!!!!!!')
            break    
    if i+1==attempts:
        print('you lose')        
        
game(attempts)        

