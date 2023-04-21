#!/usr/bin/python

import psycopg2
from config import config


def phone_list():
    off = input("please input offset: ")
    lim = input("please input limit: ")


    sql = """
        SELECT * FROM phone_book
    """

    if off:
        sql += " OFFSET " + off
    if lim:
        sql += " LIMIT " + lim

    sql += ";"
    conn = None
    res = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(sql)
        res = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return res


# print(phone_list())


def get_number_by_username(username):
    username = '%' + username + '%'
    sql = f"SELECT * FROM phone_book WHERE username like '{username}';"
    conn = None
    res = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(sql)
        res = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return res


# print(get_number_by_username("m"))


def get_number_by_phone(phone):
    sql = f"SELECT * FROM phone_book where phone = '{phone}';"
    conn = None
    res = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(sql)
        res = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return res


# print(get_number_by_phone("234424"))
