from Sum1 import summa

class third(summa):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d



summa_2=third(2,7,5,6).sum_3()
print(summa_2)   

