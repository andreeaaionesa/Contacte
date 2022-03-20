from domain.Contact import Contact
from repository.Repo import Repo
from domain.ContactExceptions import ContactExceptions


class Menu:
    def __init__(self): 
        self.__repo=Repo()
        
    def print_menu(self):
        stri="\t Available commands \n"
        stri+="\t 0-Exit \n"
        stri+="\t 1-Update a contact \n"
        stri+="\t 2-Get all contacts \n"
        stri+="\t 3-Get all work \n"
        stri+="\t 4-Get all personal \n"
        stri+="\t 5-Filter work \n"
        stri+="\t 6-Filter personal \n"
        stri+="\t 7-Sort work \n"
        stri+="\t 8-Sort personal \n"
        print (stri)
        
    def start_menu(self):
        C1=Contact("Ana", "+40-765-876999", "w")
        C2=Contact("Andrei", "+40-765-345886", "w")
        C3=Contact("Barbara", "+40-765-870006", "w")
        C4=Contact("Maria", "+40-765-878886", "p")
        C5=Contact("Crina", "+40-765-873336", "p")
        C6=Contact("Paul", "+40-765-878999", "p")
        
        self.__repo.add(C1)
        self.__repo.add(C2)
        self.__repo.add(C3)
        self.__repo.add(C4)
        self.__repo.add(C5)
        self.__repo.add(C6)
        comm=""
        ok=True
        self.print_menu()
        while ok:
            comm=int(input("Give me a command: "))
            if comm==0:
                ok=False
                print("Exit")
            elif comm==1:
                index=int(input("Give me an index: "))
                new_name=input("Give a name: ")
                new_nrph=input("Give me nr: ")
                new_categ=input("Give me a categ")
                try:
                    self.__repo.update_c(index, new_name, new_nrph, new_categ)
                except ContactExceptions as e:
                    print (e)
                
            elif comm==2:
                print(self.__repo.get_all())
            elif comm==3:
                print (self.__repo.get_all_w())
            elif comm==4:
                print (self.__repo.get_all_p())
                
            elif comm==5:
                try:
                    print(self.__repo.filter_W())
                except Exception as e:
                    print (e)
            elif comm==6:
                try:
                    print(self.__repo.filter_p())
                except Exception as e:
                    print (e)
                
            elif comm==7:
                print (self.__repo.sorted_w())
            elif comm==8:
                print (self.__repo.sorted_p())
            self.print_menu()
Menu=Menu()
Menu.start_menu()

                