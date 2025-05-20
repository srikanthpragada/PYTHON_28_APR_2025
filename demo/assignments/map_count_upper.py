def count_upper(name):
    count = 0
    for c in name:
        if c.isupper():
            count += 1

    return count


names = ['Scott Guthrie', 'Larry Page', 'Tim', 'Ellison']

for count in map(count_upper, names):
    print(count)

