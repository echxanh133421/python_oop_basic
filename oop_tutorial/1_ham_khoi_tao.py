#hàm khởi tạo: dùng khi khởi tạo đối tượng
'''
- nên ghi các thuộc tính trong đây
- thuộc tính được ghi trong đây được gọi là thuộc tính cá thể; dùng riêng cho đối tượng riêng biệt
'''


#thuộc tính của lớp
'''
- tạo ở ngoài hàm __init__()
-thuộc tính lớp là thuộc tính dùng chung cho mọi đối tượng
'''

#hàm __str__():in ra đối tượng từ hàm print khi sử dụng

class Dog:

    #class attribute:
    species='chihuahua'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

if __name__=='__main__':
    #khởi tạo đối tượng:
    A=Dog('milu',4) #không có 2 giá trị khởi tạo sẽ lỗi
    print(A.name,A.age)
    print(A.species)
    #sử dụng hàm __str__()
    print(A)