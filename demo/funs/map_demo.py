
#
# nums = [-10, 2, 4, 5, - 20]
#
# for n in map(abs , nums):
#     print(n)

st = "10,20,30,44,55"
nums = map(int, st.split(","))
print(sum(nums))

