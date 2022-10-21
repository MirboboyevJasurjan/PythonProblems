import math
#a, b = input().split()
#sums = int(a) // int(b)
#print(sums)

#a, b, c = input().split()
#forA = int(a) // 2
#forB = int(b) // 2
#forC = int(c) // 2
#sums = forA + forB + forC
#print(sums)

#a, b, c = input().split()
#aa = int(a) 
#bb = int(b)
#cc = int(c)
#if aa > 0 and bb > 0 and cc > 0 :
  #forA = aa // 2
  #forB = bb // 2
  #forC = cc // 2
  #sums = forA + forB + forC
  #print(sums)

#n = int(input())
#if 100 > n > 0 :
	#print(n // 10)

#n = str(input())
#print(int(n[-1]))


#hh1, mm1, ss1 = input().split()
#hh2, mm2, ss2 = input().split()
#if int(hh1) <= 23 and int(hh2) <= 23 and int(mm1) <= 59 and int(mm2) <= 59 and int(ss1) <= 59 and int(ss2) <= 59 :
    #h = (int(hh2)-int(hh1)) * 3600
    #m = (int(mm2)-int(mm1)) * 60
    #s = int(ss2)-int(ss1)
    #summ = h+m+s
#    print(summ)

#25

#n = int(input())
#h = n // 3600
#m = int(n / 3600  * 60)
#s = n % 3600
#m==0 if m == 60 else m == m
#print(h,m,s)

#a,b = input().split()
#aa = int(a)
#bb = int(b)
#if aa > 0:
    #print(bb+1)
#else:
    #print(1)

# a,b = input().split()
# aa = int(a)
# bb = int(b)
# if aa > 0:
#     vir = bb+1
#     print(vir**2)
# else:
#     print(1)

# serie = input()
# sad = 1 if serie == "A089957" else 0
# print(sad)

# a,b = input().split()
# aa = int(a)
# bb = int(b)
# if aa > 0:
#     vir = bb+1
#     print(vir**2)
# else:
#     print(1)



# aa,bb,cc = input("a,b,c").split()
# [a,b,c] = [int(aa),int(bb),int(cc)]
# ab = math.lcm(a,b)
# ac = math.lcm(ab,c)
# print(ac)

# n = int(input())
# arr = [1,2,3,4,5,6]
# arrRev = [6,5,4,3,2,1]
# ind = 0
# while n  >  ind :
#     ind+=1
# if ind == 1:
#     print(6)
# else :
#     print(arrRev.index(ind-1))

# aa,bb,cc = input().split()
# [a,b,c] = [int(aa),int(bb),int(cc)]
# if a>b and a>c :
#   print(a)
# elif b>a and b>c:
#   print(b)
# elif c>a and c>b :
#   print(c)

# n = int(input())
# sc = input()
# arr = []
# for i in range(1, n+1):
# 	arr.append(i)
#     if arr[i] == sc[i]:
#         print("Yes")
#     else :
#         print("No")
#     print(sc, "\n", arr)