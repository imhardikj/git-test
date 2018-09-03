aliens = []

for alien_number in range(50):
    new_alien = {'color' : 'green', 'speed' : 'slow', 'points': 5}
    aliens.append(new_alien)
    
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'medium'
        alien['points'] = 10
  
for alien in aliens[:7]:
    print(alien)
