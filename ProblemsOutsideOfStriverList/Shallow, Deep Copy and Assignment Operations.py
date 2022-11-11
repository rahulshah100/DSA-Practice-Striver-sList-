import copy

a=[1,[2,3]]
print("a",a)

b=copy.deepcopy(a)  #This creates a deepcopy of a variable in which no reference from the original is took, but totally new declarations are made for that object and it's entry.
c=copy.copy(a)  #Shallow copy, create a new object but it's inner value i.e.entries, get referred from original one.
d=a[:]       #Another way of creating a shallow copy.
e=a             #Assignment, creates a reference of original object, it creates just a different variable name to access the original variable.

a[0] = 31
a[1][0] = 5

print("abcde:",a,"\n",b,"\n",c,"\n",d,"\n",e)