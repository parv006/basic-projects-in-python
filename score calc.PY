def calculate_love_score():
    name1=str(input('name 1: '))
    name2=str(input('name 2: '))
    name=name1+name2
    b=[]
    for i in name:
        i=i.upper()
        b.append(i)

    
    T=b.count('T')    
    R=b.count('R')
    U=b.count('U')
    E=b.count('E')
    L=b.count('L')
    O=b.count('O')
    V=b.count('V')
    E=b.count('E')
    print(f'your love score is : {str(T+R+U+E)+str(L+O+V+E)}')
calculate_love_score()
