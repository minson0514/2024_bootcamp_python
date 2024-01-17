#0116 과제
'''
while True:
    menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Prime1 4) Prime2 5) Quit Program : ")

    if menu =='1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0)*5.0 / 9.0): .4f}C')
    elif menu == '2':
        celsius = float(input('Input celsius : '))
        print(f'Celsius : {celsius}F, Celsius : {((celsius * 9.0 / 5.0) + 32.0): .4f}C')
    #중복코드 수정 필요 by 함수
    elif menu =='3':
        number = int(input("input num: "))
        is_prime = True  # int type-> boolean
        if number <= 1:  # 1이 소수가 아니니까 해당 코드 추가
            print("%d is NOT prime nuber" % number)
        else:
            for i in range(2, number):  # 이부분 수정함
                if number % i == 0:
                    is_prime = False  # remove +
                    break  # 약수가 한번이라도 발생하면 루프 탈출
                    # number=111 일 때 3번까지 돌고 break
                i += 1
            if is_prime:  # remove ==
                print("%d is prime number" % number)
            else:
                print("%d is NOT prime nuber" % number)
        pass
    elif menu == '4': #이전 버전 대비 띄어쓰기 안 했을 때 생기는 오류 수정 해야함
        numbers = input("input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:  # non temporary variable
            n1, n2 = n2, n1  # unpacking
        for number in range(n1, n2 + 1):  # from n1 ~ to n2+1
            is_prime = True  # reset
            if number <= 1:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break  # escape ^for^
                if is_prime: print(number, end=' ')
        print() #줄바꿈
        pass
    elif menu == '5':
        print("Terminate program")
        break
'''
#0117과제
#205p 8.10까지
#예습도 좀 하세요 !!
