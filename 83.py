def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

user = input ("Enter a name. ")
greet_user(user)
