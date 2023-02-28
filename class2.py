'''class TwoNumbers:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def findMaxorMin(self):
        if self.num1>self.num2:
            return f'Less number is {self.num2}'
        else:
            return f'less number{self.num1}'
    def findANumber3(self):
        if self.num1%3==0:
            return f'{self.num1}'
        if self.num2%3==0:
            return f'{self.num2}'
        else:
            return f'No find'
        
if __name__=='__main__':
    a=int(input('a:'))
    b=int(input('b:'))
    maxOrmin=TwoNumbers(a,b).findMaxorMin()
    print(maxOrmin)
    divide3=TwoNumbers(a,b)
    print(divide3.findANumber3())'''


'''class Square:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Perimitor(self):
        P=2*(self.a+self.b)
        return P
    def SQ(self):
        S=self.a*self.b
        return S
    
if __name__=='__main__':
    c=int(input('a:'))
    d=int(input('b:'))
    a = Square(c,d).SQ()
    b=Square(c,d).Perimitor()
    print(a,b)'''

'''class Person(object):
    def __init__(self,fulname,age):
        self.fulname=fulname
        self.age=age
    def move(self):
        return f'{self.fulname}идет в \
школу и Ему {self.age}'
    def talk(self):
        return f'Данный момент {self.fulname} говорит с Ботом'
    
if __name__=='__main__':
    sharofiddin=Person('Sharofiddin',15)
    print(sharofiddin.move())
    print(sharofiddin.talk())'''

class Pet(object):
    def __init__(self,name,age,colour,isCut,breed,eat,isPlay,trained):
        self.name=name
        self.age=age
        self.colour=colour
        self.isCut=isCut
        self.breed=breed
        self.eat=eat
        self.isPlay=isPlay
        self.trained=trained

    def name_(self):
        return f'Кличка моего питомца {self.name},ему {self.age}, \
он {self.colour} цвета, он {self.isCut},его порода {self.breed},он ест {self.eat},он играет в {self.isPlay}\
 и он {self.trained} '
    def age_(self):
        if self.age>6:
            return f'он взрослый'
        

   
        
if __name__=='__main__':
    dog=Pet ('Graff',4,'чёрного','не обрезанный','овчарка','рис','догонялки','не дресерованный')
    print(dog.name_())
    print(dog.age_())

'''
from sys import stdin
from copy import deepcopy

class Matrix(object):
    def __init__(self,matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):'''

    
   



