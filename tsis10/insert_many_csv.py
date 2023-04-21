import csv
import insert_into_phonebook

rows = []
with open("phone_records.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(tuple(row))

print(header)
print(rows)

insert_into_phonebook.insert_phones(rows)
