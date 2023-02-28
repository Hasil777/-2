class Engine:
    def __init__(self,model,power,fuel):
        self.model=model
        self.power=power
        self.fuel=fuel
    
    def windUp(self):
        return f'{self.model}-{self.power}-{self.fuel}'

engine_1=Engine('2.2','150 л.с','petrol')

class Ford(Engine):
    def __init__(self,name,color,wheels,passengers):
        super().__init__(self, power='15.23',fuel='Petrol')
        self.name=name
        self.color=color
        self.wheels=wheels
        self.passengers=passengers

    def drive(self):
        return f'{self.name}-{self.color}-{self.wheels}-{self.passengers}'
car_1=Ford('Mustang','black',5,4)
