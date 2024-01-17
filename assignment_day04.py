number = int(input("input num: "))
is_prime = True #int type-> boolean
if number <= 1: #1이 소수가 아니니까 해당 코드 추가
    print("%d is NOT prime nuber" % number)
else:
    for i in range(2,number): #이부분 수정함
        if number % i == 0:
            is_prime = False #remove +
            break #약수가 한번이라도 발생하면 루프 탈출
            #number=111 일 때 3번까지 돌고 break
        i += 1
    if is_prime: #remove ==
        print("%d is prime number"%number)
    else:
        print("%d is NOT prime nuber" %number)