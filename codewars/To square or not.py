def square_or_square_root(arr):
    c = []
    import math
    for i in arr:
        if i % math.sqrt(i) == 0:
            b = math.sqrt(i)
            c.append(int(b))
        else:
            b = i * i
            c.append(b)

    return c
print(square_or_square_root([2,4,9]))
__________
# тестировнаие программы "Если число имеет целый квадратный корень, возьмите его, иначе возведите число в квадрат"
# from solution import square_or_square_root
#
#
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         tests = [
#             [[4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]],
#             [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
#             [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
#         ]
#
#         for inp, exp in tests:
#             test.assert_equals(square_or_square_root(inp), exp)
