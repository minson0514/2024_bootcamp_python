'''
def desc(f): #outer fuction
    def wrapper(): #inner function 독립된 공간, 호출해야 사용 가능
        #closure가 f라는 값을 가지고 있음
        print("study")
        f()
    #print("a")
    return wrapper

#decorating
@desc
def something():
    print("do something~")
# s=desc(something)
# s() #이렇게 두 줄 써도 되고 밑에처럼 써도 됨
something()
'''