# Positional-only args
def wish(message, person, /):
    print(message, person)


#wish(person  = "Jack", message = "Hi")
wish("Hi", "Tom")