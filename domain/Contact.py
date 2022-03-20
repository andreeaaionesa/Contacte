class Contact:
    def __init__(self,name,nrph,categ):
        self.__name=name
        self.__nrph=nrph
        self.__categ=categ

    def get_name(self):
        return self.__name


    def get_nrph(self):
        return self.__nrph


    def get_categ(self):
        return self.__categ


    def set_name(self, value):
        self.__name = value


    def set_nrph(self, value):
        self.__nrph = value


    def set_categ(self, value):
        self.__categ = value

    def __str__(self):
        return "Contact("+str(self.__name) +","+str(self.__nrph) +","+str(self.__categ)+")"
    
    def __repr__(self):
        return self.__str__()