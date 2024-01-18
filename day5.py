#prime number
#new*
def isprime(n) -> bool: #return type is boolean type(t/f)
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return  True
#help(isprime) #우리가 작성한 함수에 대한 설명이 나옴
#help(len)
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1
for number in range(n1, n2+1):
    if isprime(number): #함수 호출
        print(number, end=' ')