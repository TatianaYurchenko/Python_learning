# m, n = 5, 1
# if m < n:
#     for i in range(m, n+1):
#         print(i)
# else:
#     for i in range(m, n-1, -1):
#         print(i)
# =================
m, n = 23, 2
k = 1 - 2 * (m > n)
for i in range(m, n + k, k):
    print(i)
