# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:01:00 2023

@author: USER
"""

# uyga vazifa

# 1 mashq
#son = int(input("juft son kiriting: "))
#if son%2==0:
#    print("Rahmat!")
#else:
#    print("bu son juft son emas")

# 2 mashq
#yosh=int(input("yoshiingiz nechida?>>>"))
#if yosh<4 or yosh>60:
#    print("bepul")
#elif yosh<18:
#    print('siz kirish 10000 so\'m') 
#else:
 #   print("sizga kirish 20000 so'm")    

# 3 mashq

#son1=int(input('1 -chi sonni kiriting: '))
#son2 = int(input("2-chi sonni kiriting: "))
#if son1>son2:
 #   print(f"{son1} soni {son2} sonidan katta")
#elif son1==son2 :
 #   print("ikkala son teng")
#else:
 #   print(f"{son2} soni {son1} sonidan katta")    

# 4 mashq
#mahsulotlar=['sabzi', 'kartoshka', 'piyoz', 'tuxum','tarvuz', 'qovun', 'gilos', 'pomidor']
#savat=[]
#for n in range(5):
#    savat1=input(f"{n+1} mahsulotni kiriting: ")
#    savat.append(savat1)
#bor_mahsulotlar=[]
#mavjud_emas=[]
#if savat:
#    for zakas in savat:
#        if zakas in mahsulotlar:
#            bor_mahsulotlar.append(zakas)
#        else:
#            mavjud_emas.append(zakas) #print(mavjud_emas)       
#if mavjud_emas:
#   print(f"quyidagi mahsulotlar do'konimizda yo`q: {mavjud_emas}")
#else:
    
 #  print("siz so'ragan barcha mahsulotlar do`knimizda bor")

# 5 mashq
#foydalanuvchilar=['sarvar', 'anvar', 'vali', 'diyor', 'sherbek']
#yangi_login=input("yangi login tanlang ")
#yangi_login.lower()
#if yangi_login in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print(f"Xush kelibsiz, {yangi_login.title()}!")    

# 6 mashq
#son = int(input('butun son kirting: >>>'))
#bolinuvchilar=[]
#if son%2==0:
#    bolinuvchilar.append(2)
#3if son%3==0:
#    bolinuvchilar.append(3)
#if son%4==0:
#    bolinuvchilar.append(4)
#3if son%5==0:#
#    bolinuvchilar.append(5)
#3##3if son%6==0:
 #   bolinuvchilar.append(6)
#if son%7==0:
 #   bolinuvchilar.append(7)
#if son%8==0:
 #   bolinuvchilar.append(8)
#if son%9==0:
 #   bolinuvchilar.append(9)
#if son%10==0:
 #   bolinuvchilar.append(10)
#3print(f"{son} soni {bolinuvchilar} sonlariga qoldiqsi bo'linadi")  
  
son=int(input("butun son kiritng>>>"))
bolinuvchilar=[]
for n in range(2,11):
    if son%n==0:
        bolinuvchilar.append(n)
print(f"{son} soni {bolinuvchilar} ga qoldiqsiz bo'linadi")        




















