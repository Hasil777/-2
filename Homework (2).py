import string
class Alphabet(object):
    def __init__(self,russian,english):
        self.russian=russian
        self.english=list(english)
    def letter(self):
        if a in self.russian:
            return 'Русская буква'
        if a in self.english:
            return 'English letter'
        
    def len_(self):
        len_1=len(self.russian)
        len_2=len(self.english)
        
        return f'Кол-во русских букв {len_1} , кол-во английских букв {len_2}'
    @staticmethod
    def example():
        print('England')
    
      
if __name__=='__main__':
    

    
    a=input('').lower()
    print(string.ascii_uppercase)
    b=Alphabet(['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ё','э','ж','д','л','о','р','п','а','в','ы','ф','я','ч','с','м','и','т','ь','б','ю'],['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','m','n','b','v','c','x','z'])
    print(b.letter())
    print(b.len_())
    Alphabet.example()
    

    