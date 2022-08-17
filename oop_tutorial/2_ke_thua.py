#các lớp con có thể hi đè , mở rộng các thuộc tính, các phương thức của lớp cha
# đạt lớp cha trong ngoặc ssown trong phần định nghĩa

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self,sound):
        return f'{self.name} says {sound}'

class JackRussellTerrier(Dog):
    def speak(self,sound='hmhm'):
        return super().speak(sound)  # tự động gọi đến phương thức speak ở lớp cha
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass

if __name__=="__main__":
    a=JackRussellTerrier('meme',3)
    b=Dachshund('mimi',2)
    c=Bulldog('meomeo',5)

    print(a)
    print(b.name)
    print(c.age)
    print(c.speak('gâu gâu'))
    print(a.speak())