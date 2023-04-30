import psycopg2
from config import config


def delete_by_username_or_phone():
    pattern = input("enter pattern for search:\n")
    create_func = """
    CREATE OR REPLACE PROCEDURE delete_by_pattern(pattern VARCHAR)
    AS $$
    BEGIN

     DELETE FROM phone_book
     WHERE phone_book.username like pattern OR phone_book.phone like pattern;

    END; $$
    LANGUAGE plpgsql;
    """

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(create_func)
        cur.execute('CALL delete_by_pattern(%s)', (pattern,))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return "Deleted"

delete_by_username_or_phone()
