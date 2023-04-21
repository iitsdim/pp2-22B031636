
import insert_into_phonebook
from query_phone_book import get_number_by_username
from update_phone_book import update_phone

username = input("insert username:\n")
phone = input("insert phone number:\n")

was = get_number_by_username(username)

if was:
    print(update_phone(was[0][0], username, phone))
else:
    print(insert_into_phonebook.insert_phone(username, phone))
