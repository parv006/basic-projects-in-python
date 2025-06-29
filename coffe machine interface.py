import time
resources={'coffee':300 , 'water':1000 , 'milk':5000}
password=1111
global money
money=0
price={'espresso':1,'latte':3,'cappuccino':2}
pas=0
coffee_recipes = {
    "espresso": {
        "coffee_g": 10,
        "water_ml": 30,
        "milk_ml": 0
    },
    "latte": {
        "coffee_g": 10,
        "water_ml": 30,
        "milk_ml": 210
    },
    "cappuccino": {
        "coffee_g": 10,
        "water_ml": 30,
        "milk_ml": 120
    }
}

def sufficient_res(choice):
    if choice=='espresso':    
        res_lis=list(coffee_recipes['espresso'].values())
        if res_lis[0]>resources['coffee'] or res_lis[1]>resources['water'] or res_lis[2]>resources['milk']:
            return False
        else:
            return True    
    if choice=='latte':   
        res_lis2=list(coffee_recipes['latte'].values())
        if res_lis2[0]>resources['coffee'] or res_lis2[1]>resources['water'] or res_lis2[2]>resources['milk']:
            return False
        else:
            return True 
    if choice=='cappuccino':
        res_lis3=list(coffee_recipes['cappuccino'].values())
        if res_lis3[0]>resources['coffee'] or res_lis3[1]>resources['water'] or res_lis3[2]>resources['milk']:
            return False
        else:
            return True
  
def reduce(choice):
   
    if choice=='espresso':
        res_lis=list(coffee_recipes['espresso'].values())
        resources['coffee']=resources['coffee']-res_lis[0]
        resources['water']=resources['water']-res_lis[1]
        resources['milk']=resources['milk']-res_lis[2]
        
    elif choice=='latte':
        res_lis=list(coffee_recipes['latte'].values())
        resources['coffee']=resources['coffee']-res_lis[0]
        resources['water']=resources['water']-res_lis[1]
        resources['milk']=resources['milk']-res_lis[2]
        
    elif choice=='cappuccino':
        res_lis=list(coffee_recipes['cappuccino'].values())
        resources['coffee']=resources['coffee']-res_lis[0]
        resources['water']=resources['water']-res_lis[1]
        resources['milk']=resources['milk']-res_lis[2]
def cashier_desk(choice):
    global money
    money=0
    quarters=int(input('quarters(0.25$): '))
    dimes=int(input('dimes(0.10$): '))
    nickel=int(input('nickel(0.05$): '))
    pennies=int(input('pennies(0.01$): '))
    total=quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01
    global change
    change=total-price[choice]
    if change>=0:
        print(f'here is your change {round(change,2)}$')
        money=money+price[choice]
    elif change<0:
        print(f'not enough money for a {choice} ,{round(change ,2)}$ refunded , try again')
def loading(choice):
    print(f'{choice} making in progress. ')
    time.sleep(0.5)              
    print(f'{choice} making in progress.. ')
    time.sleep(0.5)              
    print(f'{choice} making in progress... ')
    time.sleep(0.5)              
    print(f'{choice} making in progress.... ') 
    time.sleep(0.5)             
    print(f'{choice} almost ready ')
    time.sleep(0.5)
    print(f'your {choice} is ready  ')              

while True:
    choice=input('What would you like? (espresso/latte/cappuccino): ')
    choice=choice.lower()
    try:
        if choice!='espresso' and choice!='latte' and choice!='cappuccino' and choice!='off' and choice !='report':
            print('invalid imput , plz try again.')
            continue
        if choice=='off':
            pasw=int(input('enter the 4 digit pincode to turn off the machine: '))
            if pasw==password:
                print('shutting down....')
                time.sleep(0.5)
                print('power off')
                break
            elif pasw!=password:
                print('access denied. ')
                continue
        if choice=='report':
            pas=int(input('enter the 4 digit numeral password: '))
            if pas==password:
                print(f"coffee = {resources['coffee']}g \nwater = {resources['water']}ml \nmilk = {resources['milk']}ml")
                print(f'money = {money}$')
                continue
            elif pas!=password:
                print('wrong password , access denied ...') 
                continue
        if sufficient_res(choice)==False:
            print(f'sorry for the inconvinience caused , but we do not have the required resources to make {choice} , left resources : {resources}')
            continue
        elif sufficient_res(choice)==True:
            pass
        quarters=int(input('quarters(0.25$): '))
        dimes=int(input('dimes(0.10$): '))
        nickel=int(input('nickel(0.05$): '))
        pennies=int(input('pennies(0.01$): '))
        total=quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01
        change=total-price[choice]
        if change>=0:
            reduce(choice)
            print(f'here is your change {round(change,2)}$')
            money=money+price[choice]
        elif change<0:
            print(f'not enough money for a {choice} ,{-1*(round(change ,2))}$ refunded , try again')
            continue
        loading(choice)
        print(f'here is your {choice} , enjoy  ;)  ')
    except ValueError or TypeError:
        print('invalid input , please check your spelling... ')