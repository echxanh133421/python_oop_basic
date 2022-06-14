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
#tính kế thừa: trong công ty có nheiefu chức vụ nân viên khác nhau, nhwung có những đặc tính chung

class developer(employee):
    co_salary=1.02
    def __init__(self, first, last, pay, program_language):
        super().__init__(first, last, pay)
        self.program_language=program_language

class manager(employee):
    co_salary=1.5
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees==None:
            self.emloyees=[]
        else:
            self.employees=employees
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('--',emp.full_name())


dev1=developer('cuong','pham',2000,'python')
dev2=developer('thanh','it',3000,'c#')

man1=manager('tuan','truong',10000,[dev1,dev2])
man1.remove_employee(dev1)
man1.add_employee(developer('hoang','nguyen',1500,'c++'))
man1.print_emp()
