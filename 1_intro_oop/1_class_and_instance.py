#object oriented programming
#định nghĩa class:
class car():
    def thuong_hieu(self,x):
        return x

BMW=car()

BMW.xuatxu='germany'
BMW.namradoi=1969

print(type(BMW))
print(BMW.xuatxu,BMW.namradoi)


vinfast=car()
print(vinfast.thuong_hieu("vietnam"))

#self: trỏ đến instance vinfast, BMW

