'''class employee: 
    def __init__(self): 
        self.name="ashish"
e1=employee()
print(e1.name) '''
class employee: 
    def __init__(self): 
        self.__name="ashish"
e1=employee()
print(e1._employee__name)             