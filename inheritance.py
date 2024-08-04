class employee: 
    def __init__(self,name,id): 
        self.name=name
        self.id=id
    def showdetails(self):  
        print(f"hey,my name is {self.name} my id is {self.id}")     
class programer(employee):  
    def showlang(self): 
        print('the deafult language is python')         

e1=employee("ashish",10)
e1.showdetails()
e2=programer('akash',5)
e2.showdetails()
e2.showlang()