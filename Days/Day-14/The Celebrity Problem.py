# https://www.codingninjas.com/studio/problems/the-celebrity-problem_982769?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# There are ‘N’ people at a party. Each person has been assigned a unique id between 0 to 'N' - 1(both inclusive).  A celebrity is a person who is known to everyone but does not know anyone at the party.
# Given a helper function ‘knows(A, B)’, It will returns "true" if the person having id ‘A’ know the person having id ‘B’ in the party, "false" otherwise. Your task is to find out the celebrity at the party. Print the id of the celebrity, if there is no celebrity at the party then print -1.

# Notes:
# 1. The helper function ‘knows’ is already implemented for you.
# 2. ‘knows(A, B)’ returns "false", if A doesn't know B.
# 3. You should not implement helper function ‘knows’, or speculate about its implementation.
# 4. You should minimize the number of calls to function ‘knows(A, B)’.
# 5. There are at least 2 people at the party.
# 6. At most one celebrity will exist.

# Constraints:
# 1 <= T <= 50
# 2 <= N <= 10^4
# Where ‘T’ is the total number of test cases, ‘N’ is the number of people at the party.
# Time Limit: 1sec

# Sample Input 1:
# 1
# 2
# Call function ‘knows(0, 1)’ // returns false
# Call function ‘knows(1, 0)’ // returns true
# Sample Output 1:
# 0
# Explanation For Sample Input 1:
# In the first test case, there are 2 people at the party. When we call function knows(0,1), it returns false. That means the person having id ‘0’ does not know a person having id ‘1'. Similarly, the person having id ‘1’  knows a person having id ‘0’ as knows(1,0) returns true. Thus a person having id ‘0’ is a celebrity because he is known to everyone at the party but doesn't know anyone.

# Sample Input 2:
# 1
# 2
# Call ‘knows(0, 1)’ // returns true
# Call ‘knows(1, 0)’ // returns true
# 2
# Call ‘knows(0, 1)’ // returns false
# Call ‘knows(1, 0)’ // returns false
# Sample Output 2:
# -1
# -1
# Explanation For Sample Input 2:
# In first test case, there are 2 people at the party. The person having id ‘0’ knows a person having id ‘1’. The person having id ‘1’  knows a person having id ‘0’. Thus, there is no celebrity at the party, because both know each other.
# In second test case, there are 2 people at the party. The person having id ‘0’ does not know a person having id ‘1’. The person having id ‘1’  also does not know a person having id ‘0’. Thus, there is no celebrity at the party, because both does not know each other.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a nested for-loop we'll check for each item with all the rest of them and if the celebrity condition that is the item is know by all but item doesnt know any, is true we'll return that item or at end return -1.
def findCelebrity(n, knows):
    for i in range(n):
        is_celebrity = True
        for j in range(n):
            if i != j and (knows(i, j) or not knows(j, i)): # We skip for the same item
                is_celebrity = False
                break
        if is_celebrity:
            return i
    return -1
# TC: O(n^2)
# SC: O(1)


# Approach2: Using stack we'll store items form 0 to n-1. Further in a while loop we'll keep popping top two items from stack and check whether either can be a celeb and if so it's pushed back. To check if it can be celeb it should not know the other candidate and when the condition violated it is not pushed back coz it cant be a celeb. If conditions work out we'll push back the item, and this we'll do uptill stack has more than one item left. On contrary if both items don't know each other we'll return -1, and to identify this condition we check that before and after the iteration, length of stack has not stayed the same. Thus, at the end when we're left with one item in the stack, we'll check for it to be a celeb by traversing it in a for-loop and comparing it with all the rest of the items except itself to see if knows(candidate, item) should be false and that knows(item, candidate) should be true, if not we return -1. At the end we return the candidate.
def findCelebrity(n, knows):
    stack = [i for i in range(n)]

    while len(stack) > 1:
        stackLen = len(stack)

        lastItem = stack.pop()
        secondLastItem = stack.pop()
        if not knows(lastItem, secondLastItem):
            stack.append(lastItem)
        if not knows(secondLastItem, lastItem):
            stack.append(secondLastItem)

        if len(stack) == stackLen:
            return -1

    if len(stack) == 0: return -1

    candidate = stack.pop()
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
# TC: O(3n)
# SC: O(n)


# Approach3: 2 pointer approach - we'll start by taking L as 0 and R as n-1 and see if L satisfies the celeb condition i.e. knows(L, R) is false, in which case R is decremented. Conversely, L is incremented. Thus, when L and R points to same item, we'll break the while loop and have thus found a candidate for being celeb. We'll separate check for candidate to be a celeb as done in Approach2. If this candidate doesn't work out it means there is no celeb or otherwise this item at first, should not have came true across knows(L,R) or the other way around it shouldn't have been true and there cant be 2 celebs, because everyone apart from a celeb should know the celeb. So in case condition doesn't work we don't bother to wonder about possibility of a different item to be candidate be return -1 directly. Whereas if condition works, the candidate is returned.
def findCelebrity(n, knows):
    L, R = 0, n - 1
    while L != R:
        if not knows(L, R):
            R -= 1
        else:
            L += 1

    candidate = L
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
# TC:O(2n)
# SC:O(1)