# todo
# Na podstawie pliku 'apache_access.log' policz ile było zapytań GET z
# adresu localhost (127.0.0.1) pomiędzy 10:40 a 10:55 ()
import datetime
import pytz  # ekstra dodatek, ale nie trzeba
import re

with open("dzien_1/data/apache_access.log") as f:
    access_log = f.readlines()

print(access_log)

list_1 = [re.search(r'^\d*.\d*.\d*.\d*', elem).group() for elem in access_log]
print(list_1)

list_2 = [datetime.datetime.strptime(re.search('\d\d:\d\d:\d\d ', elem).group()[:-1], "%H:%M:%S") for elem in access_log]
print(list_2)

index_list = [
    index for index, elem in enumerate(list_1) if elem == "127.0.0.1"
]

my_list = [list_2[i] for i in index_list]



t1 = datetime.datetime(1900,1,1,10,40,00)
t2 = datetime.datetime(1900,1,1,10,55,00)

counter = 0
for elem in my_list:
    if elem > t1 and elem < t2:
        counter += 1
print(counter)

# Rozwiazanie Oliwii:
# import datetime
# import pytz # ekstra dodatek, ale nie trzeba bylo uzyc
# import re
#
# with open('data/apache_access.log', 'r') as f:
#     linie = f.readlines()
#
# print(linie)
#
# start = datetime.datetime(2007,4,10, 10, 40)
# end = datetime.datetime(2007,4,10, 10, 55)
# counter = 0
#
# for line in linie:
#     czas = re.search(r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}', line).group()
#     czas = datetime.datetime.strptime(czas, '%d/%b/%Y:%H:%M:%S')
#     if line.startswith('127.0.0.1 '):
#         if czas>start and czas<end:
#             print(czas)
#             counter +=1
#
# print(counter)
