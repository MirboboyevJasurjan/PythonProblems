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
# 4-masala
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

# year = int(input('Enter year : '))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
#     print("Kabisa yili")
# else :
#     print("Kabisa yili emas")


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

# from pprint import pprint

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


# 43
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


# Sizga N ta elementdan iborat A to’plam hamda K soni berilgan,
# A to'plamda K sonining bo'luvchilari bor.
# (Faqatgina K soni bo'lmasligi mumkin).
# K sonining nechta bo'luvchisi to'plamda yo'q ekanligini topishingiz kerak.


# a = int(input())
# print(a+2)


# 813

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


# 336-masala

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


# 0608
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


# 0139

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


# 127
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


# n = 3
# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
# slov = text.split()
# for i in text :
#     if len(slov) > n  :
#         slov == slov[::-1]
#         print(slov[::-1])

# Isfandiyorga algebra fanidan quyidagi vazifa uy vazifasiga berildi:
# f(x) =
# x5 + 8x4 – 5x3 + 3x2 + x – 12, bo’lsa f(n) ni toping. Ammo u dangasaligi uchun bu ishni o’zi qilgisi kelmayapti. Siz unga yordam bering.

# x = int(input("X: "))
# def sumX(x) :
#     # s = math.pow(x,5) + (8*(math.pow(x,4))) - (5* (math.pow(x,3))) + (3* (math.pow(x,2))) + x -12
#     s = x**5 + (8*(x**4)) - (5* (x**3)) + (3* (x**2)) + x -12
#     print(s)
# if x < 0 and -10>=x :
#     x=x*-1
#     sumX(x)
# elif x <= 10 :
#     sumX(x)

# Python program for practical application of sqrt() function

# # import math module
# import math

# # function to check if prime or not
# def check(n):
#     if n == 1:
#         return False

#         # from 1 to sqrt(n)
#     for x in range(2, (int)(math.sqrt(n))+1):
#         if n % x == 0:
#             return False
#     return True

# # driver code
# n = 23
# if check(n):
#     print("prime")
# else:
#     print("not prime")

# 138

# x = int(input())

# def sumX(x) :
#     s = (x**5 + (8*(x**4)) - (5* (x**3)) + (3* (x**2)) + x -12)
#     print(s)
# def check(x) :
#     if x <= 10 :
#         sumX(x)
#     elif x <= 0 and x<=-10 :
#         x=x*-15
#         sumX(x)
# check(x)

#


# son = input("butun son kiriting:")
# while True:
# 	if son.isdigit():
# 		print('tashakkur')
# 		break
# 	else:
# 		son = input("butun son kiriting:")

# from turtle import Screen, Turtle

# windowPy = Screen()

# import pygal
# line_chart = pygal.Line()
# line_chart.title = "Statistika"
# line_chart.x_labels = ["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentabr","Oktabr","Noyabr","Dekabr"]
# line_chart.add("Github",[14,4,18,15,1,0,2,3,2])
# line_chart.add("Instagram",[15,6,8,15,1,0,2,7,4])
# line_chart.add("Pinterest",[34,41,10,15,10,2,1,3])
# n = 0
# while n < 2 :
#     social_name = input("Social Media Name ")
#     social_param = input("Social Media Parametrs ").split()
#     line_chart.add(social_name, list(range(i in social_param)))
#     n+=1
# line_chart.render_in_browser()


# print(list(range(85)))


# n = int(input())
# if n % 4 == 0 :
#     res = n / 4 * 2
#     print(res)
# else :
#     print(-1)

# n = int(input())
# n = 7
# m = n//2
# il = math.sqrt(n)
# res = int(il*2)
# print(m)


# n = 7
# i = 0
# res = 0
# iDar = []
# while res <= 7 :
#     ik = 2
#     res = math.pow(2,i)
#     iDar.append(i)
#     i += 1
#     print(res, i)
# if iDar[-1] - 2**0 == n :
#     print(2)

# def isTwo(numb) :
# while n > numb :
# while nTim < n :
#     resDbl = int(math.pow(2, item))
#     nTim = resDbl
#     item += 1
#     arrIts.append(item)
#     arrDbls.append(resDbl)
# if arrDbls[-1] > n :
#     arrDbls.pop()
#     arrIts.pop()
# resTot = n-arrDbls[-1]

# import math
# n = 37
# def isTwo(two):
#     arrDbls = []
#     arrIts = []
#     nTim = 0
#     item = 0
#     while nTim < two:
#         resDbl = int(math.pow(2, item))
#         nTim = resDbl
#         item += 1
#         arrIts.append(item)
#         arrDbls.append(resDbl)
#     if arrDbls[-1] > two:
#         arrDbls.pop()
#         arrIts.pop()
#     resTot = two-arrDbls[-1]
#     print(resTot)
#     return resTot
# res = isTwo(n)
# if res > 2 :
#     res = isTwo(res)


# 3
# 0 0
# 2 1
# 2

# 0

# n = int(input("Bekatlar "))
# arr = []
# for i in range(0, n) :
#     aa,bb = input().split()
#     [a, b] = [int(aa),int(bb)]
#     arr.append([a,b])
#     for item in arr :
#         res = item[0]-item[1]
# print(res)

# uy raqami - xyz
# - xyz + yz


# arr = [1,2,3,4,3,2,1]
# arr.sort()
# item = 0
# while arr[item] != arr[item+1]:
#     item = item + 1
#     print(arr)
#     break
# arr = [1,2,3,4,3,2,1]
# setted = set(arr)
# print(setted, len(setted))
# arr.sort()
# for i in arr :
#     # print(i)
#     item = 0
#     while i == arr[item+1] :
#         arr.remove(i)
#         print(arr[item])
#         item+=1
# print(arr)

# arr = [1,2,3,4,3,2,1]


# 0009
# n = int(input())
# arr = input().split()
# while len(arr) != n :
#     arr.pop()
# for x in arr:
#     if arr.count(x) == 1:
#         print(x)
# print(arr)5

# print(arr)

# ints_list = [1, 2, 3, 4, 3, 2]

# temp = []

# for x in ints_list:
#     if x not in temp:
#         temp.append(x)

# ints_list = temp

# print(f'Updated List after removing duplicates = {temp}')

# values = [87, 94, 45, 94, 94, 41, 65, 94, 41, 99, 94, 94, 94]

# for x in values:
#     if values.count(x) > 1:
#         values.remove(x)
# print(values)  # [87, 45, 65, 41, 99, 94, 94] - 94 is still present twice


# 0011
# 2-max
# n(2 ≤ n ≤ 100) ta elementdan iborat butun sonli massiv berilgan.
# Massivning ikkinchi eng katta elementini aniqlang.

# Kiruvchi ma'lumotlar:
# Birinchi satrda massiv elementlar soni n natural soni beriladi.
# Keyingi qatorda nn ta nomanfiy butun son, massiv elementlari beriladi.
# Barcha kiruvchi ma'lumotlar qiymati 100 dan oshmaydi.

# Chiquvchi ma'lumotlar:
# Massivning ikkinchi eng katta elementini chiqaring.

# Misollar

# #	input.txt	output.txt
# 5
# 1 5 2 3 4
# 4

# 6
# 3 5 5 2 2 3
# 5

# n = int(input())
# arr = input().split()
# maxNumb = 0
# while len(arr) > n :
#     arr.pop()
# for i in arr :
#     if int(i) >= 2 and 100 >= int(i):
#         arr.remove(max(arr))
#         maxNumb = max(arr)
#         break
# print(int(maxNumb))


# n = int(input())
# # arr = input().split()
# nList = input().split()
# integerMap = map(int, nList)
# arr = list(integerMap)
# arr.sort()
# while len(arr) >= n :
#     arr.pop()
# if min(arr) > 1 and 101 > max(arr):
#     arr.remove(max(arr))
# print(arr[-1])

# n = int(input())
# nList = input().split()
# integerMap = map(int, nList)
# arr = list(integerMap)
# arr.sort()
# while len(arr) >= n :
#     arr.pop()
# if arr[0] > 1 and 101 > arr[-1] :
#     arr.remove(arr[-1])
#     print(arr[-1])
# else :
#     print(False)
# n = int(input())
# arr = input().split()
# maxNumb = 0
# while len(arr) >= n :
#     arr.pop()
# for i in arr :
#     if 101 > int(i) > 1:
#         arr.remove(max(arr))
#         maxNumb = max(arr)
#         print(int(maxNumb))
#         break
#     else :
#         break
# print(int(maxNumb))

# n = int(input())
# nList = input().split()
# integerMap = map(int, nList)
# arr = list(integerMap)
# while len(arr) >= n :
#     arr.pop()
# arr.sort()
# arr.pop()
# print(arr[-1])

# 0462
# k = int(input())
# txt = input().split()
# arr = []
# for i in txt :
#     if len(i) >= k :
#         arr.append(i[::-1])
#     print(i[::-1])
# print("".join(arr))
# if len(txt) < 16 :
  	# if 'sh' in txt :
        # print(txt[::-1])


# str = input()
# str1 = ""
# for i in str:
#     if (i == "s" and i+1== 'h') and (i == "c" and i+1== 'h') and (i == "n" and i+1== 'g'):
#         str1 = i[::-1] + str1
#     else:
#         str1 = i + str1
# print(str1)


#     # Given String
# # print("The original string is: ", str)
# # print("The reverse string is", reverse_string(str))  # Function call

# def reverse(str):
#     string = "".join(reversed(str)) # reversed() function inside the join() function
#     return string

# s = "JavaTpoint"

# print ("The original string is : ",s)
# print ("The reversed string using reversed() is : ",reverse(s) )


# 0008

# nList = input().split()
# integerMap = map(int, nList)
# n = list(integerMap)
# sumMin = 0
# sumMax = 0
# if len(n) != 5 :
#     n.pop()
# minn = n.copy()
# maxx = n.copy()
# minNum = min(minn)
# maxNum = max(maxx)
# maxList = maxx.remove(minNum)
# minList = minn.remove(maxNum)
# for ele in range(0, len(minn)):
#     sumMin = sumMin + minn[ele]
#     sumMax = sumMax + maxx[ele]
# print(sumMin, sumMax)

# letr = 10
# for i in range(0, 701) :
#     letr = letr ** i
#     print(letr)


# aa, bb, cc = input().split()
# [a,b,c] = [int(aa) ,int(bb) ,int(cc) ]
# sumPl = a+b+c
# if sumPl <= 1000 :
#     if sumPl % 2 == 0 :
#         sums = sumPl // 2
#         print(int(sums))
#     else :
#         sums = sumPl // 2 + 1
#         print(int(sums))


# aa, bb, cc = input().split()
# [a, b, c] = [int(aa), int(bb), int(cc)]
# def sumTwo(n) : 
#     if n % 2 == 0 :
#         return n // 2
#     else :
#         return (n // 2) + 1
    
# all =  sumTwo(a) + sumTwo(b) + sumTwo(c)
# print(int(all))

# if a % 2 == 0 :
#     sumA = a // 2
# else :
#     sumA = a // (2 + 1)
# if b % 2 == 0 :
#     sumB = b // 2
# else :
#     sumB = b // (2 + 1)
# if a % 2 == 0 :
#     sumC = c // 2
# else :
#     sumC = c // (2 + 1)


# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return False
#   val += 1
# if val % 2 == 0:
#     print("Ali")
# else:
#     print("Bobur")

# def isPrime(num) :
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#     if flag != True:
#         val += 1

# for i in range(1, n+1) :
#     isPrime(i)

# n = int(input())
# val = 0
# arr = []
# for i in range(0, n):
#     c = 0
#     for j in range(1, i):
#         if i % j == 0:
#             c+=1
#     if c==1 :
#         val +=1
#         arr.append(i)
# if val % 2 == 0:
#     print("Ali")
#     print(val, arr)
# else:
#     print("Bobur")
#     print(val, arr)



# 0693
# k = int(input())
# txt = input().split()
# k = int(input())
# txt = input()
# letter = txt.split(' ')
# arr = []
# for i in letter :
#     if len(i) > k :
#         arr.append(i[::-1])
#     else:
#         arr.append(i)
# print(" ".join(arr))

#0462

# txt = input()
# # letter = txt.split('')
# arr = []
# for i in txt :
#     if (i == "s" and i+1 == "h") and (i == "c" and i+1 == "h") and (i == "n" and i+1 == "g") :
#         continue
#     else:
#         arr.append(i[::-1])
#         # arr.append(i)
# print("".join(arr))


# str = input()
# str1 = ""
# for i in str:
#     for ind in range(1, len(str)) :
#         # if (i == "s" and str[ind+1]== 'h') and (i == "c" and str[ind+1]== 'h') and (i == "n" and str[ind+1]== 'g'):
#         #     str1 = i[::-1] + str1
#         # else:
#         if i == 's' and ind == "h":
#             str1 = i + ind+str
#         else :
#             str1 = i[::-1] + str1

# print(str1)

# str = 'asherzod'
# str1 = ''
# for i in str:
#     if (i == "s" or i == "c" and str.index(i)+1 == "h")  :
#         str1 = i + str1[::]
#     # else :
#     #     str1 = i[::-1] + str1
# print(str1)


# 0025

# def convert(seconds):
#     seconds = seconds % (24 * 3600)
#     hour = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     return "%d:%02d:%02d" % (hour, minutes, seconds)     
# n = int(input())
# print(convert(n))


# seconds = n % (24*3600)
# print(seconds)
# hour = n // 3600
# seconds = seconds % 3600
# print(seconds)
# minutes = seconds // 60
# seconds %= 60
# print(seconds)

# print(hour, minutes, seconds)


# O'NLIKDAGI SATR


# import math


# def isTwo(two):
#     arrDbls = []
#     arrIts = []
#     nTim = 0
#     item = 0
#     while nTim < two:
#         resDbl = int(math.pow(2, item))
#         nTim = resDbl
#         item += 1
#         arrIts.append(item)
#         arrDbls.append(resDbl)
#     if arrDbls[-1] > two:
#         arrDbls.pop()
#         arrIts.pop()
#     resTot = two-arrDbls[-1]
#     print(resTot)
#     return resTot
# res = isTwo(n)
# if res > 2 :
#     res = isTwo(res)





# def power(num, n):
 
#     if(n == 0):
#         return 1
#     elif(n % 2 == 0):
#         return power(num, n // 2) * power(num, n // 2)
#     else:
#         return num * power(num, n // 2) * power(num, n // 2)
 
# def checkRecursive(x, n, curr_num=1, curr_sum=0):
#     results = 0
#     p = power(curr_num, n)
#     while(p + curr_sum < x):
#         results += checkRecursive(x, n, curr_num + 1, p + curr_sum)
#         curr_num = curr_num + 1
#         p = power(curr_num, n)
#     if(p + curr_sum == x):
#         results = results + 1
#     return results

# if __name__ == '__main__':
#     x = int(input())
#     n = 2
#     print(checkRecursive(x, n))
 









# n = 50
# powTwo = 0
# iterr = 0
# while n > 2 :
#     if n // 2 :
#         n = n // 2
#         powTwo+=1
# print(powTwo)

# 
# aa, bb = input().split()
# [a, b] = [int(aa), int(bb)]
# powB = b*100
# print(f"{format(powB / a, '.2f')}%")


# aa, bb = input().split()
# [a, b] = [int(aa), int(bb)]
# powB = b*100
# res = powB/a
# if powB % a != 0 :
#     print(f"{int(res)}.00%")
# elif powB % a == "%02d" :
#     print(f"{round(float(res),2)}%")





# "%02d"



# return "%d:%02d:%02d" % (hour, minutes, seconds)     


# res = b * 100
# val = round(float(res) / a, 2)
# vall = round(val,2)
# print("%02d" % val)


# 0870
# from datetime import datetime
# start_time = datetime.now()

# aa, bb = input().split()
# [a, b, year ] = [int(aa), int(bb), 0]
# if (a > b) and (1 < a+b < 198) :
#     while a / b != 2.0 :
#         a+=1
#         b+=1
#         year+=1
#     print(year)
# else: 
#     print(-1)
    
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))




#0303
# n = int(input())
# scores = input().split()
# newArr = []
# newStr = ''
# for i in scores :
#     if 0 < int(i) < 101 :
#         newArr.append(1)
#     else :
#         newArr.append(0)
# if len(scores) == n :
#     if sum(newArr) == n:
#         scores.sort()
#         newStr = str(" ".join(scores))
#     else :
#         print(False)
# else :
#     print(False)
# print(newStr)




#0301
# n = int(input())
# scores = input().split()
# trueArr = scores
# sortedArr = trueArr.sort()
# print(sortedArr)
# if len(scores) == n :
    # for i in trueArr:
        # print(i)
        # if trueArr[int(i)] == scores[int(i)] :
        #     print(True)

# 0296
# v = int(input("Tb"))
# d = int(input("Speed Morning"))
# n = int(input("Speed Night"))
# dayInSec = 86400 
# dayMb



# 0269
# mil = 1000000
# k = int(input())
# allNums = []
# for i in range(1,mil,2) :
#     allNums.append(i)



# print(allNums)

# 0236  Completed

# n = int(input())
# arr = []
# arrMin = []
# for i in range(1,n+1) :
#     arr.append(i)
# if n < 0 :
#     n = (n*-1) 
#     for i in range(1,n+1) :
#         arrMin.append(i)
# if arr == [] :
#     print(f"-{sum(arrMin)-1}")
# else :
#     print(sum(arr))

# 0237 
# n = int(input())
# socks = input().split()
# newSock = []
# values = 0
# if len(socks) == n :
#     socks.sort()
# for i in range(1, len(socks)) :
#     if socks[i] == socks[i-1] :
#         values += 1
#         newSock.append(socks[i])
# print(values)


# 0238 
# n = int(input())
# nums = input().split()
# newArr = []
# val = 0
# if len(nums) == n :
#     nums.sort()

# for i in range(0, len(nums)):
#     if nums[i] not in newArr :
#         newArr.append(nums[i])
#     if nums[i] not in newArr :
#         val+=1
# print(nums, newArr)        
# print(val)


#     for i in range(0, len(nums)) :

#         if nums.count(i) > 1 :
#             x = nums.count(i)
#             print(x)
# else :
#     print(False)
# 0243
# n = int(input())
# day = 1
# rek = 5
# # whLik = 2
# whLikAll = 0

# for i in range(0, n) :
#     whLikAll = round(rek/2 * day)
#     rek+=1
#     day+=1
# print(whLikAll)


#0214
# from datetime import datetime
# start_time = datetime.now()

# # n,q = input().split()
# # a = input().split()
# n,q = 5,10
# a = [10,20,30,40,50]
# if len(a) == int(n) :
#     for i in range(0, int(q)) :
#         x = input()
#         if x in a:
#             print("YES")
#         else:
#             print("NO")
 
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))


#0257 
# n = input()
# freshZer = n.split('0')
# freshOne = n.split('1')
# print(freshZer,freshOne)

# if '0' in freshZer :
#     print("N0")
# else :
#     print("YES")






# a = int(input())
# if 1 <= a <= 20 :
#   n = n/(2*n-1)
#   print(int(n))


# 0445 accepted
# n = input()
# sums= []
# sumOfP = 0
# sumOfMult = 0
# for i in range(0,len(n)) :
#     sums.append(n[int(i)])
# for i in sums:
#     sumOfMult *= int(i) 
#     sumOfP += int(i)
# if int(n) > sumOfMult or int(n) > sumOfP :
#     print(n)
# elif sumOfP > sumOfMult :
#     print(sumOfP)
# elif sumOfP < sumOfMult :
#     print(sumOfMult)
# 2 3 10 21 34 


#0791

# n = int(input())
# n = 5
# arr = []
# for i in range(1,n+1) :
#     arr.append(i)
# start = 0
# i=2
# ler = start+i
# while len(arr) != 2 :
#     arr.pop(arr[i])
#     start+=1
#     i+=2
#     if len(arr) != i :
#         i+=2
#     else :
#         i=0
    
# print(arr)

#0603

# import math
# def sums3(p,q,r) :
#     res = 0
#     i = 0
#     while i<=p :
#         cnt = 0
#         j = 0
#         while j <=q :
#             a = math.pow(r,i)
#             b = (a-1)/a
#             cnt+=math.pow(b,j)
#         cnt2 = math.factorial(p) /( math.factorial((p-i)) * math.factorial(i))
#         if i&1 :
#             res -= cnt*cnt2
#         else:
#             res+= cnt*cnt2
#     return res

# response = sums3(2,3,2) % (math.pow(10,9)+7)

# print(response)


# 0076
# a = input().split()
# b = int(input())
# arr = [] 
# for i in range(0,len(a)) :
#     arr.append(int(a[i]))
# if b > sum(arr[0::6]) :
#     print(b-sum(arr))
# else:
#     print(0)






# 0053

# import math

# def count_diags(n):
#     if 1 <= n <= 10**9:
#         return int(n * (n - 3) / 2)
# n = int(input())
# print(count_diags(n))

# n = int(input())
# if n > 0 :
#   sumDig = int(n * ((n - 3) / 2))
#   print(sumDig)

# aa, bb = input().split()
# [a, b, year ] = [int(aa), int(bb), 0]
# if (a > b) and (1 < a < 100 and 1 < b < 100) :
#     while a / b != 2 :
#         a+=1
#         b+=1
#         year+=1
#     print(year)
# else: 
#     print(-1)



# def insertionSort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#         key = arr[i]
#         # Move elements of arr[0..i-1], that are #
#         # greater than key, to one position ahead 
#         # of their current position
#         j = i-1
#         while j >=0 and key < arr[j] :
#                 arr[j+1] = arr[j]
#                 j -= 1
#         arr[j+1] = key
 
# #sorting the array [12, 11, 13, 5, 6] using insertionSort
# # arr = [12, 11, 13, 5, 6]
# arr = list(map(int, input("Enter a multiple value: ").split()))
# insertionSort(arr)
# # lst = [] #empty list to store sorted elements
# print("Sorted array is : ")
# print(arr)

# for i in range(len(arr)):
#     lst.append(arr[i])     #appending the elements in sorted order
# print(lst,arr)


# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >=0 and key < arr[j] :
#                 arr[j+1] = arr[j]
#                 j -= 1
#         arr[j+1] = key


# t = int(input())
# ts = 0
# while t != ts :
#     arr = list(map(int, input().split()))
#     insertionSort(arr)
#     print(arr)    
#     ts+=1





# Sorting algoritm



# def sort(nums) :
#     for i in range(len(nums)) :
#         minpos = i
#         for j in range(i,len(nums)+1):
#             if nums[j] < nums[minpos] :
#                 minpos = j
#         temp = nums[i]
#         nums[i] = nums[minpos]
#         nums[minpos] = temp



# # nums = list(map(int, input("Enter a multiple value: ").split()))
# nums = [5,4,6,8,7,9]
# sort(nums)
# print(nums)




#0092
# t = int(input())
# attemp = 0
# if 1 <= t <= 1000 :
#     while t > attemp :
#         n = int(input())
#         if 1 <= t <= 1000 :
#             arr = list(map(int, input().split()))
#             attemp+=1
#             val = 0
#             for i in arr :
#                 if arr.count(i) > 1 :
#                     val +=1
#             print(val)



# 12981 10309 12981 19639 10309 22624 22624 19639 2273




#0099
# import math
# n = int(input())
# fact = math.factorial(n)
# m = n+1
# sumAll = fact % m
# print(sumAll)

# from datetime import datetime
# start_time = datetime.now()

# n = int(input())#
# # n = 6
# fact = 1
# for i in range (1,n+1):
#     fact = fact * i
# print(fact % (n+1) )


# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))


# def oddprod(l,h) :
#   p = 1
#   ml = (l%2>0) ? l : (l+1)
#   mh = (h%2>0) ? h : (h-1)
#   while ml <= mh do
#     p = p * ml
#     ml = ml + 2
#   end
#   p
# end

# def fact(k)
#   f = 1
#   for i in 1..k-1
#     f *= oddprod(3, 2 ** (i + 1) - 1)
#   end
#   2 ** (2 ** k - 1) * f
# end

# print fact(15)


# 0464
# n = int(input())
# item = 0
# val = 0
# def isEqual(l,r) :
#     target = 0
#     for i in range(0, len(l)) :
#         if l[i] == r[i] :
#             target+=1
#     if target > 0 :
#         print("YES")
#     else :
#         print("NO")
    
# if 1 <= n <= 10 :
#     while item != n:
#         s1 = input()
#         s2 = input()
#         arr1 = []
#         arr2 = []
#         if len(s1) > len(s2) :
#             for i in range (0, len(s2)) :
#                 arr1.append(s1[i])
#                 arr2.append(s2[i])
#         else :
#             for i in range (0, len(s1)) :
#                 arr1.append(s1[i])
#                 arr2.append(s2[i])

#         if len(arr1)>len(arr2) :
#             isEqual(arr2,arr1)
#         else:
#             isEqual(arr1,arr2)
#         item+=1
        
        
        
        # print("YES" if val >0 else "NO")    
        # if (1 <= len(s1) <= 10**5 ) and (1 <= len(s2) <= 10**5 ) :
        #     if len(s1) > len(s2) :
        #         for i in range (0,len(s1)) :
        #             arr1.append(s1[i])
        #             arr2.append(s2[i])
        #     else :
        #         for i in range (0,len(s2)) :
        #             arr1.append(s1[i])
        #             arr2.append(s2[i])
        #         if arr1[i] == arr2[i] :
        #             val += 1
        #         # else:
        #         #     val = 0
# 8 8 7 7
# 8 9 6 7
# 8
# 7.5
# 7.5 7.5 8.5 7.5
#0818

# writ = sum(map(float, input().split()))
# speak = sum(map(float, input().split()))
# listen = float(input())
# read = float(input())
# sumWrite = int(writ / 4)
# sumSpeak = int(speak / 4)
# overall = (sumWrite + sumSpeak + listen + read ) / 4
# if float(overall) < float(format(overall, '.2f')) < int(overall)+0.5 :
#     print(str(round(overall)+0.5))
# elif float(format(overall, '.2f')) > int(overall)+0.5 :
#     print(int(overall) + 1)

# else :
#     print(round(overall))



# print(format(overall, '.2f') < str(round(overall)+0.5))
# print(format(overall, '.2f'))
# print(str(round(overall)+0.5))
# f"{format(powB / a, '.2f')}%"


# Oqimga qarshi tezlik
# Matorli qayiq daryoda oqim bo'ylab t soat harakat qilib, 
# s km yo'l bosdi. 
# Agar daryo oqimining tezligi qayiqning turg'un suvdagi tezligidan v km/soat kam bo'lsa, 
# qayiqning oqimga qarshi tezligini toping.


# t soat 
# all yo'l
# qarshi v ?

# 1.5 60 20
# v = s/t 
# 60/1.5






# tt,ss,vv = input().split()
# [t,s,v] = [float(tt),float(ss),float(vv)]
# v1 = s/t
# print(int(v1-v))

# n = int(input())
# item = 0
# val = 0
# def isEqual(l,r) :
#     target = 0
#     for i in range(0, len(l)) :
#         if l[i] == r[i] :
#             target+=1
#     if target > 0 :
#         print("YES")
#     else :
#         print("NO")
    
# if 1 <= n <= 10 :
#     while item != n:
#         s1 = input()
#         s2 = input()
#         arr1 = []
#         arr2 = []
#         if len(s1) > len(s2) :
#             for i in range (0, len(s2)) :
#                 arr1.append(s1[i])
#                 arr2.append(s2[i])
#         else :
#             for i in range (0, len(s1)) :
#                 arr1.append(s1[i])
#                 arr2.append(s2[i])

#         if len(arr1)>len(arr2) :
#             isEqual(arr2,arr1)
#         else:
#             isEqual(arr1,arr2)
#         item+=1

# n = int(input())
# item = 0
# val = 0
# def isEqual(l,r) :
#     target = 0
#     for i in range(0, len(l)) :
#         if l[i] == r[i] :
#             target+=1
#     if target > 0 :
#         print("YES")
#     else :
#         print("NO")
    
# if 1 <= n <= 10 :
#     while item != n:
#         s1 = input()
#         s2 = input()
#         arr1 = []
#         arr2 = []
#         if len(s1) >1 and len(s2) > 1 :
#             if len(s1) > len(s2) :
#                 for i in range (0, len(s2)) :
#                     arr1.append(s1[i])
#                     arr2.append(s2[i])
#             else :
#                 for i in range (0, len(s1)) :
#                     arr1.append(s1[i])
#                     arr2.append(s2[i])

#             if len(arr1)>len(arr2) :
#                 isEqual(arr2,arr1)
#             else:
#                 isEqual(arr1,arr2)
#         item+=1

#0341
# n = int(input())
# arr = list(map(int, input().split()))
# val = 0
# if 1<= n <= 500 :
#     while len(arr) != n :
#         arr.pop()
#     for i in arr :
#         if 1<= i <=100 :
#             val-=1
#     if val == 0 :
#         res = [*set(arr)]
#         sumall = len(arr)-len(res)
#         if sumall == 0 :
#             print(n)
#         else:
#             print(len(arr)-len(res))

# n = int(input())
# arr = list(map(int, input().split()))
# if 1<= n <= 500 :
#     while len(arr) != n :
#         arr.pop()
#     arr.sort()
#     res = [*set(arr)]
#         print(n)
#     else :
#         print(sumall)


#     for i in arr :
#         if 1 <= i <= 100 :
#             if arr[i] not in arr1 :
#                 arr1.append(arr[i])
#             else:
#                 val+=1
# print(val)
# print(arr, arr1)






# for i in range(len(arr)) :
#     if arr[i] == arr[i-1] :
#         arr.remove(arr[i])
#     else:
# #         val+=1

# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# print("The original list is : " + str(test_list))
 
# res = []
# for i in test_list:
#     if i in res:
#         res.append(i)
 
# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension and arr.index

# # initializing list
# arr = [1, 5, 3, 6, 3, 5, 6, 1]
# print ('The original list is : '+ str(arr))

# # using list comprehension + arr.index()
# # to remove duplicated
# # from list
# res = [arr[i] for i in range(len(arr)) if i == arr.index(arr[i]) ]

# # printing list after removal
# # of duplicate
# print('The list after removing duplicates :'
# 		,res)


# #0309
# def binary_search(arr):
#     low = 0
#     high = len(arr) - 1
#     mid = 0 
#     while low <= high:
#         mid = (high + low) // 2
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
#         # means x is present at mid
#         else:
#             return mid
#     # If we reach here, then the element was not present
#     return -1
 
# n = int(input())
# arr = [ i for i in range(0,n+1) ]
# print(arr)
# x = 10
# result = binary_search(arr, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


# def binary(arr) :
#     step = 0
#     low = 0
#     high = len(arr)
#     mid = 0 
#     while low <= high:
#         mid = (high + low) // 2
#         high = mid - 1
#         step+=1
#     return step

# n = int(input())
# arr = [ i for i in range(0,n+1) ]
# resultt = binary(arr)
# print(resultt)






# Bo’linmas son
# Sizga N va K sonlari beriladi. K ga bo’linmaydigan N-natural sonni chop eting!

# Chiquvchi ma'lumotlar:
# Chiqish faylida yagona son, KK ga bo’linmaydigan NN-sonni chop eting!




# arr = list(map(int,input().split()))
# [n,k] = [arr[0],arr[1]]
# target = 0
# step = 0
# while n!=0 :
#     for i in range(100):
#         if i%k != 0 :
#             target = i
#         n-=1
# print(target)
# arr = list(map(int, input().split()))
# [n,m] = [arr[0],arr[1]]
# matr = []

# for i in range(1,n+1) :
#     test = input().split()
#     matr.append(test)
# print(matr)


#0226

# a = int(input())
# gamers = []
# winners = []
# score = 0
# while a!= 0:
#     gamer = input().split()
#     gamers.append(gamer)
#     a-=1
# b = int(input())
# while b!= 0:
#     gamScore= input()
#     winners.append(gamScore)
#     b-=1
# for i in range(len(gamers)) :
#     for j in range(len(winners)) :
#         if gamers[i][1] == winners[j] :
#             score += gamers[i][2]
# print(score)
# print(gamers)


#0045
# n = int(input())
# # print(n+1)
# print(int(n*(n+1)/2))

# n = int(input())
# if 0 <= n:
#     print(int(n*(n+1)//2))

# 0184

# Kamida 6 ta belgidan iborat bo’lishi kerak;
# Kamida bitta raqam qatnashishi kerak;
# Kamida bitta Ingliz alifbosining kichik harfi qatnashishi kerak
# Kamida bitta Ingliz alifbosining katta harfi qatnashishi kerak
# Kamida bitta maxsus belgi qatnashishi kerak. Maxsus belgilar: !@#$%^&*()-+

# n = int(input())
# pin = input()
# target = 5
# symbols = ["!@#$%^&*()-+"]
# if len(pin) == n :
#     if len(pin) == 6 :
#         target -=1
#     for i in pin :
#         if i in symbols :
#             target -=1
#             continue
#         if i.isalpha() and i.isupper() :
#             target -=1
#             continue
#         if i.isalpha() and i.islower() :
#             target -=1
#             continue
#         if i.isdigit() :
#             target -=1
#             continue
# print(target)



#0185
# n = int(input())
# arr = list(map(int, input().split()))
# if n < 200000 :
#     if len(arr) == n :
#         arr1 = sorted(arr)
#         minSum = arr1[-1]
#         for i in range(1, len(arr1)) :
#             diff = arr1[i] - arr1[i-1]
#             if diff < minSum :
#                 minSum = diff
#             else :
#                 minSum = minSum
# print(arr1, '\n', minSum)


#0188
# s = input()
# arr = []
# for i in range(len(s)) :
#     arr.append(i)



# a,b = map(int, input().split())
# if 1 < a and 1 < b:
#     if b-a == 2 :
#         for i in range(2, int(b/2)+1):
#             if (b % i) == 0:
#                 print("No")
#             else :
#                 print("Yes")
#     else:
#         print("No")


# def isPrime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False

#     return True


from math import factorial
n = int(input())
def is_prime(x):
    return factorial(x - 1)  % x == x - 1
print(is_prime(n))














