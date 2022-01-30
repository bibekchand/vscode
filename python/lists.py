
terobau = ['a', 'b', 'c', 'd' ] 
terobau.sort()
#slicing
print(terobau[::-1])
print(len(terobau))
print(max(terobau))
print(min(terobau))
terobau[1]= 'hello'
print(terobau)
terobau.append('b') #add the element to the list
terobau.pop()# removes the element 'last one from the list'
tp = (1, 2 ,3)
# it is a tuple which cannot have a value appended
print(tp)
# tp(1) = 3 this is invalid
a=1
b=2
# temp = a
# a = b 
# b = temp
# print(a,b) 
(a,b)=(b,a)
print(a,b)

