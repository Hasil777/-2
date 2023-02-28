'''class tomato:
    statas={0:'nothing',1:'flower',2:'green_tomato',3:'red_tomato'}
    def __init__(self,_index,_state):
        self._index=_index
        self._state=0

    def grow(self):
        self._state+=1
    def is_ripe(self):
        if self._state==3:
            return 'Помидор созрел'
        return 'Помидор ещё неспелый'

class Tomayobush(tomato):
    def __init__(self, _index, _state):
        super().__init__(_index, _state)'''

#ОПИРОВАТЬ
'''class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.empCount)  
  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

# Это создаст первый объект класса Employee  
emp1 = Employee("Андрей", 2000)  
# Это создаст второй объект класса Employee  
emp2 = Employee("Мария", 5000)  
emp1.display_employee()  
emp2.display_employee()  
print("Всего сотрудников: %d" % Employee.emp_count)'''

