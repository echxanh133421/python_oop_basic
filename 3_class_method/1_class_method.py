#class method:
class car():
    tax=1.2
    car_number=0
    def __init__(self,hang_san_xuat,mau_xe,nam_phat_hanh,gia_thanh):
        self.hang_san_xuat=hang_san_xuat
        self.mau_xe=mau_xe
        self.nam_phat_hanh=nam_phat_hanh
        self.gia_thanh=gia_thanh
    

    #regular method: hàm bình thường
    def mau_xe(self):
        return self.mau_xe
    def gia_mua_tai_viet_nam(self):
        return self.gia_thanh*self.tax
    
    def hien_thi(self):
        print(self.hang_san_xuat,self.mau_xe,self.nam_phat_hanh,self.gia_thanh)
    #class method
    @classmethod
    def set_tax(cls):
        cls.tax=1.5
    
    @classmethod
    def from_string(cls,string_car):
        hang_san_xuat,mau_xe,nam_phat_hanh,gia_thanh=string_car.split('-')
        nam_phat_hanh=int(nam_phat_hanh)
        gia_thanh=float(gia_thanh)
        #coi cls giống __init__(): chỉ truy xuất đến các biến trong __init__()
        #không truy xuất được các hàm khác
        return cls(hang_san_xuat,mau_xe,nam_phat_hanh,gia_thanh)

vin=car('vinfast','x5',2019,1000)
bmw=car('BMW','x10',2022,4000)
#ví dụ1:
vin.set_tax()
print(car.tax)
print(bmw.gia_mua_tai_viet_nam())

#ví dụ2:
car_string='toyota-g6-2021-3500'
toyo=car.from_string(car_string)
toyo.hien_thi()
