from questions import RandomQuestion
# print(RandomQuestion.quesion())
ques_no=0
correct=0
howmany=int(input('how many questions do you want your quiz to have '))
for i in range(howmany):
    ques=RandomQuestion.quesion()
    print(f'Q.{ques_no+1})  {ques[0]}')
    userans=input('(True/False)?: ')
    userans=userans.title()
    boolans=False
    if userans=='True' or userans=='Yes':
        boolans=True
    elif userans=='False' or userans=='No':
        boolans=False
    else:
        boolans=None    

    if boolans==ques[1]:
        print('you are correct !!')
        correct+=1
    elif boolans!=ques[1]:
        print('wrong ans. ')
    elif boolans==None:
        print('invalid input ')    
    print(f'your score: {correct}/{ques_no+1}')        
    ques_no+=1
print(f'you scored {correct}/{ques_no}')    