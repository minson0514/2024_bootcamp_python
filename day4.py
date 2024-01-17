numbers = input("input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:  # non temporary variable
    n1, n2 = n2, n1  # unpacking
    for number in range(n1, n2 + 1):  # from n1 ~ to n2+1
        is_prime = True  # reset
        if number < 2:
            pass
        else:
            i = 2
            while i*i < number: #performance issue
                if number % i == 0:
                    is_prime = False
                    break
                i = i + 1
                #print(i,end =' ') #확인용 구문
            if is_prime:
                pass
                print(number, end=' ')