class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    @property  #biến hàm phía sau giống thuộc tính
    def full_name(self):
        return f'{self.brand} {self.model}'

    @full_name.setter #setter
    def full_name(self,full_name):
        self.brand,self.model=full_name.split(" ")

    @full_name.deleter #deleter
    def full_name(self):
        self.brand=None
        self.model=None
        print('deleted fullname')

car1=car('vin','luxA')
#giống như thuộc tính (property)
print(car1.full_name)

#setter
car1.full_name='BMV i320'
print(car1.brand)

#deleter
del car1.full_name
print(car1.brand,car1.model)

