#6장 반복문 연습문제
#6.1
'''
list_0117=[3,2,1,0]
for i in range(0,4):
    print(list_0117[i])
'''

#6.2
'''
guess_me = 7
number = 1
while True:
    if number<guess_me:
        print("too low")
    elif number==guess_me:
        print("found it")
    else:
        print("oops")
        break
    number+=1 #number==8 일 때까지 반복하고 종료
'''

#6.3
'''
guess_me = 5
for number in range(10): #range: default parameter(0:":1)
    if number<guess_me:
        print("too low")
    elif number==guess_me:
        print("found it")
        break #break this loop when number==5
        #this loop circulate 6 times b/c range's start default parameter is 0
    else:
        print("oops")
        break
'''