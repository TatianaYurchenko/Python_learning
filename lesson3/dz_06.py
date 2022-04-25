# a = [100, 40, 34, 57, 29, 72, 57, 88]
# for i in a:
#     print(i)
#
# =============
# преобразовть список в кортедж
# a = [100, 40, 34, 57, 29, 72, 57, 88]
# a = tuple(a)
# print(a)
# =============
# программа убирающяя дубликаты в списке
# a = [100, 40, 34, 34, 34, 57, 29, 72, 57, 88]
# b = set(a)
# c = list(b)
# print(c)
# =======

# data_clients = ("John", "Doe")
# client = {
#     "Name": data_clients[0],
#     "Lastname": data_clients[1]
# }
# print(client)
# print(client.__class__)
# ======

def create_client_object(name, last_name, dob, sex, city, state, zip_code):
    client = {
        "Name": name,
        "LastName": last_name,
        "DOB": dob,
        "Sex": sex,
        "City": city,
        "State": state,
        "ZipCode": zip_code
    }
    print(client.__class__)
    print(client)
    return client
create_client_object("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")

