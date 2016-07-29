import psycopg2
import sys


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
if len(sys.argv)<=1:
        cur.execute("SELECT word, count from tweetwordcount ORDER BY word")
        records = cur.fetchall()
        for rec in records:
                print "word = ", rec[0]
                print "count = ", rec[1], "\n"

else:
     	findword=str.format(sys.argv[1])
        cur.execute("SELECT * from tweetwordcount WHERE word = %s",(findword,))
        records = cur.fetchall()
        if not(records):
                print "not found in the table"
        else:
             	for rec in records:
                        print "word = ", rec[0]
			print "count = ", rec[1], "\n"

else:
     	findword=str.format(sys.argv[1])
        cur.execute("SELECT * from tweetwordcount WHERE word = %s",(findword,))
        records = cur.fetchall()
        if not(records):
                print "not found in the table"
        else:
             	for rec in records:
                        print "word = ", rec[0]
                        print "count = ", rec[1], "\n"

conn.commit()
conn.close()
