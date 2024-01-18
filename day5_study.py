#함수 정의 및 사용
'''
1. 인자 X 반환값 X: 함수 내의 수행문만 수행
2. 인자 X 반환값 O: 수행문 수행 후 결과값 반환
3. 인자 O 반환값 X: 인자를 사용해서 수행문만 수행
4. 인자 O 반환값 X: 인자를 사용해서 수행문 수행 후 결과값 반환
'''

'''
#1
def say():
    print("Hi") #함수 내의 수행문
say()

#2
def say():
    return "Hi" #반환값
a=say()
print(a) #print(say())

#3
def add(a,b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")
add(3,4)

#4
def add(a,b):
    return f"{a}, {b}의 합은 {a+b}입니다."
c = add(3,4)
print(c)
'''