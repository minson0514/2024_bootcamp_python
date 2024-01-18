
"""
def squares(*n) -> list:
    '''
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    return [pow(i,2) for i in n]#list comprehension
    #return n*n

def run_function(f, *number) -> list:
    return f(*number)

print(squares(7,5,2))
print(run_function(squares, 9,10))
"""

"""
def out_func(nout):
    def inner_func(nin):
        return nin * nin
    return inner_func(nout)
print(out_func(5))
"""

"""
def out_func(nout): #1) 호출 nout받음
    def inner_func(): #4) 9받음
        return nout * nout #5) 리턴
    return inner_func #2) inner_func 을 리턴
x=out_func(9) #3) inner_func 주소 받을 때 nout에 9(외부함수의 매개변수)인 것도 알고 있음

print(type(x)) #<class 'function'>
print(x) #<function out_func.<locals>.inner_func at 0x00000299014C2AC0>
print(x()) #closure 호출 방식 #5번 과정까지 실행한 결과를 리턴함
"""ㅗ