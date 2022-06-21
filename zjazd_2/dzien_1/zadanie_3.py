# todo
# Wczytaj plik 'personal_dataset.txt', jego zawartość przetwórz na słownik
# i zapisz do pliku o formacie json. Możesz skorzystac z ponizszej listy pomocniczej

job_list = ['Dentist', 'Operator', 'IT Support Staff','Staffing Consultant','Clerk',
            'Healthcare Specialist','HR Coordinator','Auditor',
            'Global Logistics Supervisor','Baker','Cashier']

import re
import json

counter_id = 0
dictionaries = {}

try:
    with open("dzien_1/data/personal_dataset.txt") as f:
        contents = f.readlines()
except:
    with open("data/personal_dataset.txt") as f:
        contents = f.readlines()


for line in contents:
    counter_id = counter_id + 1
    name = re.search(r"[A-Z][a-z]+_[A-Z][a-z]+", line).group().split("_")[0]
    surname = re.search(r"[A-Z][a-z]+_[A-Z][a-z]+", line).group().split("_")[1]
    mail = re.search(r"[A-Z][a-z]+_\w+\d+@.+[.]\w{2,3}", line).group()
    date = re.search(r"\d{1,2}[\/]\d{1,2}[\/]\d{4}", line).group()
    telephone = re.search(r"\d-\d{3}-\d{3}-\d{4}", line).group()
    for index, elem in enumerate(x.replace(' ', '') for x in job_list):
        if elem in line:
            position = job_list[index]

    dictionary = {
        'name': name,
        'surname': surname,
        'mail': mail,
        'date': date,
        'telephone': telephone,
        'position': position
    }

    dictionaries[counter_id] = dictionary

with open("personal_dataset_2.json", "w") as f:
    json.dump(dictionaries, f)

print(dictionaries)


# job_list = [x.replace(' ', '') for x in job_list]
# counter_id = 0
# dictionaries = {}
#
# with open('personal_dataset.txt', 'r') as f:
#     for line in f.readlines():
#         counter_id += 1
#         telephone = re.findall(r'\d-\d{3}-\d{3}-\d{4}', line)
#         date = re.search(r'((\d\d)|(\d))/((\d\d)|(\d))/\d\d\d\d', line).group()
#         mail = re.search(r'([A-Z][a-z]+_\w+\d+@\w+.\.)(org|com|biz|tech)', line).group()
#         while mail[0].isdigit():
#             mail = mail[1:]
#         surname = mail.split('_')[1].split("@")[0]
#         name = mail.split('_')[0]
#         surname = ''.join(x for x in surname if not x.isdigit())
#         for job in job_list:
#             if re.search(job, line):
#                 position = job
#                 break
#
#         dictionary = {
#             'name': name,
#             'surname': surname,
#             'mail': mail,
#             'date': date,
#             'telephone': telephone,
#             'position': position
#         }
#         dictionaries[counter_id] = dictionary
#
# with open("personal_dataset_2.json", "w") as f:
#     json.dump(dictionaries, f)