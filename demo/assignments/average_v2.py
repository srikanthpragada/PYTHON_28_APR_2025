def average(*nums, positive=False):
    if not positive:
        return sum(nums) / len(nums)
    else:
        total = 0
        count = 0
        for n in nums:
            if n > 0:
                total += n
                count += 1

        return total / count


print(average(10, 20, -30, 40))
print(average(1, 2, 30, -50, positive=True))

