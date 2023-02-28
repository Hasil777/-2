'''class Main:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def getSum(self):
        return self.a+self.b
    
class Home(Main):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

    def getSum(self):
        a= super().getSum()+self.c
        return a

main=Main(5,4)
print(main.getSum())

home=Home(5,4,3)
print(home.getSum())'''
'''
class Person:
    def __init__(self):
        self._age=0

    def get_age(self):
        return f'Getter {self._age}'
    
    def set_age(self,a):
        self._age=a
        return f'Setter {self._age}'
    
    def del_age(self):
        del self._age
        return f'Deleter method is called'
    
    age =property(get_age,set_age,del_age)

sharyar=Person()
sharyar.age=13
print(sharyar.age)
print(sharyar.set_age(15))
print(sharyar.del_age())'''

class Person:
    def __init__(self):
        self._age=0

    @property
    def age(self):
        print('getter method is called')
        return self._age
    @age.setter
    def age(self,a):
        if a < 18 :
            raise ValueError('sorry we cannot accept you as adult')
    
    @age.getter
    def aged(self):
        print('Another method is called')
        return self._age
    
    @age.deleter
    def ageD(self):
        del self._age
        print('Deleter method is called')

Talgat= Person()
age=int(input('a :'))
Talgat.age=age
print(Talgat.aged)
print(Talgat.ageD)