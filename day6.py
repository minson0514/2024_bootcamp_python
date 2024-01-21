class FlyingMixin:
    def fly(self):
        return f"{slef.name}이(가) 훨훨 납니다."
class SwmminMixin:
    def fly(self):
        return f"{slef.name}이(가) 수영을 합니다."

class Pokemon:
    def attack(self):
        print("공격")

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

class Pokemon:
