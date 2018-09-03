planet = 'earth'

print (planet == 'earth')                  # checking equality
print (planet == 'mars')

planet_1 = 'EartH'

print (planet_1.lower() == 'earth')        # Ignoring case when checking inequality

print (planet != 'venus')                  # checking inequality

if planet != 'venus':
    print ("It must be Earth")

age_1 = 15                                 # numerical comparison
age_2 = 24

print ( age_1 > 18 and age_2 > 18 )
print ( age_1 > 18 or age_2 > 18 )

age_1 = 21

print ( age_1 > 18 and age_2 > 18 )
print ( age_1 < 18 or age_2 < 18 )

banned_users = ['abcd', 'berzek', 'qwerty']
user = 'asdf'
if user not in banned_users:
    print ('Welcome to !@#$%^&')
