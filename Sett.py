
'''
Set:
   - k = {1,2,2.'raj',8,....}
   - do not allow duplicates
   - no index, no slicing, adds values in un-order manner
   -do not allow mutable data types as set elements
'''

s = {1,234,9.8,'raj'}
print(type(s))

'''
Methods:
- add
- update
- pop
- remove
'''

s = {2,35,7,2,5,7,55,63,7} # in set,duplicate values are not allowed
print(s)                   # so it remove duplicates and shows o/p.
     # also displays o/p not in order as given.
s.add(69)  # it used to add single data 
print(s)
s.update({4,7,55,35,674,66})   # used to add bulk of data
print(s)
s.pop()    # deletes one data randomly
print(s)
s.remove(66)  # deletes particular value given
print(s)

'''
Operations:
      - union
      - intersection
      - difference
      - issubset
      - issuperset
'''
s1 = {2,3,4}
s2 = {4,5,6}
# Union:It combines 2 sets by removing duplicates
print(s1.union(s2))

# Intersection: It prints common values from 2 sets
print(s1.intersection(s2))

'''
# difference:It removes common values and print 
                      only one set'''
print(s1.difference(s2))  
#it removes common value from s1 and prints s1.
print(s2.difference(s1))
#it removes common value from s2 and prints s2.

#issuperset: 
s1 = {1,2,3,4,5}
s2 = {1,2,3}  #here s2 contains elements from s1
              # so s1 issuperset of s2
print(s1.issuperset(s2))

#issubset: 
s1 = {1,2,3,4,5}
s2 = {1,2,3}  #here s2 contains elements from s1
              # so s2 issubset of s1
print(s2.issubset(s1))

# for loop for set
p = {3,4,7.7,9,54,678,'Raj'}
for i in p:   # here also it reads values randomly
    print(i)



