'''
class Pokemon():#소괄호 쓰지 않아도 됨
    pass

pikachu = Pokemon()
squirtle = Pokemon()
'''
'''
class Pokemon:#소괄호 쓰지 않아도 됨
    def __init__(self, name): #생성자
        print(f"{name} 포켓몬스터 생성")

pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
print(pikachu) #<__main__.Pokemon object at 0x0000023585754F10>
print(squirtle) #<__main__.Pokemon object at 0x0000023585754F90>
'''
'''
class Pokemon:
    pass
pikachu = Pokemon()
squirtle = Pokemon()
pikachu.name = "피카츄"
pikachu.nemesis = squirtle
print(pikachu.name) #피카츄
#print(pikachu.nemesis.name)
squirtle.name="꼬부기" #객체에 이름속성을 부여 한 후에

print(pikachu.nemesis.name) #프린트해야 에러 없이 할당된 것이 나옴
#아래처럼 해도 됨
#pikachu.nemesis.name = "꼬부기"
#print(squirtle.name)
'''

#클래스 안에 선언된 멤버함수를 메소드라고 함

class Pokemon:#소괄호 쓰지 않아도 됨
    def __init__(self, name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name} 이(가) {target.name}을(를) 공격!")

charizard = Pokemon("리자몽")#리자몽 포켓몬스터 생성
pikachu = Pokemon("피카츄")#피카츄 포켓몬스터 생성
squirtle = Pokemon("꼬부기")#꼬부기 포켓몬스터 생성

charizard.attack(squirtle) #리자몽 이(가) 꼬부기을(를) 공격!
#print(pikachu.name) #AttributeError: 'Pokemon' object has no attribute 'name'
#print(squirtle.name) #포켓몬에 네임이라는 속성을 가지고 있지 않다