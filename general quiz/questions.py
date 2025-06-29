from ques_bank import ques
import random
class RandomQuestion:
    def quesion():    
        qa=[]
        qlis=ques.quest
        keylis=list(qlis.keys())
        ran=random.choice(keylis)
        qa.append(qlis[ran]['question'])
        qa.append(qlis[ran]['answer'])
        return qa
       