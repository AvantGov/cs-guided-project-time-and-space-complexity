"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""


"""
UNDERSTAND 
- return true if there are any repeated values 
- return false if all are unique 

PLAN

#1
- make a new set 
- if the set length wasn't equal to the array length, that means there were duplicates
    - TIME: O(n)
    - SPACE: O(n)

#2
- sort the given set of numbers 
- iterate over the sorted list of items 
    - for each item, compare it to the next item 
    - if they are the same, then return True 
- if True is never returned, return False 

"""

# PLAN # 2
# TIME: O(n log n + n) --> O(n log n)
# SPACE: 
def contains_duplicates(nums):
    # create count iterator
    i = 0                   # O(1)
   
    #sort the nums given, in place  
    nums.sort()             # O(n log n)

    # for each num,
    while i < len(nums) - 1:    #O(n)
        # compare the num next to current num
        if nums[1] == nums[i+1]:        # O(1)    
            return True
            i += 1
        else: 
            i += 1
            continue
    return False
