# def vazifa2(arr) :
#     sumAll = 0
#     i = 0
#     while i != len(arr) :
#         sumAll += arr[i]
#         i += 1
#     arif = sumAll / i
#     indexArif1 = arr.index(int(arif))
#     indexArif2 = arr.index(int(arif)+1)
#     return sumAll, i, arif, indexArif1, arr[indexArif1], indexArif2, arr[indexArif2] 

# arr1 = [1,2,3,4,5,6,7,8,9,10] # Oddiy test
# # arr1 = list(map(int, input().split()))   # szning test caseingiz  
# print(vazifa2(arr1))
# print("O'rta arifmetik = ", vazifa2(arr1)[2])
# print(arr1)
# print("Element",  vazifa2(arr1)[4])
# print("Index", vazifa2(arr1)[3])
# print("Element", vazifa2(arr1)[6])
# print("Index", vazifa2(arr1)[5])




# class Vazifa_2(object):
#     # @classmethod
#     def main(cls, args):
#         a = [1, 2, 3, 4, 5, 6, 7, 8]
#         k = 0
#         sum = 0
#         x = 0
#         y = 0
#         i = 0
#         while len(a):
#             sum += a[i]
#             i += 1
#         k = len(a)
#         print ("O'rta arifmetik=", + k)
#         Arrays.sort(a)
#         print(Arrays.toString(a))
#         i = 0
#         while len(a):
#             if k <= a[i]:
#                 print("element=" + a[i] + "\nindeksi=" + i)
#                 break
#             i += 1
#         i = len(a)
#         while i >= 0:
#             if k >= a[i]:
#                 print("element=" + a[i] + "\nindeksi=" + i)
#                 break
#             i -= 1