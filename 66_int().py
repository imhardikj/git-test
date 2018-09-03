prompt = "Please enter your age: "

age = input(prompt)

print ( int(age) >= 18 )

if int(age) >= 18:
    print ("You are eligible to vote.")
else:
    print ("Sorry you can't vote.")
