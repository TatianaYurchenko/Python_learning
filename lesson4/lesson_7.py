# file = open("text.txt", "r")
# print(file.read())
# ==========
# def create_insert(a):
#     file = open("text_1", "w")
#     file.write(a)
#     file.close()
# create_insert("w - Write - Opens a file for writing, creates the file if it does not exist")
# =============
# Написать функцию кот получает 2 параметра, 1-й имя файлв, 2-й символ (letter, number)
# Заменить все символы на 0
# def change_character(a, b):
# #     for i in a:
# #         if i == b:
# #             tr = a.replace(b, '0')
# #     print(tr)
# #
# # change_character("Opens a file for writing, creates the file if it does not exist", "e")
# # ==========
# # Вариант 2

def change_character(file_name, letter):
    with open(file_name, 'r') as file:
        content = file.read()

    transformed = content.replace(letter, '0')

    with open(file_name, 'w') as file:
        file.write(transformed)

change_character(text_2.txt, "e")
