'''class Car():
    def __init__(self,model,passengers,isWork):
        self.model=model
        self.passengers=passengers
        self.iswork=isWork

    def drive(self):
        actions =  []
        actions.extend([self.model,self.passengers,self.iswork])
        return actions
    
    @staticmethod
    def say():
        return f'Hi'
if __name__=='__main__':
    car_1 = Car('bmw',4,True)
    print(car_1.drive())
    print(car_1.say())'''

'''class e_commerce:
    material='Mobile phone'

    def purchase(obj):
        return f' P. m. is: {obj.material} '
    
e_commerce.purchase=classmethod(e_commerce.purchase)
print(e_commerce.purchase())'''

'''from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def fromB(cls,name,year):
       return cls(name,date.today().year-year)
    
    @staticmethod
    def isAdult(age):
        if age >18:
            return True
        else:
            return False
    def desplay(self):
        return f'Name {self.name},{self.year}'
person_1=Person('Talgat',14)
person_2=Person.fromB('Talgat',2008)
print(person_1.age)
talgat=person_2.age
print(talgat)
print(f'The person {talgat} is adult {Person.isAdult(talgat)}')'''

from datetime import date
class Company:
    def __init__(self,name,year,product):
        self.name=name
        self.year=year
        self.product=product

    @classmethod
    def data_(cls,name,year,product):
        return cls(name,year,product)
    
    @classmethod
    def year_(cls,name,year,product):
        return cls(name,year,product)
    
    @staticmethod
    def ischeck(year):
        if date.today().year - year >=3:
            return 'просроченный'
company=Company('Lays',2019,'chips')
company_2=Company.data_('Lays','12,02,2019','chips')
print(f'дата выпуска {company_2.year}')
company_3=Company.year_('Lays',2019,'chips')
print(f'год выпуска {company_3.year}')
print(company.ischeck(2019))
