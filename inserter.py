import json
import psycopg2
import os

dumpJsonTableName = "zooplajsondump"

# Me am SMART?
def insertJsonDumpIntoPostgreSQL (jsonString):
    sqlCommandString = "INSERT INTO " + dumpJsonTableName + " VALUES ( default," + json.dumps(jsonString) + ")"
    connectionHandler(sqlCommandString)

def cleanDumpPostgreSQL() :
    return None

def connectionHandler(sqlCommandString):

    con = None

    try:

        con = psycopg2.connect(host='localhost',database='zooplatest', user='externalapi', password='test')
        cur = con.cursor()
        cur.execute(sqlCommandString)

    except:
        print(psycopg2.DatabaseError)
        sys.exit(1)

    finally:

        if con:
            con.close()

list(map(print,os.sys.argv[1:]))
    #sqlCommandString = insertDumpIntoPostgreSQL(jsonString)
    #connectionHandler(sqlCommandString)
