T = int(input())
for tc in range(1,T+1):

    nums = list(input().split())
    result = []
    for i in range(len(nums)):
        if nums[i] == 'ZRO' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'ONE' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'TWO' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'THR' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'FOR' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'FIV' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'SIX' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 'SVN' :
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 8:
            result += nums[i]

    for i in range(len(nums)):
        if nums[i] == 9 :
            result += nums[i]


    print(result)