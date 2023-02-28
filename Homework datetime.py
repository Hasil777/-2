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