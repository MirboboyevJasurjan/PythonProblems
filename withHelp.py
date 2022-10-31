# n = int(input("N:"))
# i = 2
# sumA = 0
# if 1 <= n <= 20 :
#   while i <= n :
#     sumA = sumA + 1*i+1
#     print(sumA)
#     break
# i+=1
# print(sumA)


# n = int(input())
# i = 2
# sumA = 0
# def f(n):
#     if n <= 2:
#         return 1
#     return f(n-1) + f(n-2)
# if 1 <= n <= 20 :
#   while i <= n :
#     sumA = 1 if n<=2 else f(n-1) + f(n-2) 
#     i+=1
# print(sumA)




def count_diags(n):
    if 3 <= n <= 10**9:
        return (n * (n - 3)) // 2
    elif n < 3 :
        return 0
n = int(input())
print(count_diags(n))