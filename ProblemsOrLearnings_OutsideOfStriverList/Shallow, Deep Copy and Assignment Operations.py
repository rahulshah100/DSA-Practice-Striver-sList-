import copy

a=[1,[2,3]]
print("a",a)

b=copy.deepcopy(a)  #This creates a deepcopy of a variable in which no reference from the original is took, but totally new declarations are made for that object and it's entries.
c=copy.copy(a)  #Shallow copy, create a new object but all it's inner values i.e. entries are referred from original one i.e. points at same mem location. By changing immutables in original array such as int, stored at a[1], array a creates a new reference to where new a[0] gets stored but c i.e. shallow copy keeps pointing to old reference of a[0] and hence c persists the original value of a[0]. While with changing mutables i.e. a[1] it could be changed at same mem location where originally it had been saved, which is being referred by c and so it reflects in both arrays a and c.
d=a[:]       #Another way of creating a shallow copy.
e=a             #Assignment Operation. In case of immutables/basic data structures such as int, string, float along with one immutable yet derived data structure- tuple this will create deepcopy. But for mutable data structures such as array, set, dictionary this will creates a reference of original object.

a[0] = 31
a[1][0] = 5

print("abcde:",a,"\n",b,"\n",c,"\n",d,"\n",e)
# O/P: abcde: [31, [5, 3]]
#  [1, [2, 3]]
#  [1, [5, 3]]
#  [1, [5, 3]]
#  [31, [5, 3]]