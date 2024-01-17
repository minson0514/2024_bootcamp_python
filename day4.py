#sequence data structure
#immutable -> tuple
#mutable -> index

#list can contain any type of data

#create from a string with split
#use split() to chop a string into a list
#get item by indexing [num]
#gty items by slicing [:]
#to reverse a list in place, use list.reverse()
'''
subjects = ["C++", "Java", "Python"]
print(subjects[::-1])
print(subjects) #원본이 바뀌지는 않음
#subjects = subjects[::-1] #assign variable to change origin
subjects.reverse() #use reverse
print(subjects) #원본을 바꿈
'''
#Add an item to the end with append() -> just add an item at the end of the list
#Add an item by offset with insert() -> 잘 안 쓰임
#combine list by using extend() or '+'
#change Items with a slice
#delete an Item by offset with del
#delete an Item by vlaue with remove()
#get an Item by offset and delete it with pop()
#delete all items with clear
#find an Item's offset by value with index()
'''
subjects = ["C++", "Java", "Python"]
subjects = subjects[::-1]
print(subjects)
#by offset
#del subjects[-2] #역방향 지우기
#del subjects[2]
#subjects.pop(2)

#by value
#subjects.remove("Java") #동일 값이 있는 경우 가장 앞쪽 것을 지움
print(subjects)
'''

#test for a value with in (check for existense)-> return type: bool
#convert a list to a srting with join

#reorder item by sort
subjects = ["C++", "Java","리눅스","5", "Python", "Java", "9","데이터베이스"]
subjects = subjects[::-1]
print(subjects)
subjects.sort() #정방향 정렬
#한글, 숫자, 영어 순으로 우선순위
subjects.sort(reverse=False) #역방향 정령
#리스트 안에 숫자형 있으면 TypeError: '<' not supported between instances of 'str' and 'int'
copy_subjects = sorted((subjects))
print(subjects)