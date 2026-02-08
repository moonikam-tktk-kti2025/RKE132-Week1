#kirjutada programm, mis küsib kasutajalt nime ja tervitab teda nimepidi

#Algus
#Küsi kasutajalt eesnimi
#Salvesta väärtus muutujasse first_name
#Väljasta tervitust: 'Hello, first_name!'
#Lõpp

#first_name = input('Enter your first name:')
#print('Hello, ' + first_name + '!')

#f-string
#print(f'Hello, {first_name}!')

# Teeme nii, et programm küsiks kasutajatelt mitte ainult eesnime, vaid ka perekonnanime ning tervitaks teda nime ja perekonnanimega.

first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
#print('Hello, ' + first_name + '!')

#f-string
print(f'Hello, {first_name} {last_name}!')