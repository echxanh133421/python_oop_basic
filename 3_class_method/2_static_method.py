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
    
    @staticmethod
    def nhan_dinh_gia(gia_thanh):
        if gia_thanh>=1000:
            return 'expensive'
        else:
            return 'cheap'
    
vin=car('vinfast','x5',2019,600)
bmw=car('BMW','x10',2022,4000)


print(vin.nhan_dinh_gia(vin.gia_thanh))
print(bmw.nhan_dinh_gia(vin.gia_thanh))
print(bmw.nhan_dinh_gia(bmw.gia_thanh))
#NÊN DÙNG CÁCH VIẾT NÀY VỚI PHƯƠNG THỨC TĨNH
print(car.nhan_dinh_gia(bmw.gia_thanh))
