alien_0 = { 'x-position': 0, 'y-positon': 25, 'speed': 'medium'}
print ("original X-Position: " + str(alien_0['x-position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # This Must be fast alien.
    x_increment = 3
    
alien_0['x-position'] = alien_0['x-position'] + x_increment

print ("New X-Position: " + str(alien_0['x-position']))
