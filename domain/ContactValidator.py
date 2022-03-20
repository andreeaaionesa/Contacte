from domain.ContactExceptions import ContactExceptions

class ContactValidator:
    
    def validate(self,c,l ):
        err=""
        
        for elem in l:
            if elem.get_nrph()==c.get_nrph():
                err+="Number exists"
                
        if err!="":
            raise ContactExceptions(err)
            