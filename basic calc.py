def calc(n1 , n2 , op):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='/':
        return n1/n2
    elif op=='*':
        return n1*n2
    else:
        return 'invalid operator'
n1=int(input('enter 1st number : '))    
n2=int(input('enter 2nd number : '))    
op=input('select operator: \n + \n - \n / \n * \n')
res=calc(n1, n2 ,op)
print(res)
while True:
    des=input('y to continue with current value or n for new calc or any other key for exit : ')
    if des=='y':
        n2=int(input('enter the next number: '))
        op=input('select operator: \n + \n - \n / \n * \n')
        print(calc(res , n2 , op))
        res=calc(res,n2,op)
    elif des=='n':
        n1=int(input('enter 1st number : '))    
        n2=int(input('enter 2nd number : '))    
        op=input('select operator: \n + \n - \n / \n * \n')
        res=calc(n1, n2 ,op)
        print(res)
    else:    
        break
