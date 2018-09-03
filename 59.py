aliens = []

for alien_number in range(50):
    new_alien = {'color' : 'green', 'points': 5}
    aliens.append(new_alien)
    
for alien in aliens[:7]:
    print(alien)
    
print ("\nTotal number of aliens: " + str(len(aliens)))
