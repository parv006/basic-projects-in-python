import random

celebs = {
    "Selena Gomez": ["American singer, actress, and producer known for her music career and role in 'Only Murders in the Building'", 421_000_000],
    "Dwayne Johnson": ["Actor, producer, and former wrestler popularly known as 'The Rock', with roles in blockbuster action films", 395_000_000],
    "Kylie Jenner": ["Entrepreneur and media personality, known for founding Kylie Cosmetics and starring in reality TV", 394_000_000],
    "Ariana Grande": ["Pop singer and actress known for her powerful vocals and roles in 'Victorious' and 'Wicked'", 376_000_000],
    "Kim Kardashian": ["Reality TV star, entrepreneur, and legal advocate famous for 'Keeping Up with the Kardashians'", 357_000_000],
    "Beyoncé": ["Global music icon and performer known for her work with Destiny's Child and solo success", 312_000_000],
    "Khloé Kardashian": ["Media personality and entrepreneur, best known for reality TV and co-founding Good American", 303_000_000],
    "Justin Bieber": ["Canadian pop singer who rose to fame via YouTube and known for hits like 'Peaches' and 'Sorry'", 294_000_000],
    "Kendall Jenner": ["Fashion model and television personality known for her work with top fashion brands and runway shows", 288_000_000],
    "Taylor Swift": ["Singer-songwriter renowned for narrative-driven music across genres like country, pop, and indie", 282_000_000],
    "Virat Kohli": ["Indian cricketer and former captain of the national team, admired for his athleticism and leadership", 272_000_000],
    "Jennifer Lopez": ["Actress, singer, and businesswoman known for her multi-decade career in entertainment and fashion", 249_000_000],
    "Neymar": ["Brazilian footballer known for his flair, skill, and play with PSG and the Brazilian national team", 229_000_000],
    "Nicki Minaj": ["Rapper, singer, and songwriter known for her bold style, lyrical flow, and chart-topping tracks", 226_000_000],
    "Kourtney Kardashian": ["Reality TV star and entrepreneur, co-founder of Poosh and known for her lifestyle branding", 219_000_000],
    "Miley Cyrus": ["Pop singer and actress known for her role as Hannah Montana and musical reinvention", 213_000_000],
    "Katy Perry": ["Pop star known for colorful music videos, chart-topping hits, and role as an 'American Idol' judge", 204_000_000],
    "Zendaya": ["Actress and singer acclaimed for roles in 'Euphoria' and 'Dune', as well as her fashion influence", 179_000_000],
    "Kevin Hart": ["Stand-up comedian and actor known for high-energy performances and comedic roles in movies", 177_000_000],
    "Cardi B": ["Rapper and entertainer known for her unfiltered personality, social media presence, and hit music", 164_000_000],
    "LeBron James": ["NBA star and philanthropist known for his dominance on the court and educational initiatives", 159_000_000],
    "Demi Lovato": ["Singer and actress known for her powerful voice, advocacy, and past Disney Channel roles", 153_000_000],
    "Rihanna": ["Pop and R&B artist turned business mogul, founder of Fenty Beauty and Savage X Fenty", 149_000_000],
    "Chris Brown": ["R&B singer and dancer recognized for his musical talent and high-energy performances", 144_000_000],
    "Drake": ["Canadian rapper and global music icon known for chart-topping albums and crossover appeal", 143_000_000],
    "Ellen DeGeneres": ["Comedian and TV host known for 'The Ellen DeGeneres Show' and her influence in daytime television", 136_000_000],
    "Billie Eilish": ["Grammy-winning singer-songwriter known for her haunting vocals and genre-defying sound", 124_000_000],
    "Kylian Mbappé": ["French football sensation known for his speed, skill, and success with PSG and France", 123_000_000]
}
r1=random.choice(list(celebs.keys()))
r2=random.choice(list(celebs.keys()))
def check_dup():
    while True:
        global r1
        global r2
        if r1==r2:
            r2=random.choice(list(celebs.keys()))
        else:
            break
check_dup()
win=0        

while True:
    if celebs[r1][1]>celebs[r2][1]:
        win=1
    elif celebs[r1][1]<celebs[r2][1]:
        win=2   
    score=0
    print(f'{r1} or {r2} \n')
    print(f'{r1} is {celebs[r1][0]}\n')
    print(f'{r2} is {celebs[r2][0]}\n')
    guess=int(input(f'1 for {r1} and 2 for {r2} \n'))
    if guess!=1 and guess!=2:
        print('invalid guess , try again out of 1 or 2 : ')
        break
    if guess==win:
        score+=1
        print('correct')
        r1=r2
        r2=random.choice(list(celebs.keys()))
        check_dup()
        print(f'score:{score}')
    elif guess!=win:
        print('wrong , you lose ')
        print(f'final score:: {score}')
        break
    elif score==30:
        print('you winnnnn!!!!!!!!!!!!!!!!!!!')
        print(f'final score:: {score}')
        break
    else:
        print('invalid , try again')
