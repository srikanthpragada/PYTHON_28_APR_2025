def compare_lists(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    return s1 == s2

lst1 = [10, 20, 30]
lst2 = [30, 10, 10, 20]
lst3 = [30, 10, 40]

print(compare_lists(lst1, lst2))
print(compare_lists(lst1, lst3))

