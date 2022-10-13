# 2-masala
# a, b = input().split()
# if a != b:
#     if a > b:
#         print(">")
#     else:
#         print("<")
# else:
#     print("=")
# a, b = input().split()
# if a != b:
#     print('>') if (a>b) else print("<" )
# else:
#     print("=")
#4-masala
# a, b = input().split()
# print(int(a) * int(b))


# taking multiple inputs at a time. # and type casting using list() 
# function. 
# x = list(map(int, input("Enter a multiple value: ").split()))
# taking multiple inputs at a time. 
# c = [int(x) for 
# x in input("Enter multiple value: ").split()]

# year = int(input())
# if year % 400 == 0 and year % 4 == 0:
# 	print(f"12/09/{year}")
# else:
#     print(f"13/09/{year}")


# Kabisa
# year = int(input('Enter year : '))
 
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
#     print(f"12/09/{year}")
# else :
#     print(year, "is not a leap year.")

# let serie = "A465187";
# let check = 0;
# for (let i = 0; i < serie.length; i++){
#     if((serie[0] == "A") && (typeOf(serie[1::]) == "number") && (serie.length == 6) {
#         check+=1
#     }
# }
# console.log(check);


# Kiruvchi ma'lumotlar:
# Kirish ma'lumotlari uzunligi 7 ta belgili satr. =
# Satrning birinchi belgi lotin harfi A, =
# keyin 6 o'nlik raqamlari 0-9.=

# Chiquvchi ma'lumotlar:
# Javob chiqarish kerak(butun son).


# serie = "A987654"
# letter = serie[0]
# numSer = serie[1::]
# nums = '1234567890'
# value = 0
# for i in serie :
#     if (letter == 'A') and (numSer.isdigit()) and (len(serie) == 7 ):
#         value+=1
# if value > 0 :
#     value = 1
# print(value)
# print(numSer in nums)

#from pprint import pprint

# serie = "A987654"
# if (serie[0] == "A") and (serie[1::].isdigit) and len(serie) == 7 :

#     print(1)

# Kiruvchi ma'lumotlar:
# Kirish ma'lumotlari uzunligi 7 ta belgili satr. =
# Satrning birinchi belgi lotin harfi A, =
# keyin 6 o'nlik raqamlari 0-9.=

# if serie[1::].isdigit() and serie[0].isupper() and serie[0].isalpha() and len(serie) == 7 :

# serie = input()
# len(serie) == 7
# if serie[1::].isdigit() and serie[0].isupper() : # and serie[0].isalpha() 
#     print(1)
# else :
#     print(0)
# year = int(input())
# if 10000 > year > 0 :
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
#         if 0 < year <= 9 :
#             print(f"12/09/000{year}")
#         elif 10 <= year <= 99 :
#             print(f"12/09/00{year}")
#         elif 100 <= year <= 999 :
#             print(f"12/09/0{year}")
#         else :
#             print(f"12/09/{year}")
#     else :
#         if 0 < year <= 9 :
#             print(f"13/09/000{year}")12 
#         elif 10 <= year <= 99 :
#             print(f"13/09/00{year}")
#         elif 100 <= year <= 999 :
#             print(f"13/09/0{year}")
#         else :
#             print(f"13/09/{year}")


#43
# a, b = input().split()
# [a, b] = [b, a]
# print(a,b)

# serie = input()
# if len(serie) == 7 and serie[0] == "A" and serie[1::].isdigit() :
#     print(1)



# “Deyarli” tub son
# n va 4ta a, b, c va d turli sonlar beriladi. 
# Ushbu 4ta sonning hech qaysisiga qoldiqsiz bo’linmaydigan sonlarni “Deyarli” tub son deymiz.
# Sizning vazifangiz [1; n] oralig’ida nechta “Deyarli” tub son borligini topish.

# Kiruvchi ma'lumotlar:
# Birinchi qatorda t, testlar soni (1 ≤ t ≤ 105).
# Har bir test uchun uchun alohida qatorda beshta butun son: n, a, b, c, d (2 ≤ n ≤ 1015 , 2 ≤ a, b, c, d ≤ 106) kiritiladi.

# Chiquvchi ma'lumotlar:
# Har bir test uchun alohida qatorda bittadan butun son, masalaning javobini chop eting.

# Misollar
# #	input.txt	output.txt
# 1	
# 2
# 20 2 3 10 7
# 40 11 19 23 5
# 6
# 26


# len(nums) == nums[0::n+1]
# for i in nums :
#     if int(i) in nums :
#         print(f"in {i}")
#     else :
#         print("0")

        
# result = any(item in test_list for item in test_list)



# from operator import not_



# n = int(input())
# nums = input().split()


#Sizga N ta elementdan iborat A to’plam hamda K soni berilgan, 
# A to'plamda K sonining bo'luvchilari bor.
# (Faqatgina K soni bo'lmasligi mumkin).
# K sonining nechta bo'luvchisi to'plamda yo'q ekanligini topishingiz kerak.


#a = int(input())
#print(a+2)


#813

# n = int(input())
# summ = 0
# for i in range(1, n+1) :
#     if 99 < i < 1000 :    
#         summ += 3
#     elif 9 < i < 100  :
#         summ += 2
#     else :
#         summ += 1
# print(summ)


# n = int(input())
# val = 0
# i = val+2 if n > 9 else val + 1
# print(val)


# n = int(input("Son kiriting: "))
# a = [1000000000, 1000000, 1000, 100 ]
# b = ["milliard", "million", "ming", "yuz"]
# c = ["","o'n","yigirma","o'ttiz","qirq","ellik","oltmish","yetmish","sakson","to'qson"]
# d = ["","bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz"]
# def say(long, n)
# for i in range(0, 4) :
#     if n >= a[i] :
#         say(n/a[i] + b[i]  + say(n%a[i]))



# # 10
# n = int(input())
# aa,bb,cc = input().split()
# [a,b,c] = [int(aa),int(bb),int(cc)]
# summ = a+b+c
# if n <= summ :
# 	print("Yes", type(summ))
# else :
#   	print("No")

# min and max

# import math 

# string_list = ["1", "2", "3"]
# integer_map = map(int, string_list) # Maps each string to an int.
# integer_list = list(integer_map) # Converts mapped output to a list of ints.
# print(integer_list, type(string_list))

# nList = str(input())
# integerMap = map(int, nList)
# n = list(integerMap)
# # listlar qiymatlari qiymatlar
# sumMin = 0
# sumMax = 0
# # Copy listlar
# minn = n.copy()
# maxx = n.copy()
# # min bn maxni chopish
# minNum = min(minn)
# maxNum = max(maxx)
# maxList = maxx.remove(minNum)
# minList = minn.remove(maxNum)
# # Sum lists
# for ele in range(0, len(minn)):
#     sumMin = sumMin + minn[ele]
#     sumMax = sumMax + maxx[ele]
# print(sumMin, sumMax)


# print(sumMin, sumMax, n)
# print(n)

# n = input()
# yuza = ['1','2','3','4','5','6']
# for i in range(0,7) :
#     if n in yuza :
#         print(n)



#336-masala

# Bitboyda 1 tiyinlik tanga bor, uning bu tangasi ketma-ket tashlanganda hech qachon ketma-ket uch marotaba gerb tomoni bilan tushmaydi.
# Bitboy bu tangani ketma-ket N marotaba tashlaganda tanganing tushish ketma-ketligi variantlar sonini aniqlang.


# Kiruvchi ma'lumotlar:
# Kirish faylining dastlabki satrida bitta butun son, T(1 ≤ T ≤ 105) testlar soni kiritiladi.

# Har bir test uchun alohida satrda bitta butun son, N(1 ≤ N ≤ 1018) tanga tashlashlar soni kiritiladi.

# Chiquvchi ma'lumotlar:
# Chiqish faylida har bir test uchun alohida satrda so’ralgan javobni 109+7 ga bo’lgandagi qoldiqni chop eting!

# Misollar
# #	input.txt	
# 2
# 4
# 5
# output.txt
# 13
# 24


# test = int(input())
# arr = []
# if 1<= test <= 10**5 :
#     for i in range(test) :
#         n = int(input())
#         if 1 <= n <= 10**18:
#             arr.append(n)
# print(arr)


# 0091
# Palindrome
# Sizda a va b satrlar mavjud. Quyidagi shartlarni qanoatlantiruvchi s satrni hosil qiling:

# s ni s = sa+sb ko’rinishida ifodalab bo’lsin. Bu yerda sa a satrning bo’sh bo’lmagan qism satri, sb esa b satrning bo’sh bo’lmagan qism satri hisoblanadi.
# s palindrome satr bo’lsin
# s satrning uzunligi imkon qadar uzun bo’lsin.

# Kiruvchi ma'lumotlar:
# INPUT.TXT kirish faylining dastlabki satrida bitta butun son, T(1 ≤ T ≤ 10) testlar soni kiritiladi.

# Keyin esa har bir test uchun alohida ikkita satrda a va b(1 ≤ |a|, |b| ≤ 105) satrlar kiritiladi.

# Barcha testlardagi |a| lar yig’indisi 2*105 dan oshmaydi.

# Barcha testlardagi |b| lar yig’indisi 2*105 dan oshmaydi.

# Chiquvchi ma'lumotlar:
# OUTPUT.TXT chiqish faylida har bir test uchun alohida satrda hosil qilish mumkin bo’lgan s satrning leksikografik eng kichik qiymatini chop eting. Agar s satrni hosil qilishning imkoni bo’lmasa -1 chop eting.

# testlar soni
# test = int(input())
# slov = []
# # testlar
# for i in range(test) :
#     a = str(input())
#     b = str(input())
#     slov.append([a,b])
# # Testlarni tekshirish
# for arr in slov :

#     if arr[0] in arr[1] :
#         print(arr + arr.sort())






# Azimjon va Davlatbek bugun bir o'yin o'ynashmoqda. 
# Azimjon bitta sonini o'ylaydi va bu sonni Davlatbekga aytmaydi. 
# Ammo Azimjon Davlatbekka o'ylagan soni [a,b] oraliqda ekanligini aytadi. 
# Davlatbek Azimjon o'ylagan sonni topish uchun o'zidan taxminiy sonlarni aytishni boshlaydi va 
# o'zi aytgan sonlar ichida Azimjon o'ylagan son borligiga 100% ishonch xosil qilgan payti bu jarayonni tugatadi. 

# Savol: Davlatbek eng kamida nechta urunishda Azimjon o'ylagan sonni 100% aytgan bo'ladi?

# aa,bb = input().split()
# if 0 < a <= 1000 and 0 < a <= 1000 :
# 	print(b-a)


# aa,bb = input().split()
# a = int(aa)
# b = int(bb)
# if b % a == 0 :
# 	print("Yes")
# else :
# 	print("No")


# 0728
# aa, bb = input().split()
# [a, b] = [int(aa), int(bb)]
# while a % b != 0 :
#     a+=1
# print(a)

# aa,bb = input().split()
# [a, b] = [int(aa), int(bb)]
# if a == b :
#     print(1)
# elif a>b:
#     print(b)	
# print(a,b)


# 555
# a = 456
# yuz = a // 100 
# on = a // 10 - yuz * 10
# bir = a % 10
# print(yuz,on,bir)


#0608
# a,b = input().split()
# if len(b) == int(a):
# 	print("yes")
# else :
#   	print("no")


# aa,bb = input().split()
# [a, b] = [int(aa), int(bb)]
# if 1 <= a <= b <= 1000 :
#     if a == b:
#         print(1)
#     else :
#         print(b-a)


# aa,bb = input().split()
# [a, b] = [int(aa), int(bb)]
# print(b-a+1)


# log2\4 =16

# 0910
# import math 
# n = int(input())
# # ik = n//2
# lo = math.log(n,2)
# print(lo)



# # 0293
# 1-7-1101000 
# 2-5-1100101
# 3-11-1101100
# 4-11-1101100
# 5-14-1101111


# 1 0000000
# 2 0000001
# 3 0000010
# 4 0000011
# 5 0000100
# 6 0000101
# 7 0000110
# 8 0000111


# 1100101
# 2
# 1101000
# 4
# 1101100


# m = 0
# for i in range(0,10):
# 	m+=i
# print(m)

# xx1,yy1,xx2,yy2 = input().split()
# [x1,y1,x2,y2] = [xx1,yy1,xx2,yy2]
# space = 8
# time = 0.5
# if 0 < x1 <= 1000000 :
#     x = x2-x1
#     y = y2-y1
#     print(x,y)


# a = int(input())
# if a % 2 !=  0 :
#     print(True)
# else :
#     print(False)

# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/MirboboyevJasurjan/PythonProblems.git
# git push -u origin main

# 479
# n = int(input())
# if 1 <= n < 100:
#     print(n/100)
# elif 100 <= n <= 10000:
#     print(n//100)


#0139

# 4 
# 1 1
# 2 2 2
# 3 3 3 3

# n = int(input())
# t = input()
# arr = []

# for i in t:
#     arr.append(t[i])
# print(arr)
# bir = []
# ikki = []
# uch = []
# tort=[]
# besh = []
    # if t[i] == 1:
    #     bir.append(i)
    # elif t[i] == 2:
    #     ikki.append(i)
    # elif t[i] == 3:
    #     uch.append(i)
    # elif t[i] == 4:
    #     tort.append(i)
    # elif t[i] == 5:
    #     besh.append(i)
# print(bir,'\n',ikki,'\n',uch,'\n',tort,'\n',besh)


#127
# n = int(input())
# a = input().split()
# arr1 = [3,4,1,7]
# arr2 = [0,1,1,1,0,0,0,1]
# maxArr = max(arr1)
# empty = []
# print(maxArr)
# for i in range(0, maxArr) :
#     if arr1[i] == i :
#         empty.append(1)
#     else :
#         empty.append(0)
# print(empty)

# def find_missing(arr1, arr2):

#     # Set longer array to lst1, shorter to lst2 
#     if len(arr1) > len(arr2):
#         lst1 = arr1
#         lst2 = arr2
#     else:
#         lst1 = arr2
#         lst2 = arr1

#     # Go through elements in longer list
#     for element in lst1:

#         # If this element is not in lst2, we found it, return result
#         if element not in lst2:
#             return element



# aa,bb,cc = input.split()
# [a,b,c] = [int(aa),int(bb),int(bb)]
# if a < 100000 and b < 100000 and c < 100000 :
#     if a > b > c:
#         print(a-c)
#     elif a> c >b:
#         print(a-b)
#     elif b> c >a:
#         print(b-a)
#     elif b> a >c:
#         print(b-c)
#     elif c> a >b:
#         print(c-b)
#     elif c> b >a:
#         print(c-a)


n = 3
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
slov = text.split()
for i in text :
    if len() > n  :
        slov == slov[::-1] 
        print(slov[::-1])