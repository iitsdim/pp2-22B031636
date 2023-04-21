import csv
from insert_into_phonebook import insert_phone

rows = []
with open("phone_records.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(tuple(row))

bad_phones = []
for phone in rows:
    if phone[1].isnumeric():
        insert_phone(phone[0], phone[1])
    else:
        bad_phones.append(phone)

print(*bad_phones)