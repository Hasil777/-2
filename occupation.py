from person import Person

class programmer(Person):
    def __init__(self,id,name,age,add,emails):
        super ().__init__( id ,name,age,add)
        self.emails=emails

sharyar=programmer(1,'Sharyar',13,'programmer','sharyar@mail.com').isBorn()
print(f'My occupation is {sharyar}')

Atabek=programmer(2,'Atabek',24,'Doctor','atabek@mail.com').isBorn()
print(f'My first is {Atabek}')





    