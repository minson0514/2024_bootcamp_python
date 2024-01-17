'''
squares = list()
for i in range(1, 5+1, 1):
    squares.append(i**2)
print(squares)
'''

#create a list with a comprehension

#['expression' for 'item' in 'iterable']
# -> iterable 자료에 순환 가능한 자료형이 나와야함
# -> 자동으로 append기능이 있음
'''
sqares = [i*i for i in range(1, 5+1, 1)]
print((sqares))
'''

#['expression' for 'item' in 'iterable' if 'condition']
'''
even_sqares = [i*i for i in range(1, 5+1, 1) if i % 2 == 0] #짝수의 제곱만 출력 됨
print(even_sqares)
'''

#tuple versus lists
#튜플은 적은 공간 사용
#you can't clobber tuple items by mistake
#튜플을 딕셔너리의 key로 사용할 수 있음 b/c immutable
