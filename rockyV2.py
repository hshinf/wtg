import random

korean = {'Jogeum' : ['GomTangEee', 'Myunga', 'JangWon'], 'Jotna' : ['BonChon', 'BBQ', 'Chugajib']}
american = {'Jogeum' : ['Ihop', 'SevenEleven', 'Mcdonald'], 'Jotna' : ['GoldenCorral', 'FiveGuys','SmokeDatGrass']}
other = {'Jogeum' : ['Pho', 'Redo', 'PandaExpress'], 'Jotna' : ['ManassasHibachi', 'ChantillyHibachi', 'Oolalala']}

print('Welcome To Rocky Rambo Random Food Generator v.1')
n = input('Select korean, american, or other')

while True:
    if n == '':
        print('DumbFuck type korean or american or other')
        n = input('Select korean, american, or other')
    else: 
        x = input('Hunger Level: jogeum or jotna')
        while True:
    
            if n == 'korean' and x == 'jogeum' :
                print(random.choice(korean['Jogeum']))
                break
            elif n == 'korean' and x == 'jotna' :
                print(random.choice(korean['Jotna']))
                break
            elif n == 'american' and x == 'jogeum' :
                print(random.choice(american['Jogeum']))
                break
            elif n == 'american' and x == 'jotna' :
                print(random.choice(american['Jotna']))
                break
            elif n == 'other' and x == 'jogeum' :
                print(random.choice(other['Jogeum']))
                break
            elif n == 'other' and x == 'jotna' :
                print(random.choice(other['Jotna']))
                break
        break


print('LEEEEEGGGGOOOO!!!! Move It Move It')


