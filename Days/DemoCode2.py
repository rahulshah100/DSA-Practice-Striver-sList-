tasks=[[1,3,2],[2,5,3],[5,6,2]]

def func(tasks):
    globalMax=0
    globalMin=999999999
    for i in tasks:
        i.pop()
        if globalMax<max(i):
            globalMax=max(i)
        if globalMin>min(i):
            globalMin=min(i)
    print(globalMax-globalMin)

func(tasks)