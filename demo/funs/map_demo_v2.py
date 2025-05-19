
st = "10,20,30,a,44,55"
num_parts = filter(str.isdigit, st.split(","))
nums = map(int,num_parts)
print(sum(nums))

