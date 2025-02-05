def validate(n):
    count, nums = 0, []
    for i in str(n):
        nums.append(int(i))
    if len(nums) % 2 == 0:
        for i in range(len(nums)):
            if count % 2 == 0:
                nums[i] *= 2
                if nums[i] > 9:
                    nums[i] -= 9
            count += 1
    else:
        for i in range(len(nums)):
            if count % 2 != 0:
                nums[i] *= 2
                if nums[i] > 9:
                    nums[i] -= 9
            count += 1
    return sum(nums) % 10 == 0
