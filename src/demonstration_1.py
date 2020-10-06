"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*



UPER 

UNDERSTAND 
- our goal is to remove the duplicates
- the array is already sorted
- numbers don't have to be consecuctive 
- assumed to all be integers 

PLAN 
- turn the list into a set --> automatically remove duplicates (what sets do)
- turn into a dictionary --> dictionaries can't have more than one explicit key 
- loop in a loop to check each variable against the other variables 

EXECUTE
"""

# turn the list into a set --> automatically remove duplicates (what sets do)
# RUNTIME: O(n)
# SPACE: O(n)
def remove_duplicates(nums):
    nums_set = set(nums)
    # or
    for nums in nums:
        nums_set.add(num)

    return list(nums_set)


# loop in a loop to check each variable against the other variables 
# RUNTIME: O(1) + O(n ^ O(1) + O(n)) --> O(n ^ 2)
# SPACE: O(1) --> there is no space used 
def remove_duplicates(nums):
    # in place means we don't use extra space -- 
    # ie we have to swap / move nums around in the given 
    i = 0                           # O(1)
    while i < len(nums) - 1:        # runs how many times? O(n)
        if nums[i] == nums[i+1]:    # O(1)
            nums.pop(i+1)           # O(n)
        else:
            i = i + 1
    return nums 


#RUNTIME: O(n) --> since the list is only being iterated through once 
# (even with two indecies)
def remove_duplicates_in_place_linear(nums):
    # keep one idx pointing to the end of the part of the array with duplicates 
    non_duplicate_index = 0  

    # and another idx pointing to the current element in the array
    # iterate through the list 
    for current_index in range(len(nums)):
        # if the current element is already in the array
        if nums[current_index] == nums[current_index]:
            # skip it
            continue
        else:
            # otherwise, set nums[num_duplicate_index] to the current element 
            nums[non_duplicate_index] = current[current_index]
            # and incremement non_duplicate_index
            non_duplicate_index += 1 
    
    return nums, non_duplicate_index
    