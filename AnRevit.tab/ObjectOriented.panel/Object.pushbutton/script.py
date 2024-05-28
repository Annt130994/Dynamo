# class SieuNhan:
#     pass
# sieu_nhan_A = SieuNhan()
# sieu_nhan_A.ten = "Sieu nhan do"
# sieu_nhan_A.vu_khi = "Guom"
# sieu_nhan_A.mau_sac = "Do"

# print("Ten cua sieu nhan:",sieu_nhan_A.ten)
# print("Vu khi:",sieu_nhan_A.vu_khi)
# print("Mau sac:",sieu_nhan_A.mau_sac)



# class SieuNhan:
#     so_thu_tu = 1
#     suc_manh  = 50
#     stt       = 10
#     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
#         self.ten = para_ten
#         self.vu_khi = para_vu_khi
#         self.mau_sac = para_mau_sac
#         self.stt = SieuNhan.so_thu_tu
        
#         SieuNhan.so_thu_tu += 1
    
# sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
# sieu_nhan_B = SieuNhan("Sieu nhan vang", "Kiem", "Vang")

# print(sieu_nhan_A.stt)
# print(sieu_nhan_B.stt)
# print(SieuNhan.so_thu_tu)


# # CLASS, INSTANCE, HÀM CONSTRUCTOR
# class AN():
#     def __init__(self, ten, namsinh, quequan, tuoi):
#         self.ten_1 = ten
#         self.nam_sinh = namsinh
#         self.que_quan = quequan
#         self.tuoi_1 = tuoi
#     def Ten(self):
#         return self.ten_1
#     def Nam_Sinh(self):
#         return self.nam_sinh
#     def Que_Quan(self):
#         return self.que_quan
#     def Tuoi(self):
#         return self.tuoi_1
# lylich = AN("An", "1994", "Đồng Tháp", "30")
# print('Tôi tên là: {}'.format(lylich.Ten()))
# print('Tôi sinh năm: {}'.format(lylich.Nam_Sinh()))
# print('Quê quán tôi ở: {}'.format(lylich.Que_Quan()))
# print('Tuổi đang ở độ tuổi: {}'.format(lylich.Tuoi()))
# # CLASS VARIABLES (BIẾN CỦA LỚP)
# class Car():
#     tax = 1
#     Car_number = 0
#     def __init__(self, hieuxe, model, namsanxuat, gia):
#         self.hieu_xe = hieuxe
#         self.model_1 = model
#         self.nam_san_xuat = namsanxuat
#         self.gia_1 = gia
#         Car.Car_number += 1
#     def Thuong_Hieu(self):
#         return self.hieu_xe
#     def Gia_Xe(self):
#         return (self.gia_1 * Car.tax)
# print(Car.Car_number)
# Car.tax = 2
# car_1 = Car("BMW", "I520", "2020", 1000)
# car_2 = Car("Vinfast", "LuxA 2.0", 2018, 1200)
# print('Giá xe BMW là: {}'.format(car_1.Gia_Xe()))
# print('Giá xe Vinfast la: {}'.format(car_2.Gia_Xe()))
# # print(f"{car_1.Thuong_Hieu()} giá {car_1.Gia_Xe()}$")
# print(Car.Car_number)

# STATIC METHOD AND CLASS METHOD
class Car():
    tax = 1
    Car_number = 0
    def __init__(self, hieuxe, model, namsanxuat, gia):
        self.hieu_xe = hieuxe
        self.model_1 = model
        self.nam_san_xuat = namsanxuat
        self.gia_1 = gia
        Car.Car_number += 1
# REGULAR METHOD
    def Thuong_Hieu(self):
        return self.hieu_xe
    def Gia_Xe(self):
        return (self.gia_1 * self.tax)
# CLASS METHOD
    @classmethod
    def set_tax(cls):
        cls.tax = 2
    @classmethod
    def from_string(cls, car_string):
        hieuxe, model, namsanxuat, gia = car_string.split('-')
        namsanxuat = int(namsanxuat)
        gia = int(gia)
        return cls(hieuxe, model, namsanxuat, gia)
# STATIC METHOD
    @staticmethod
    def check_gia(gia_1):
        if gia_1 <= 1000:
            return "This car is cheap!"
        else:
            return "This car is expensive!"

car_temp = "Toyota-Camry-1969-900"
car_1 = Car("BMW", "I520", 2020, 1200)
car_2 = Car("Vinfast", "LuxA 2.0", 2018, 1200)
car_3 = Car.from_string(car_temp)
car_1.set_tax()
# print(Car.tax)
print(car_1.Gia_Xe())
print(car_2.Gia_Xe())
print(car_3.Gia_Xe())
print(car_3.hieu_xe, car_3.model_1, car_3.nam_san_xuat, car_3.gia_1)
# print('Giá xe BMW là: {}'.format(car_1.Gia_Xe()))
print(Car.check_gia(car_1.gia_1))
print(Car.check_gia(car_2.gia_1))
print(Car.check_gia(car_3.gia_1))

# TÍNH KẾ THỪA (INHERITANCE)
class Emloyee:
    co_salary = 1.05
    def __init__(self, first, last, pay):
        self.first_1 = first
        self.last_1 = last
        self.email = first + '.' + last + '@email.com'
        self.pay_1 = pay
    def fullname(self):
        return'{} {}'.format(self.first_1, self.last_1)
    def apply_co_salary(self):
        self.pay_1 = int(self.pay_1*self.co_salary)
        return self.pay_1

class Developer(Emloyee):
    co_salary = 1.05
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang_1 = pro_lang

class Manager(Emloyee):
    co_salary = 1.5
    def __init__(self, first, last, pay, employess = None):
        super().__init__(first, last, pay)
        if employess == None:
         self.emloyess_1 = []
        else:
         self.emloyess_1 = employess
    def add_employess(self, emp):
        if emp not in self.emloyess_1:
            self.emloyess_1.append(emp)
    def remove_employee(self, emp):
        if emp in self.employess_1:
            self.emloyess_1.remove(emp)
    def print_emp(self):
        for emp in self.emloyess_1:
         print('--', emp.fullname())

dev1 = Developer("An", "La", 400, "Python")
dev2 = Developer("An", "Đồng Tháp", 8000, "C#")

man1 = Manager('Trump', 'Donal', 1000, [dev1,dev2])
man1.print_emp()
print(dev1.fullname())
print(dev1.apply_co_salary())
print(dev2.fullname())
print(dev2.apply_co_salary())

# PHƯƠNG THỨC ĐẶC BIỆT
import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))
print('-'*50)
class Vit():
    def __init__(self, tencun, tenmatbanh, love):
        self.tencun_1 = tencun
        self.tenmatbanh_1 = tenmatbanh
        self.love_1 = love
Heo = Vit("Cún","Mặt Bành", "Yêu")
print(Heo.tencun_1, Heo.love_1, Heo.tenmatbanh_1)
print('-'*50)
    