bid={}
while True:
    name=input('what is your name? ')
    abid=int(input('what is your bid amount? '))
    bid[name]=abid
    q=int(input('are there any more bidders? , 1 for yes 0 for no : '))
    if q==1:
        True # type: ignore
    else:
        break

s = max(bid.values())

for j in bid:
    if bid[j]==s:
        print(f'{j} is the winner')