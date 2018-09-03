unverified_users = ['alan', 'bree', 'candace', 'rick',]
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()
    
    verified_users.append(current_user)
    
    print ("Verifying user: " + current_user.title())

print ("\nThe newly verified users are:")

for user in verified_users:
    print(user.title())
