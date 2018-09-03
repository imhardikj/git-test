favorite_languages = { 'jen': 'python', 'sarah': 'c', 
    'edward': 'ruby', 'phil': 'python',}

friends = ['phil', 'edward']

for name in favorite_languages.keys():                  # No need to use keys()
    print(name.title())                                 # because its default behaviour when looping through dictionary
    
    if name in friends:
        print ( "Hi " + name.title() +
        ", I see  see you favourite language is " +
        favorite_languages[name].title() + "!")
