
''''
Tuple:
    -immutable:means we can not modify it
    -stores diff type of elements
    -allows duplicates
    -allows slicing i.e (start:stop:skip):divides list into parts
    -allows indexing:
                -forward:starts with 0 and ends with n-1
                -negative:starts with -1 and ends with -n
    - No methods            
'''

m = ()
print(type(m))

m=(2,5,9.9,True,2+4j,"raju")
print(m)

m=(2,5,900.9,6,2,100)
print(m.index(2))
print(m.count(2))

p = (1,3,5.5,6.88,1,3,"Raj",True)
print(p)
print(p[6])
print(p[-4])
print(p[0:6:2])   #here 6th index cant print bcoz we stop there.

'''
Built-in opertions:we can use for any type of datatypes
           so we can also use for Tuple.They are
'''
m=(2,5,900.9,6,2,100)
print(m.index(2))
print(m)
print(len(m))
print(max(m))
print(min(m))
print(sum(m))

'''
Tuple operations:
     -concatanetion
     -iteration
     -repeatation : repeats the tuple,given no of times
     -membership operatns:checks values is member of tuple or not
                                i.e 1)in     2)not in
     -identity operatns:checks whether tuples are identical or not
                           i.e 1)is      2)is not
'''

t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2) #concatanetion
for i in t1:
    print(i)   #iteration

print(t2 * 3)  #repeat: it repeats t2 values 3 times and print them

print(3 in t1)  #membership: checks 3 is in t1 or not and 
print(3 in t2)             #   print true or false
print(4 not in t1)   #o/p is true

t1 = (1,2,3)
t2 = (1,2,3)   #Identity operatn:checks whether tuples are identical
t3 = (3,2,1)
print( t1 is t2)   #o/p: true
print(t2 is t3)     #false
print(t3 is not t1)   #true

