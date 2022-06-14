class employee:
    co_salary=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@gmail.com'
        self.pay=pay
    
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_co_salary(self):
        self.pay=int(self.pay*self.co_salary)
        return self.pay
    
    #ham1
    def __repr__(self):
        return f'employee {self.first}, {self.last}, {self.pay}'
    #ham2
    def __str__(self):
        return f'{self.first}-{self.last}'
    #ham3
    def __add__(self,orther):
        return self.pay + orther.pay
    #ham4
    def __len__(self):
        return len(self.full_name())

emp1=employee('cuong','pham',1500)
emp2=employee('huyen','phan',2000)
#ham3
print(emp1+emp2)
print(employee.__add__(emp1,emp2))
#ham4
print(emp1.__len__())
print(len(emp1))

#còn nhiều hàm mặc định của class hơn nữa