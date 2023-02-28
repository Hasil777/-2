class Person:
    def __init__(self,id,name,age,add):
        self.id=id
        self.name=name
        self.age=age
        self.add=add

    def isBorn (self):
        persons=dict()
        persons['id']=self.id
        persons['name']=self.name
        persons['age']=self.age
        persons['add']=self.add

        return persons