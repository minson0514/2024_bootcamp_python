#원소 중에 immutable한 값을 바꾸면 복제 공간에 있는 값을 건드리지 않아서 값이 변경되지 않음
'''
subjects = ["a","b","c"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects, a,b,c,d)
subjects[1]="x"
print(subjects,a,b,c,d)
'''
#문자열 literal을 list(mutable)로 바꾸니까 copy한 값이 변경되게 됨
'''
subjects = ["a",["b","c"],"d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects, a,b,c,d)
subjects[1][1]="x"
print(subjects,a,b,c,d)
'''

#깊은 복사, 얕은 복사, 참조
#->변수는 바뀌지만 복제본이 바뀌는 것을 원하지 않으면 deepcopy를 하면 됨
'''
import copy
subjects = ["a",["b","c"],"d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a) #deep copy한 부분만 바뀌지 않음
#a를 복사해서 그대로 copy하기 때문에...
print(subjects, a,b,c,d,e)
subjects[1][1]="x"
print(subjects,a,b,c,d,e)
'''

#pythontutor.com 에서 구현한 코드를 가시적으로 확인할 수 있음

#iterate with for and in -> return True and False
#iterate multiple sequences with zip()
#->여러 개의 리스트가 있는데 원소의 길이가 서로 다를 때 가장 작은 리스트의 길이만큼만 run

#create a list with a comprehension

#['expression' for 'item' in 'iterable']
# -> iterable 자료에 순환 가능한 자료형이 나와야함
# -> 자동으로 append기능이 있음


