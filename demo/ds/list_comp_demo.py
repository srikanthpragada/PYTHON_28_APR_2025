squares = []

for n in range(1, 11):
    squares.append(n * n)

print(squares)

# list comprehension
squares = [n * n for n in range(1, 11)]
print(squares)
