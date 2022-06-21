#todo
# Przetwórz plik timelog.txt, aby miał formę taką jak timelog_final.txt
# (odpowiednią ilość spacji można pominąć jak w pliku new_timelog.txt)

import re
from datetime import datetime

try:
    with open("dzien_1/data/timelog.txt") as f:
        contents = f.readlines()
except:
    with open("data/timelog.txt") as f:
        contents = f.readlines()

for elem in contents:
    print(elem)

lines = [elem for elem in contents if elem != "\n"]
hours = [elem[:5] for elem in lines]
activities = [elem[6:-1] for elem in lines]

starting_hours = hours[:-1]
ending_hours = hours[1:]

new_lines = []
for line, ending_hour in zip(lines, hours):
    if "End" not in line:
        new_lines.append(line[:5] + '-' + ending_hour + line[5:])
    else:
        new_lines.append("\n")

starting_hours = [datetime.strptime(x, '%H:%M') for x in starting_hours]
ending_hours = [datetime.strptime(x, '%H:%M') for x in ending_hours]

time_diff = [x - y for x, y in zip(ending_hours, starting_hours)]
time_diff_minutes = [x.seconds / 60 for x in time_diff]

activity_time_dictionary = {}
for key, value in zip(activities, time_diff_minutes):
    if key not in activity_time_dictionary.keys():
        activity_time_dictionary[key] = value
    else:
        activity_time_dictionary[key] += value

del activity_time_dictionary['End']
print(activity_time_dictionary)

from collections import OrderedDict # ekstra dodatek, ale można tez bez tego sie obejsc
activity_time_dictionary_ordered = OrderedDict(sorted(activity_time_dictionary.items()))
print(activity_time_dictionary_ordered)

sum_of_all = sum(activity_time_dictionary_ordered.values())
print(sum_of_all)

percents = [x/sum_of_all*100 for x in activity_time_dictionary_ordered.values()]
percents = [round(x) for x in percents]
print(percents)

new_lines_2 = []
for key, value, percent in zip(activity_time_dictionary_ordered.keys(),
                               activity_time_dictionary_ordered.values(),
                               percents):
    new_lines_2.append(key + '\t' + str(int(value)) + ' minutes' + ' ' + str(percent) + '%' + '\n')

for line in new_lines:
    print(line)

for line in new_lines_2:
    print(line)
