#Problem #1
#if - else 문을 이용해 짝홀수 판별하기
"""
num = int(input("Enter the num: "))
def even_odd(num):
    '''
    인자 O, 반환값 X
    :param num:
    :return:
    '''
    if num%2==1:
        print("%d is an odd number"%num)
    else:
        print("%d is an even number"%num)
even_odd(num) #함수 호출
#인자 num을 사용해서 수행문(if else) 수행
"""

#Problem #2
#if - else 문을 이용해 2개의 숫자를 입력 받아 최대값을 구하고 출력
#단 최대값을 함수 안에서 출력하시오.
'''
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
def cal_max(a,b):
    if a > b:
        max = a
    else:
        max = b
    print(f"max num is {max}")
cal_max(num1,num2) #num1, num2를 인자로 받아서 실행문 실행
'''

#Problem #3
#if - else 문을 이용해 2개의 숫자를 입력 받아 최대값을 구하고 출력
#단 최대값을 함수 밖에서 출력하시오.
"""
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
def cal_max(a,b): #2) 함수 실행
    '''
    
    :param a: 
    :param b: 
    :return: return max
    '''
    if a > b:
        max = a
    else:
        max = b
    return max #3) max값 리턴
a=cal_max(num1,num2) #1) num1, num2를 a,b로 넘김
#4) 리턴 값을 a에 저장
print(f"{a} is the max value") #5) print
"""

#Problem #5
#for 문을 이용하여 원하는 단을 입력받아 그 단의 구구단을 출력
#함수명 gugudan으로 작성하시오
'''
dan = int(input("원하는 단을 입력하세요: "))
def gugudan(a):
    for i in range(1,10): #함수 내 구문 실행
        print(f"{a} * {i} = {a*i}")
gugudan(dan) #단을 입력받아서
'''

#Problem #6
#특정값부터 특정값까지의 합을 구해서 출력하는 프로그램을 함수를 이용해 작성하시오
#함수 이름 any_sum
#단 합의 구간에 해당하는 값은 사용자가 셸에서 입력하도록 하고, 이후에 함수를 호출하고 합은 함수 밖에서 출력하시오.
'''
start = int(input("시작값 입력: "))
end = int(input("끝값 입력: "))
def any_sum(start,end):
    total = 0
    for i in range(start, end+1):
        total = total + i
    return total
hap=any_sum(start, end)
print(f"합은 {hap}")
'''

#Problem #7
#사용자로부터 Shell에 정수값을 하나 입력받아 그 수가 2의 배수면서 3의 배수면 Yes를, 아니면 No를 출력하는 프로그램을
# 조건문과 함수를 이용해 작성하되, 함수 호출까지 코드에 포함시킨다.
#7-1
#함수 이름을 multiple1로 하여 Yes, No를 함수 안에서 출력하며 전달인자는 없게 작성
'''
def multiple1():
    num = int(input("enter a num: "))
    if (num % 2 == 0 and num % 3 == 0):
        print("Yes")
    else:
        print("No")
multiple1()
'''

#7-2
#함수 이름을 multiple2로 하여 Yes, No를 함수 안에서 출력하며 전달인자가 있게 작성
'''
num = int(input("enter a num: "))
def multiple2(num):
    if (num % 2 == 0 and num % 3 == 0):
        print("Yes")
    else:
        print("No")
multiple2(num)
'''

