#biến class, và biến instance
#ví dụ 1: biến class
class conmeo():
    #varianle class
    thue_mua_meo_ngoai=1.2

    def __init__(self,name,age,color,price):
        self.name=name
        self.age=age
        self.color=color
        self.price=price
    
    def name(self):
        return self
    
    def giameo(self):
        return self.price*conmeo.thue_mua_meo_ngoai

#có thể thay đổi biến thue_mua_meo_ngoai ở bên ngoài class
con_meo_1=conmeo('thanh',21,'blue',2000)
conmeo.thue_mua_meo_ngoai=1.5
print(f'gia con meo thanh: {con_meo_1.giameo()} $')

#end ví dụ1

#ví dụ2
class car():
    tax=1
    def __init__(self,hang_san_xuat,mau_xe,nam_phat_hanh,gia_thanh):
        self.hang_san_xuat=hang_san_xuat
        self.mau_xe=mau_xe
        self.nam_phat_hanh=nam_phat_hanh
        self.gia_thanh=gia_thanh
    def mau_xe(self):
        return self.mau_xe
    def gia_mua_tai_viet_nam(self):
        return self.gia_thanh*self.tax


vinfast=car('vin','x3',2019,1000)
BMW=car("BMW",'x6',2022,4000)

#biến instance 
vinfast.tax=1.2
print(f'gia mua o viet nam cua xe vinfast: {vinfast.gia_mua_tai_viet_nam()} $')
#biến instance 
BMW.tax=1.5
print(f'gia mua BMW ở việt nam: {BMW.gia_mua_tai_viet_nam()} $')

print(car.__dict__)
