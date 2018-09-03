def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    
    profile = {}
    
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        if user_info['tow_package']:
            user_info['tow_package'] = 'Yes'
            profile[key] = value
        else:
            user_info['tow_package'] = 'No'
            profile[key] = value
    return profile
    
user_profile = build_profile('subaru', 'outback', color='blue', tow_package=False)

print(user_profile)

