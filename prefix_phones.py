#PLAN
    # for reach number in numbers: 
        # compare each to every other number 
            # if one of the numbers is a prefix of the other number
                # return False
        # if not found, return True


# TIME O(n ^ 2) --> there is a nested for loop in this operation
# SPACE 
def prefixFreePhones(nums):
    for num in nums:                # O(n)
        for other_num in nums:      # O(n)
            if num == other_num:    # O(1)
                continue
            if other_num.startswith(num) or num.(startswith(other_num)): #O(1)
                return False
    return True

#VER 2 sorting the numbers first 
# TIME O(n log n)
def prefixFreePhones(nums):
    # sorted 
    nums.sort()

    #iterate through 
    for i in range(len(nums) - 1):
        
        # assign values for the two values being compared
        first = numbers[i]
        second = numbers[i+1]

        # if the first selection is a prefix of the second, return True 
        if second.startswith(first):
            return False 
    
    # else, return false 
    return True