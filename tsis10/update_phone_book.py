#!/usr/bin/python

import psycopg2
from config import config


def update_phone(pk, username, phone):
    if username and phone:
        username = f"username = '{username}'"
        phone = f"phone = '{phone}'"
        sql = f"""UPDATE phone_book
                SET {username}, {phone}
                WHERE id = {pk} RETURNING * """
    elif username:
        username = f"username = '{username}'"
        sql = f"""UPDATE phone_book
                SET {username}
                WHERE id = {pk} RETURNING *"""
    elif phone:
        phone = f"phone = '{phone}'"
        sql = f"""UPDATE phone_book
                SET {phone}
                WHERE id = {pk} RETURNING *"""
    else:
        return "No changes"


    conn = None
    new_record = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute(sql)
        new_record = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return new_record


# update_id = input("enter id of record change: ")
# new_username = input("enter new username/leave blank if you do not want to change: ")
# new_phone = input("enter new phone number/leave blank if you do not want to change: ")
#
# print(update_phone(update_id, new_username, new_phone))


def delete_phone(username, phone):
    if username and phone:
        username = f"username = '{username}'"
        phone = f"phone = '{phone}'"
        sql = f"""DELETE FROM phone_book
                WHERE {username} AND {phone}"""
    elif username:
        username = f"username = '{username}'"
        sql = f"""DELETE FROM phone_book
                        WHERE {username}"""
    elif phone:
        phone = f"phone = '{phone}'"
        sql = f"""DELETE FROM phone_book
                        WHERE {phone}"""
    else:
        return "No changes"


    conn = None
    new_record = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return "deleted"


# del_username = input("enter to delete username/leave blank if you do not want to change: ")
# del_phone = input("enter to delete phone number/leave blank if you do not want to change: ")
#
# print(delete_phone(del_username, del_phone))
