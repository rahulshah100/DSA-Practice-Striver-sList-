from typing import List

ANum = [12, 23]     #--1
class Solution:
    def AnyRandomFunc(self, nums: List[int]) -> int:
        def recursiveFunction():
            if nums[0] < 30:
                nums[0] = nums[0] + 1
                print(nums[0])
                recursiveFunction()
            else:
                return 0

        print("initially nums[0]", nums[0])
        recursiveFunction()
        print("After recursions nums[0]", nums[0])

def AnyRandomFunc2():
    ANum[0] = ANum[0] + 1

def AnyRandomFunc3(ANumIsSent): #If mutable datatypes i.e.lists,dicts, and set are passed into a function, then altering them from within the function will alter their original variables too. That is because they're always passed by reference and not by value. That is the reference of mem address where the original one is stored is passed as opposed to passing the value of variable. We can use is operator to verify this. As seen below: 'is' shows True. So unlike == which compares value, 'is' operator compares id(var1)==id(var2) i.e. mem locatn.
    print('ANumIsSent is ANum-',ANumIsSent is ANum)
    ANumIsSent[0] = ANumIsSent[0] + 1

def AnyRandomFunc4(AANum):
    print('AANum is ANum-',AANum is ANum)
    AANum = [112, 12]  # Reassignment changes this function's local copy of AANum from pointing/referring to the mem address of passed ANum
    print('AANum is ANum-',AANum is ANum)
    AANum[0] += 1

def AnyRandomFunc5(ANum):
    ANum = [112, 12]  # Reassignment changes this function's local copy of ANum from pointing/referring to the mem address of passed ANum
    ANum[0] += 1

# def AnyRandomFunc6(ANum): #O/p: SyntaxError: name 'ANum' is parameter and global
#     global ANum #Makes this the Global Variable
#     ANum = [112, 12]
#     ANum[0]+=1

def AnyRandomFunc6(A):
    global ANum  # Makes this the Global Variable defined outside at #--1
    ANum = [112, 12]
    ANum[0] += 1


S = Solution()
S.AnyRandomFunc([23, 12, 34, 1, 232, 63])
print()

print('ANum Before AnyRandomFunc2', ANum)
AnyRandomFunc2()
print('ANum After AnyRandomFunc2', ANum)
print()

print('ANum Before AnyRandomFunc3', ANum)
AnyRandomFunc3(ANum)
print('ANum After AnyRandomFunc3', ANum,end="\n")
print()

print('ANum Before AnyRandomFunc4', ANum)
AnyRandomFunc4(ANum)
print('ANum After AnyRandomFunc4', ANum,end="\n")
print()

print('ANum Before AnyRandomFunc5', ANum)
AnyRandomFunc5(ANum)
print('ANum After AnyRandomFunc5', ANum,end="\n")
print()

print('ANum Before AnyRandomFunc6', ANum)
AnyRandomFunc6(ANum)
print('ANum After AnyRandomFunc6', ANum,end="\n")

# TakAway: While passing derived DataStructure (especially in recusrsion) pass a copy and not the original list. In merge sort code we can see arr[:mid] and arr[mid:] passes not arr but a seperately created array including specified entries.