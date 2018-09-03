favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby ',
    'phil': 'python',
    }

print ("The foolowing languages are mentioned:")

for language in sorted(set(favorite_languages.values())):
    print (language.title())

