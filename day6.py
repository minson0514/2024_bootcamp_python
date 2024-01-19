# Open Closed Principle
def test(f):
    """
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    #def test_in(*args, **kwargs):
    def test_in():
        print('start')
        #result = f(*args, **kwargs)
        f()
        print('end')
        #return result
    return test_in
def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

@test
def greeting():
    print("안녕하세요~")


greeting()
number = int(input("number : "))
print(factorial_repetition(number))
print(factorial_recursion(number))
print(globals())