# def better_than_average(class_points, your_points):
#     count = 0
#     s = 0
#     for i in class_points:
#         s = s + i
#         count = count + 1
#     print(s)
#     print(count)
#     if s / count <= your_points:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
#
# better_than_average([5,2], 5)
# =======================

def better_than_average(class_points, your_points):
    a = your_points > sum(class_points) / len(class_points)
    print(a)
    return a

better_than_average([5,2], 5)