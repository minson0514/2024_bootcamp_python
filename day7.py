# module
#from mymathi import* #from 절은 모듈 이름 생략 가능
#모듈 이름을 아예 생략하고 쓰면 됨
import mymathi as mm #모듈 이름을 다른식으로 import 인공지능 분야에서 많이 사용함
#cf. importh numpy as np  이런 식으로 사용 함


while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {mm.fahrenheit_to_celsius(fahrenheit):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {mm.celsius_to_fahrenheit(celsius):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        if mm.isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if mm.isprime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Menu!')