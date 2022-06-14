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


emp1=employee('cuong','pham',1000)

print(str(emp1))
print(repr(emp1))

#sự khác nhau giữa str và repr
import datetime
today=datetime.datetime.now()

print(str(today))
print(repr(today))