'''
numbers = ["7", "-11", "3"]
total=0
for number in numbers:
    total=total+int(number)
print(total) #-1
'''

#using map function
'''
numbers = ["7", "-11", "3"]
#print(map(int, numbers)) #<map object at 0x000001C244139750>
print(sum(map(int, numbers))) #-1
'''

