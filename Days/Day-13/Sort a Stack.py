# https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.
# We can only use the following functions on this stack S.
# is_empty(S) : Tests whether stack is empty or not.
# push(S) : Adds a new element to the stack.
# pop(S) : Removes top element from the stack.
# top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.

# Note:
# 1) Use of any loop constructs like while, for..etc is not allowed.
# 2) The stack may contain duplicate integers.
# 3) The stack may contain any integer i.e it may either be negative, positive or zero.

# Constraints:
# 1 <= 'T' <= 100
# 1 <=  'N' <= 100
# 1 <= |'V'| <= 10^9
# Where |V| denotes the absolute value of any stack element.
# Time limit: 1 sec

# Sample Input1:
# 1
# 5
# 5 -2 9 -7 3
# Sample Output 1: 9 5 3 -2 -7
# Explanation: 9 Is the largest element, hence it’s present at the top. Similarly 5&gt;3, 3&gt;-2 and -7 being the smallest element is present at the last.

# Sample Input2:
# 1
# 5
# -3 14 18 -5 30
# Sample Output2: 30 18 14 -3 -5
# Explanation: 30 is the largest element, hence it’s present at the top. Similarly, 18&gt;14, 14&gt;-3 and -5 being the smallest element is present at the last.
# ------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Will break down the given array by popping one item per call and hold item in a variable say temp, till at the end we'll have an empty array and givenArray's first item in temp. From here we'll make calls to a helper function where we pass the temp and array (say as element and stack respectively) up-till that point hoping to sort these 2 entities i.e. fit that item into that array in a sorted order. In helperfunc we consider received array i.e. stack to be sorted and hence for the passed item i.e. element we directly check if it is greater than top of array or if the array is empty, in either case we directly append element on top of array. If that's not the case then we pop the item from stack and hold it in a temp variable hoping that newer top thus formed is smaller than the originally passed element in this helperfunc. With that hope we put a recursive call to helperfunc this time with this newly popped stack and same old element. When this stack comes returned having been sorted, we append on top the temp.
def helper(stack, element):
    if not len(stack) or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        helper(stack, element)
        stack.append(temp)

def sortStack(stack):
    if len(stack):
        temp = stack.pop()
        sortStack(stack)
        helper(stack, temp)
    return stack

print(sortStack([5, -2, 9, 7, 3]))
# TC: O(n^2) Explanation: Because if each call in sortStack to helper has to pop and traverse the whole array then as in the first call we'll only have one item i.e.5 then 5,-2 and thus from 1, 2,...n collectively calls will be made here, signalling n(n+1)/2 TC generalized as n^2.
# SC: O(n) Explanation: when sortStack is holding recursive space of n//2, stack will have n//2 items and at that time helper() in the sortStack can at max make n//2 further recursive call to itself thus in total worst n calls collectively for both sortStack and helper functions at any given time