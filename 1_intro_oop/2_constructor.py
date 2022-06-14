#
class Car():
    def __init__(self,xuatxu,namradoi):
        self.xuatxu=xuatxu
        self.namradoi=namradoi
    def xuat_xu(self):
        return self.xuatxu

vinfast=Car('vietnam',2019)
print(vinfast.xuat_xu())

#cso thể thay biến self bằng biến kahsc được