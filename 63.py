favorite_languages = {       
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        for language in languages:
            print ("\n" + name.title() + "'s favourite language is " + language.title())
    
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    
        for language in languages:
            print("\t" + language.title())

