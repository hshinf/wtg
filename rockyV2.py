import random

version = '2.0'

korean = {'Jogeum' : ['Gom Tang Eee', 'Myunga', 'JangWon'], 'Jotna' : ['Bon Chon', 'BBQ', 'Chugajib']}
american = {'Jogeum' : ['Ihop', '7-11', 'Mcdonald'], 'Jotna' : ['Golden Corral', 'Five Guys','Smoke Dat Grass', 'Ciro\'s Pizza']}
other = {'Jogeum' : ['Pho', 'Redo', 'Panda Express'], 'Jotna' : ['Manassas Hibachi', 'Chantilly Hibachi', 'Oolalala']}

print('Welcome To Rocky Rambo Random Food Generator ' + version)
n = input('Select korean, american, or other\n')

while True:
    if n == '':
        print('DumbFuck type korean or american or other\n')
        n = input('Select korean, american, or other\n')
    else: 
        x = input('Hunger Level: jogeum or jotna\n')
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


