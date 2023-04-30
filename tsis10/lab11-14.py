import psycopg2
from config import config


def query_pattern():
    pattern = input("enter pattern for search:\n")
    create_func = """
    CREATE OR REPLACE FUNCTION query_pattern(pattern VARCHAR)
      RETURNS TABLE(id INTEGER, username VARCHAR, phone VARCHAR) AS
    $$
    BEGIN
     RETURN QUERY
    
     SELECT *
     FROM phone_book
     WHERE phone_book.username like pattern OR phone_book.phone like pattern;
    
    END; $$
    LANGUAGE plpgsql;
    """

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
        cur.execute(create_func)
        cur.callproc('query_pattern', (pattern,))
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


# print(query_pattern())

def pagination_query():
    off = int(input("please input offset: "))
    lim = int(input("please input limit: "))

    create_func = """
    CREATE OR REPLACE FUNCTION query_pattern(off INTEGER, lim INTEGER)
      RETURNS TABLE(id INTEGER, username VARCHAR, phone VARCHAR) AS
    $$
    BEGIN
     RETURN QUERY

     SELECT *
     FROM phone_book
     WHERE 1=1
     OFFSET off LIMIT lim;

    END; $$
    LANGUAGE plpgsql;
    """

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
        cur.execute(create_func)
        cur.callproc('query_pattern', (off, lim,))
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


print(pagination_query())
