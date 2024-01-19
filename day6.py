class FlyingMixin
    def fly(self):
        return f"{slef.name}이(가) 훨훨 납니다."
class SwmminMixin
    def fly(self):
        return f"{slef.name}이(가) 수영을 합니다."
class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

#class Pikachu(Pokemon):
class Pikachu(Pokemon): #is - a
    def __init__(self, name, type):
        super().__init__(name) #super() -> 부모클래스 호출, 부모클래스의 init method를 이용해서 초기화
        self.type = type
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")
    def electric_info(self):
        print("전기 계열의 공격을 합니다.")

class Squirtle(Pokemon): #is - a
    pass
class Agumon:
    pass

p1 = Pikachu("피카츄", "전기")
p2 = Squirtle("꼬부기")
p3 = Pokemon("근육몬")
p1.electric_info()
#p3.electric_info() #AttributeError: 'Pokemon' object has no attribute 'electric_info'
p1.attack(p2)
p2.attack(p1)
print(p1.name, p1.type)
print(issubclass(Pikachu,Pokemon))
#오버라이드: 부모가 가진 메서드를 자식이 재정의함