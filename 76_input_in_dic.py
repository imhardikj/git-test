responses = {}

polling_active = True

while polling_active:
    
    name = input("\nWhat is your name? ")
    player = input("Who is your favourite player. ")
    
    responses[name] = player
    
    repeat = input("\nWould you like someone else to answer this poll? (yes/no) ")
    
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name.title() + "'s favourite player is " + response.title() + ".")
