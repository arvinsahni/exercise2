import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

try:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.commit()
    conn.close()
except:
    print "Could not create tcount"
