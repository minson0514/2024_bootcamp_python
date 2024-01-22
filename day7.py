class FlyingBehavior:
    def fly(self): #메서드 형태 #fly라는 instance
        return f"하늘을 훨훨 날아갑니다~"

class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓 추진기로 하늘을 날아갑니다."

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 하늘을 훨훨 날아갑니다."

class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly_behavior):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly_behavior #클래스의 객체

    def set_fly_behavior(self, fly):
        self.fly_behavior = fly


    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self,target):
        #return self.__name+"+"+target.__name #연산자 오버로딩
        return f"두 포켓몬스터 체력의 합은 {self.hp+target.hp} 입니다."


class Charizard(Pokemon):
    pass

class Pikachu(Pokemon):
    def __init__(self, name, hp, fly):
        self.name = name
        self.hp = hp
        #self.fly_behavior = fly #aggregation
        self.fly_behavior = NoFly() #composition

#nofly=NoFly()
p1 = Pikachu("피카츄", 35, NoFly) #lsp
print(p1.fly_behavior.fly())
'''
wings = FlyWithWings()
c1 = Charizard("리자몽", 120, wings) #다른 클래스의 객체를 인수로 전달 #lsp
print(c1.fly_behavior.fly()) #리자몽객체 -> flyingbehavior클래스의 객체 -> " 가 가지고 있는 속성
print(p1.fly_behavior.fly())
print(p1) #cannot fly
print(c1)
p1.set_fly_behavior(JetPack())
print(p1+c1)
'''