phones = [ 'apple', "samsung", 'moto', 'spice', 'lenovo' ]

print("Here is the original list:")
print(phones)

print("\nHere is the sorted list:")
print(sorted( phones ))                          # sorted() function temporarily sorts list list in alphabetical order

print("\nHere is the original list again:")
print(phones)

print("\nHere is the reverse sorted list:")
print(sorted( phones , reverse = True ))         # sorted() function temporarily sorts list list in reverse alphabetical order with reverse=True arguement

print("\nHere is the original list again:")
print(phones)

message = sorted(phones)
print("\nHere is the sorted list using sorted() in variable:")
print (message)
