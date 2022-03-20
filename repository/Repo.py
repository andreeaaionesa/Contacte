from domain.Contact import Contact
from utile import identify
from domain.ContactValidator import ContactValidator

class Repo:
    def __init__(self):
        self.__repo=[]
        self.__valid=ContactValidator()
        
    def add(self,c):
        self.__repo.append(c)
        
    def update_c(self,index,new_name,new_nrph,new_categ):
        if index>=0 and index<len(self.__repo):
            try:
                self.__valid.validate(Contact(new_name,new_nrph,new_categ), self.__repo)
                self.__repo[index].set_name(new_name)
                self.__repo[index].set_nrph(new_nrph)
                self.__repo[index].set_categ(new_categ)
                return "done"
            except Exception as e:
                print(e)
        else:
            raise Exception("The index is not valid!")
        
    def get_all(self):
        return self.__repo
    
    def get_all_w(self):
        l=[]
        for elem in self.__repo:
            if elem.get_categ()=="w":
                l.append(elem)
        return l
    
    def get_all_p(self):
        l=[]
        for elem in self.__repo:
            if elem.get_categ()=="p":
                l.append(elem)
        return l
    
    def filter_W(self):
        l=[]
        for elem in self.get_all_w():
            if elem.get_nrph()[-3:]=="999":
                l.append(elem)
        return l
    
    def filter_p(self):
        def f(x):
            if x.get_nrph()[-3:]=="999":
                return True
            return False
        return identify(self.get_all_p(),f)
    
    def sorted_w(self):
        return sorted(self.get_all_w(), key=lambda x:x.get_name())
    
    def sorted_p(self):
        return sorted(self.get_all_p(), key=lambda x:x.get_name())
    
    
    
    
    