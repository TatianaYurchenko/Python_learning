# s = "4er7te"
#
# for i in s:
#     for j in range(9):
#         if i == str(j):
#             print(j)
#             tr = s.replace(i, '')
#             s = tr
# print(tr)
# ==============
# def string_clean(s):
#     for i in s:
#         for j in range(10):
#             if i == str(j):
#                 print(j)
#                 tr = s.replace(i, '')
#                 s = tr
#      return s
# =============

def string_clean(s):
    """
    Function will return the cleaned string
    """
    for d in '0123456789':
        s = s.replace(d, '')
    return s
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))




