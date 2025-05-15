def wish(*names, message='Hi'):
    for n in names:
        print(message, n)


wish("Larry", "Peter", 'Mark', message='Hello')
wish("Garry")
