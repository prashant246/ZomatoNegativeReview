'''
in this file we have maanged all the functionality related to the databases
'''

import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='zomato_data',
                                       user='root',
                                       password='makeitlarge')
        if conn.is_connected():
            return conn

    except Error as e:
        print(e)

def insert(id, rating_text, sentiment, user, user_url, rating):
    try :
        conn = connect()
        cursor = conn.cursor()
        query = "INSERT INTO review_data VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, rating, rating_text, sentiment[:499], user, user_url[:99]))
        conn.commit()

    except Error as error :
        print "error in insert" + str(error)

    finally:
        cursor.close()
        conn.close()

def find(id) :
    try :
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT * FROM review_data WHERE review_id  = %s"
       # args = id


        cursor.execute(query, (id,))
        row = cursor.fetchone()
        if row is None :
            return True
        else:
            return False

    except Error as error :
        print "error in finding" + str(error)

    finally:
        cursor.close()
        conn.close()


def delete():
    try :
        conn = connect()
        cursor = conn.cursor()
        query = "DELETE FROM review_data"

        cursor.execute(query)
    except Error as error :
        print "error in deleting"

    finally:
        cursor.close()
        conn.close()
