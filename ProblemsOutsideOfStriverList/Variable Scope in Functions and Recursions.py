from typing import List

ANum = [12,23]

class Solution:
    def AnyRandomFunc(self, nums: List[int]) -> int:
        def recursiveFunction():
            if nums[0] < 30:
                nums[0] = nums[0]+1
                print(nums[0])
                recursiveFunction()
            else:
                return 0
        print("initially nums[0]",nums[0])
        recursiveFunction()
        print("After recursions nums[0]", nums[0])

def AnyRandomFunc2():
    ANum[0]=ANum[0]+1

def AnyRandomFunc3(ANumIsSent):
    ANumIsSent[0] = ANumIsSent[0] + 1

def AnyRandomFunc4(AANum):
    AANum=[112,12] #Reassignment makes this a new local Variable of AnyRandomFunc4
    AANum[0]+=1

def AnyRandomFunc5(ANum):
    ANum=[112,12] #Reassignment makes this a new local Variable of AnyRandomFunc4
    ANum[0]+=1

# def AnyRandomFunc6(ANum): #O/p: SyntaxError: name 'ANum' is parameter and global
#     global ANum #Makes this the Global Variable
#     ANum = [112, 12]
#     ANum[0]+=1

def AnyRandomFunc6(A):
    global ANum #Makes this the Global Variable
    ANum = [112, 12]
    ANum[0]+=1

S=Solution()
S.AnyRandomFunc([23,12,34,1,232,63])

print('ANum Before AnyRandomFunc2',ANum)
AnyRandomFunc2()
print('ANum After AnyRandomFunc2',ANum)

print('ANum Before AnyRandomFunc3',ANum)
AnyRandomFunc3(ANum)
print('ANum After AnyRandomFunc3',ANum)

print('ANum Before AnyRandomFunc4',ANum)
AnyRandomFunc4(ANum)
print('ANum After AnyRandomFunc4',ANum)

print('ANum Before AnyRandomFunc5',ANum)
AnyRandomFunc5(ANum)
print('ANum After AnyRandomFunc5',ANum)

print('ANum Before AnyRandomFunc6',ANum)
AnyRandomFunc6(ANum)
print('ANum After AnyRandomFunc6',ANum)