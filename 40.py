age = 42

if age < 4:
    price = 0

elif age < 18:
    price = 5

elif age < 65: 
    price = 10
    
elif age >= 65:             # Else block can be omittetd from if-elif-elsse chain
    price = 5

print ("Your admission cost is $" + str(price) + '.')

