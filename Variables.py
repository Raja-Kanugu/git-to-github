
'''
  Variables:
  -it is a container which stores a value or
  address of a value.
  syntax: variable = value
  Rules:
  -------
      -Dont start with digit or symbols 
      -starting letter should be alphabet or underscore
      -case sensitive
 '''

#Examples:
abc23 = 10
_xyz = 20
print(abc23+_xyz)
# To find memory location of variable,we use id()
print('memory location of abc23:',id(abc23))

# 12abc = 'rajkumar'    -should not start with number or symbol

'''    a,b,c = 1
    print(b)                  here we get error,bcoz
    print(a,b,c)            we can not assign sinle value to 
                        multiple variables at a time       '''

a,b,c=1,3,5
print(a,b,c) #we can assign multiple values to multiple vars at a time

c=1,6,9
print(c)    #we can assign multiple values to single variable

a=b=c=25    #we can assign single value to multiple vars using '='
print(a,b,c)
print(b)