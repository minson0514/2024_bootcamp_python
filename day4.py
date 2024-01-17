#sequence data structure
#immutable -> tuple
#mutable -> index

t1 = (5) #int
print("type of t2: ", type(t1))

#tuple has atleast one comma
#except empty tuple e.g. t7=()
#packing example
t2=5,
print("type of t2: ", type(t2))
t3 = (5,)
print("type of t3: ", type(t3))
t4 = (5,7)
print("type of t4: ", type(t4), "print tuple data structure: ", t4)
t5 = 5,7
print("type of t5: ", type(t5))
t6="python", "kim"
print("type of t6: ", type(t6), "extract component by []: ", t6[1])
t7 = ()
print("type of t7: ", type(t7))
t8=tuple()
print("type of t8: ", type(t8))

#unpacking example
subject, professor = t6
print("unpacking component subject:", subject)
print("unpacking component professor:", professor)

#unpacking error example
#ValueError: not enough values to unpack (expected 3, got 2)
'''
a, b, c = t6
print("unpacking component subject:", subject)
print("unpacking component professor:", professor)
'''

#create with tuple()
#combine tuples by Using +
#Duplicate Items with * -> similar with 'str * int'

#comparison
t9 = 1, 2, 3
t10 = 1, 2, 3, 1
print(t9 == t10) #false
print(t9 <= t10) #true
print(t9 > t10) #false

#modify tuple(combine)
t11 = 4.43,
print("id of t11:", id(t11))
t12 = 3.97, 4.1, 3.27
print(t11 + t12) #combined temporary
print(t11)
print("id of t11:", id(t11))
t11 = t11 + t12 #t11+=t12
print(t11) #modified
print("id of modified t11:",id(t11))


