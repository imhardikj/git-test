def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person
    
musician = build_person('jimi', 'hendrix')
print(musician)
