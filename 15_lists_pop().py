phones = [ 'apple', "samsung", 'moto', 'spice', 'lenovo' ]
print (phones)

phone_1 = phones.pop()

print ( "\n" + str(phones) )        # List is inlcuded in str() 

message_1 = "\nMy latest phones is of " + phone_1.title() + "."
print (message_1)

phone_2 = phones.pop(-4)

message_2 = "\nMost expensive phone is of " + phone_2.title() + "."
print (message_2)

