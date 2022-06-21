# #!/usr/bin/env python
# # coding: utf-8
#
# # # PRACA Z DATAMI
#
# # ## Tworzenie zmiennych czasowych
#
#
import datetime
from dateutil import parser
# from datetime import datetime

#
# print("1 Hour")
# print(datetime.time(1))
# #
# print("2 and a half hour")
# print(datetime.time(2, 30))
# #
# print("3 hours, 45 minutes and 30 seconds")
# print(datetime.time(3, 45, 30))
#

# ts_now = datetime.datetime.now()
# # print(ts_now)
# #
# # #
# print(ts_now.day)
# #
# print(ts_now.year)
# print(ts_now.month)
# print(ts_now.minute)
# print(ts_now.second)
# print(ts_now.microsecond)
#
# print(ts_now.isoweekday())
#
# ts_xmas = datetime.datetime(2020,12,24)
# # print(type(ts_xmas))
# # print(ts_xmas)
# # #
# ts_now = datetime.datetime.now()
# ts_diff = ts_xmas - ts_now
# print (ts_diff)
# print (type(ts_diff))
# #
# #
# today = datetime.datetime.now()
# offset = datetime.timedelta(days=45, hours=13)
# print(today + offset)
#
#
# # ## KONWERSJA STRINGÓW I DAT
# # - %Y year
# # - %d day
# # - %m month
# # - %H hour
# # - %M minute
# # - %S second
#
#
# date_str =  "01-10-2015T14:34"
# date_ts = datetime.datetime.strptime(date_str,"%m-%d-%YT%H:%M")
# print(date_ts)
# print(type(date_ts))
#
# date_str = "10/01/2015"
# date_ts = datetime.datetime.strptime(date_str,"%d/%m/%Y")
# print(date_ts)
#
# print(type(date_ts))
#
# 2015-01-10 00:00:00
# new_date_str = datetime.datetime.strftime(date_ts, "%H:%M:%S %m-%d-%Y")
# print(new_date_str)
# print(type(new_date_str))
# # #
# # #
# print(f'{date_ts.month}-{date_ts.year}')
#
#
# from datetime import datetime
# new_date_str = datetime.strftime(date_ts, "%H:%M:%S %m-%d-%Y")
# print(new_date_str)
# print(type(new_date_str))

#
# # PARSE
#
# from dateutil.parser import parse
# print(parse('January 31, 2010'))
# print(parse("2003-01-04T10:49:41"))
#
# # todo
# # 1. Stwórz zmienną future (typ datetime), której data to 20 stycznia 2021 o 22:34


# # todo
# # 2. Zamień poniższą datę na napis: ’31 January, 2001, Wednesday’
# dt = datetime.datetime(2001, 1, 31)

#
# # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
#
# # todo
# # 3. Stwórz zmienną, która jest różnicą czasu future i chwili obecnej.
# wynik wyświetl w sekundach

# future = datetime.datetime(2022,11,20,22,34)

# # todo
# # 4. Zamień napis 'Jan 20, 2017 5pm' na zmienną typu czas
# s = 'Jan 20, 2017 5pm'

#
# # todo
# # 5. W poniższej liście dat znajdź najstarszą.
# Wyświetl czas, jaki upłynął od tej chwili do teraz w sekundach
datetime_list = ['25.08.1995 00:00:00', '22.07.1999 00:00:00', '01.01.2001 13:42:59', '13.12.2011 01:02:03']

#
# # todo
# # 6. Ile minęło sobót pomiędzy dwoma poniższymi datami, które przypadają na dzień podzielny przez 3? (odp: 14)
#
# d1 = datetime.date(1869, 1, 2)
# d2 = datetime.date(1869, 10, 2)
