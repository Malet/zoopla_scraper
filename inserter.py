import json
import psycopg2
import os

def insertIntoPostgreSQL (jsonString) {


}

def main() {

    con = None

    try:

        con = psycopg2.connect(host='localhost',database='zooplatest', user='externalapi', password='test')
        cur = con.cursor()
        cur.execute(insertIntoPostgreSQL(sys.argv[1]))
        ver = cur.fetchone()
        print ver


    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)

    finally:

        if con:
            con.close()
}

main
